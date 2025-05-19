import csv

with open("test.csv") as (cs):
    csv_reader = csv.reader(cs)
    for i in csv_reader:
        print(i)
cs.close