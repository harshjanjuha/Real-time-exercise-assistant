import pandas as pd

# Assuming 'treepose.csv' contains your DataFrame
df = pd.read_csv('warrior.csv')
# df.info()
# df2 = pd.read_csv('tpose.csv')
# df2.info()
# # Assuming the column you want to modify is named 'column_name'
# # Replace 'column_name' with the actual name of your column
last_10_indices = df.index[-35:]
df.loc[last_10_indices, 'pose'] = "Warrior II Pose"
last_10_indices = df.index[-6:]
df.loc[last_10_indices, 'pose'] = "Unknown Pose"

# df['pose'] = df['pose'].replace('Tree Pose','Plank Pose')
# Save the modified DataFrame back to CSV if needed
df.to_csv('midplank.csv', index=False)
