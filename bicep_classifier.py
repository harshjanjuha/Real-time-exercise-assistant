import csv

import cv2
import math
import numpy as np
from time import time
from angle_calculator import AngleCalculator
import mediapipe as mp

class BicepClassifier:
    def __init__(self):
        self.prev_state = None
        self.bicep_count = 0

    def classify(self, landmarks, prev_state, output_image):
        # Your classification logic here

        left_elbow_angle = AngleCalculator().calculate_angle(landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value],
                                            landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value],
                                            landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value])

        right_elbow_angle = AngleCalculator().calculate_angle(landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value],
                                            landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value],
                                            landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value])

        label = ''
        if left_elbow_angle > 140 and left_elbow_angle < 170 or right_elbow_angle > 140 and right_elbow_angle < 170:            
            if prev_state != 'down':
                label = 'down'
                prev_state = 'down'
        elif left_elbow_angle > 20 and left_elbow_angle < 70 or right_elbow_angle > 20 and right_elbow_angle < 70:
            if prev_state == 'down':
                self.bicep_count += 1
                with open('data/gymstat.csv', 'a', newline='\n') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['bicep_curls', self.bicep_count])
                print("Row added successfully to", 'gymstat.csv')

                prev_state = 'up'
                label = 'up'
        cv2.putText(output_image, f'Bicep: {self.bicep_count}', (10, 60), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)      

        return output_image,label, prev_state 
