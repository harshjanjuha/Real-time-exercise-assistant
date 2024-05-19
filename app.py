import os

from flask import Flask, render_template, request
from video_stream import VideoStream
import pandas as pd
import datetime
from calories_calc import CalorieCalc
import matplotlib.pyplot as plt
app = Flask(__name__)

# Initialize the VideoStream object
video_stream = VideoStream()


def get_pose_duration(pose: str):
    if pose == 'T Pose':
        file_name = 'tpose'
    elif pose == 'Tree Pose':
        file_name = 'treepose'
    elif pose == 'Warrior II Pose':
        file_name = 'warrior'
    elif pose == 'Plank Pose':
        file_name = 'plank'
    df = pd.read_csv(f'data/{file_name}.csv')
    df = df.applymap(str)

    t_pose_duration = 0
    t_pose_start = 0
    t_pose_end = 0
    for i, r in df.iterrows():
        prev_label = df.iloc[i - 1]['pose']
        if r['pose'] == pose and prev_label == 'Unknown Pose':
            t_pose_start = datetime.datetime.strptime(r['timestamp'], "%Y-%m-%d %H:%M:%S")
        elif r['pose'] == 'Unknown Pose' and prev_label == pose:
            t_pose_end = datetime.datetime.strptime(r['timestamp'], "%Y-%m-%d %H:%M:%S")
            t_pose_duration += (t_pose_end - t_pose_start).total_seconds()
    return t_pose_duration


def get_rep_count():
    df = pd.read_csv('data/gymstat.csv')
    reps = df.groupby('Exercise').count()
    bicep_count = reps['measure']['bicep_curls']
    pushup_count = reps['measure']['pushup_count']
    return {'bicep_curl': bicep_count, 'pushup': pushup_count}


def get_report(weight: str = 70):
    calical = CalorieCalc()
    pose_dct = {}
    for pose in ['T Pose', 'Tree Pose', 'Warrior II Pose', 'Plank Pose']:
        duration = get_pose_duration(pose)
        if duration > 0:
            pose_dct[pose] = duration
    reps_dct = get_rep_count()
    reps_dct = {**reps_dct, **pose_dct}
    calorie_dct = {}
    for key, val in reps_dct.items():
        calorie_dct[key] = calical.calculate_calories_burnt(weight=float(weight), exercise_type=key,
                                                            exercise_intensity=float(val))
    return calorie_dct,reps_dct


def generate_graphs(calorie_dct):
    exercise_calories = calorie_dct
    if not os.path.exists('graphs'):
        os.makedirs('graphs')

    # Pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(exercise_calories.values(), labels=exercise_calories.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Percentage Contribution of Each Exercise')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.savefig('static/graphs/pie_chart.png')
    plt.close()

    # Bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(exercise_calories.keys(), exercise_calories.values(), color='skyblue')
    plt.xlabel('Exercise')
    plt.ylabel('Calories Burnt')
    plt.title('Calories Burnt by Each Exercise')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/graphs/bar_graph.png')
    plt.close()

    print("Graphs saved successfully in the 'graphs' directory.")


@app.route('/getreport', methods = ['GET','POST'])
def get_reports():
    weight = request.form['weight']
    calorie_report,reps_dct = get_report(weight)
    generate_graphs(calorie_dct=calorie_report)

    return render_template('final_report.html', clorie_dct = calorie_report, reps_dct = reps_dct)



@app.route('/', methods=['GET', 'POST'])
def index():
    # clear_report_csv()
    if request.method == 'POST':
        choice = request.form['choice']
        if choice == '1':
            video_stream.set_classifier('pushup')
        elif choice == '2':
            video_stream.set_classifier('bicep')
        elif choice == '3':
            video_stream.set_classifier('plank')
        elif choice == '4':
            video_stream.set_classifier('Tree')
        elif choice == '5':
            video_stream.set_classifier('TPose')
        elif choice == '6':
            video_stream.set_classifier('WarriorPose')
        elif choice == '7':
            return render_template('report_wait.html')

    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return video_stream.stream()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
