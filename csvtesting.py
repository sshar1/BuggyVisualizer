import csv

# Path to the CSV file
csv_file_path = 'Sheet1.csv'

# Read data from the CSV file
with open(csv_file_path, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Read the header row
    data = [row for row in csvreader]  # Read the rest of the data
    for row in data:
        print(row[0])
        value = row[0]
        value = float(value)
        value *= 100000
        point = value % 1000
        pixel = (304 - point) * 2.14
        print(point, pixel)

# Print the header and data