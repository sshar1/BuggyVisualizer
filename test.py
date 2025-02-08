import tkinter as tk
from tkinter import Tk, Label, Button, PhotoImage
import pandas as pd
import csv

root = Tk()
root.title("Buggy Visualizer")
root.geometry("1235x780") 

background_image = PhotoImage(file="buggy-course1.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()

def getPoint():
    # Path to the CSV file
    csv_file_path = 'Sheet1.csv'

    # Read data from the CSV file
    with open(csv_file_path, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Read the header row
        data = [row for row in csvreader]  # Read the rest of the data
        for row in data:
            point = row[0]
            substring = point[5:]
            print(int(substring) / 10000)
