import csv
filename = "data.csv"
with open(filename, 'r') as csvfile:
  csv_reader = csv.reader(csvfile)
  for row in csv_reader:
    print(row)
