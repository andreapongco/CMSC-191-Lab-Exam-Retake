"""
Developed by Andrea Kristine S. Pongco
Student Number: 2020-01929
Laboratory Exam Retake
"""

import csv
import re

# open the csv file input as a Dictionary
with open("../input_file/Exam_Table.csv", "r", encoding="utf-8-sig") as input_file:
    reader = csv.DictReader(input_file)

    # open a new csv file as output and write a new column called “HRID” where the
    # value is the concatenation of location, site, and replicate
    with open("../Pongco_B6_answer/b6_output1.csv", "w", newline='') as output_file:
        reader.fieldnames.append('HRID')
        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames, delimiter=",")
        writer.writeheader()

        for row in reader:
            if row['Date'] != '':
                row['HRID'] = f"{row['Location']}-{row['Site']}-{row['Replicate']}"
                row['HRID'] = re.sub(r'\s*,\s*', '-', row['HRID'])

                writer.writerow(row)







