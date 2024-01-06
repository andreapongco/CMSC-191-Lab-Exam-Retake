"""
Developed by Andrea Kristine S. Pongco
Student Number: 2020-01929
Laboratory Exam Retake
"""

import csv

# open the csv file input as a Dictionary
with open("../input_file/Exam_Table.csv", "r", encoding="utf-8-sig") as input_file:
    reader = csv.DictReader(input_file)

    # open a new csv file as output and only write the average count for Pomacentrus adeluse
    with open("../Pongco_B5_answer/b5_output1.csv", "w", newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=['Scientific Name', 'Average Count'], delimiter=",")
        writer.writeheader()

        scientific_name_w_size = {}

        for row in reader:
            if row['Scientific Name'].lower() == 'Pomacentrus adelus'.lower():
                try:
                    scientific_name_w_size[row['Scientific Name']]['count'] += int(row['Count'])
                    scientific_name_w_size[row['Scientific Name']]['length'] += 1
                except KeyError:
                    scientific_name_w_size[row['Scientific Name']] = {
                        'count' : int(row['Count']),
                        'length' : 1
                    }

        for i in scientific_name_w_size:
            writer.writerow({'Scientific Name' : i, 'Average Count' : scientific_name_w_size[i]['count']/scientific_name_w_size[i]['length']})





