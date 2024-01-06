"""
Developed by Andrea Kristine S. Pongco
Student Number: 2020-01929
Laboratory Exam Retake
"""

import csv

# open the csv file input as a Dictionary
with open("../input_file/Exam_Table.csv", "r", encoding="utf-8-sig") as input_file:
    reader = csv.DictReader(input_file)

    # open a new csv file as output and only write the rows with Genus starting with "St", case insensitive
    with open("../Pongco_B2_answer/b2_output1.csv", "w", newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames, delimiter=",")
        writer.writeheader()

        for row in reader:
            if (row['Genus'][0:2]).lower() == "st":
                writer.writerow(row)
