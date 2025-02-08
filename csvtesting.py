import csv
import pandas as pd

# Path to the CSV file
csv_file_path = 'Sheet1.csv'

df = pd.read_csv(csv_file_path).iloc[::3]

print(df)

# Read data from the CSV file
for row in df:
    value = row[0]
    lval = row[2]
    print(value, lval)
    #value = 40.441778 -float(value)
    #lval = 79.9418917 + float(lval)
    #value *= 1000000
    #lval *= 1000000
    #pixel = (value) * 2.14
    #lpix = (lval) * 1.64
    #print(pixel, lpix)

# Print the header and data