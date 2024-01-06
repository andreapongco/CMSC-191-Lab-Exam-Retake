"""
Developed by Andrea Kristine S. Pongco
Student Number: 2020-01929
Laboratory Exam Retake
"""

import pandas as pd

df = pd.read_csv('../input_file/Exam_Table.csv') #read csv file
df = df.T #transpose the data

df.to_csv('../Pongco_B7_answer/b7_output1.csv', index=False)