"""
Developed by Andrea Kristine S. Pongco
Student Number: 2020-01929
Laboratory Exam Retake
"""

import csv

# open the csv file input as a Dictionary
with open("../input_file/Exam_Table.csv", "r", encoding="utf-8-sig") as input_file:
    reader = csv.DictReader(input_file)

    # open a new csv file as output and only write the unique Scientific names with their corresponding average estimated size
    with open("../Pongco_B4_answer/b4_output1.csv", "w", newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=['Scientific Name', 'Average Estimated Size'], delimiter=",")
        writer.writeheader()

        scientific_name_w_size = {}

        for row in reader:
            if row['Size Est (cm)'] != '':
                try:
                    scientific_name_w_size[row['Scientific Name']]['size'] += int(row['Size Est (cm)'])
                    scientific_name_w_size[row['Scientific Name']]['count'] += 1
                except KeyError:
                    scientific_name_w_size[row['Scientific Name']] = {
                        'size' : int(row['Size Est (cm)']),
                        'count' : 1
                    }

        for i in scientific_name_w_size:
            writer.writerow({'Scientific Name' : i, 'Average Estimated Size' : scientific_name_w_size[i]['size']/scientific_name_w_size[i]['count']})





