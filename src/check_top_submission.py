import csv

with open("output/submission.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for i, row in enumerate(reader):
        print(row)

        if i == 10:
            break