import datetime
import time
import pandas as pd
# # # t1 = datetime.datetime.now()
# # # time.sleep(10)
# # # t2 = datetime.datetime.now()
# # # print((t2-t1).total_seconds())
# # from datetime import datetime
# #
# # timestamps = [
# # "2024-05-15 17:03:44.045596",
# # "2024-05-15 17:03:44.242842",
# # '2024-05-15 17:03:44.420691',
# # '2024-05-15 17:03:44.575371',
# # '2024-05-15 17:03:44.738223',
# # '2024-05-15 17:03:44.913685',
# # '2024-05-15 17:03:45.069666',
# # '2024-05-15 17:03:45.229713',
# # '2024-05-15 17:03:45.408742',
# # '2024-05-15 17:03:45.570147',
# # '2024-05-15 17:03:45.728477',
# # '2024-05-15 17:03:45.891742',
# # '2024-05-15 17:03:46.082690',
# # '2024-05-15 17:03:46.250359',
# # '2024-05-15 17:03:46.417087',
# # '2024-05-15 17:03:46.589201',
# # '2024-05-15 17:03:46.751678',
# # '2024-05-15 17:03:46.922779'
# # ]
# #
# # # Convert timestamps to datetime objects
# # timestamps = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S.%f") for ts in timestamps]
# #
# # # Calculate time differences
# # differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
# #
# # # Calculate the average time difference
# # average_difference = sum(differences, datetime.min - datetime.min) / len(differences)
# #
# # print(average_difference)
# # List of time durations in seconds
# time_durations = [
#     0.173425, 0.178189, 0.189662, 0.174107, 0.178667,
#     0.163062, 0.171652, 0.172982, 0.191528, 0.189007,
#     0.170567, 0.186868, 0.175289, 0.18374, 0.179659,
#     0.15403, 0.172154, 0.203105, 0.175771, 0.172173
# ]
#
# # Calculate total time in seconds
# total_seconds = sum(time_durations)
#
# print("Total seconds:", total_seconds)
df = pd.read_csv("T_pose.csv")
print(len(df))
