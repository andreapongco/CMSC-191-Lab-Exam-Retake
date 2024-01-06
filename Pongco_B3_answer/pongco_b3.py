"""
Developed by Andrea Kristine S. Pongco
Student Number: 2020-01929
Laboratory Exam Retake
"""

import csv

# open the csv file input as a Dictionary
with open("../input_file/Exam_Table.csv", "r") as input_file:
    reader = csv.DictReader(input_file)

    # open a new csv file as output and only write the rows with Genus starting with "St", case insensitive
    with open("../Pongco_B3_answer/b3_output1.csv", "w", newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=['Scientific Name'], delimiter=",")
        writer.writeheader()

        unique_scientific_names = []

        for row in reader:
            if row['Scientific Name'] not in unique_scientific_names and row['Scientific Name'] != "":
                unique_scientific_names.append(row['Scientific Name'])
                writer.writerow({'Scientific Name' : row['Scientific Name']})




