"""
Developed by Andrea Kristine S. Pongco
Student Number: 2020-01929
Laboratory Exam Retake
"""

import csv

# open the csv file input as a Dictionary
with open("../input_file/Exam_Table.csv", "r", encoding="utf-8-sig") as input_file:
    reader = csv.DictReader(input_file)

    # open a new csv file as output and only write the rows with interval of 30-0
    with open("../Pongco_B1_answer/b1_output1.csv", "w", newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames, delimiter=",")
        writer.writeheader()

        for row in reader:
            if row['Interval'] == "30-0":
                writer.writerow(row)
