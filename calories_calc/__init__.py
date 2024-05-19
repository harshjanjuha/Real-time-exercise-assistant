class CalorieCalc():
    def calculate_calories_burnt(self,weight : float, exercise_type: str, exercise_intensity: float):
        """
        Calculate the amount of calories burnt during an exercise.

        Parameters:
            weight (float): Weight of the person in kilograms.
            exercise_type (str): Type of exercise ('bicep_curl', 'pushup', 'plank', 'tree_pose', 'warrior_pose', or 't_pose').
            exercise_intensity (float): Intensity of exercise in repetitions (for bicep curl, push-up, tree pose, warrior pose, or T-pose)
                                         or duration in seconds (for plank).

        Returns:
            float: Amount of calories burnt.
        """

        calories_burnt_per_rep_bicep_curl = 0.025 * weight  # Calories burnt per repetition during bicep curls
        calories_burnt_per_rep_pushup = 0.05 * weight  # Calories burnt per repetition during push-ups
        calories_burnt_per_second_plank = 0.000291667 * weight  # Calories burnt per second during plank (0.0175/60)
        calories_burnt_per_second_tree_pose = 0.0025 * weight  # Calories burnt per second during tree pose
        calories_burnt_per_second_warrior_pose = 0.003 * weight  # Calories burnt per second during warrior pose
        calories_burnt_per_second_t_pose = 0.001 * weight  # Calories burnt per second during T-pose

        if exercise_type == 'bicep_curl':
            calories_burnt_per_unit_intensity = calories_burnt_per_rep_bicep_curl
        elif exercise_type == 'pushup':
            calories_burnt_per_unit_intensity = calories_burnt_per_rep_pushup
        elif exercise_type == 'Plank Pose':
            calories_burnt_per_unit_intensity = calories_burnt_per_second_plank  # No calories burnt during plank exercise
        elif exercise_type == 'Tree Pose':
            calories_burnt_per_unit_intensity = calories_burnt_per_second_tree_pose  # No calories burnt during tree pose
        elif exercise_type == 'Warrior II Pose':
            calories_burnt_per_unit_intensity = calories_burnt_per_second_warrior_pose  # No calories burnt during warrior pose
        elif exercise_type == 'T Pose':
            calories_burnt_per_unit_intensity = calories_burnt_per_second_t_pose  # No calories burnt during T-pose
        else:
            return "Invalid exercise type. Please choose 'bicep_curl', 'pushup', 'plank', 'tree_pose', 'warrior_pose', or 't_pose'."
        return round(exercise_intensity * calories_burnt_per_unit_intensity , 2)

if __name__ == '__main__':
    # Example usage:
    weight = 70  # Weight of the person in kilograms
    bicep_curl_count = 30  # Number of bicep curls

    calicalc = CalorieCalc()
    calories_burnt_bicep_curl = calicalc.calculate_calories_burnt(weight, 'bicep_curl', bicep_curl_count)

    print("Calories burnt during bicep curls:", calories_burnt_bicep_curl)
