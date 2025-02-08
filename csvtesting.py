import csv

# Path to the CSV file
csv_file_path = 'Sheet1.csv'

# Read data from the CSV file
with open(csv_file_path, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Read the header row
    data = [row for row in csvreader]  # Read the rest of the data
    for row in data:
        value = row[0]
        lval = row[2]
        print(value, lval)
        value = 40.441778 -float(value)
        lval = 79.9418917 + float(lval)
        value *= 1000000
        lval *= 1000000
        pixel = (value) * 2.14
        lpix = (lval) * 1.64
        print(pixel, lpix)

# Print the header and data