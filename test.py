import tkinter as tk
from tkinter import Tk, Label, Button, PhotoImage
import pandas as pd
import csv

root = Tk()


canvas = tk.Canvas(root, height=780, width=1235)
canvas.pack()

try:
    bg_image = tk.PhotoImage(file="buggy-course1.png")
    # Create the image on the canvas
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
except FileNotFoundError:
    print("Error: Image file not found. Please check the path.")
    # If image not found, set a default background color
    canvas.config(bg="lightblue")







def getPoint(root):
    # Path to the CSV file
    csv_file_path = 'Sheet1.csv'

    with open(csv_file_path, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Read the header row
        data = [row for idx, row in enumerate(csvreader) if idx % 5 == 0]  # Read every 10th data row

        for i in range(len(data)):
            row = data[i]
            lat = row[0]
            long = row[2]

            y = 40.441778 -float(lat)
            x = float(long) + 79.9418917 
            
            y *= 100000
            x *= 100000
            pixelY = abs(y * 2.14)
            pixelX = abs(x * 1.64)
            
            print(pixelX, pixelY)
            canvas.create_oval(1150 - pixelX, pixelY + 7, 1150 - pixelX - 3, pixelY + 9, fill='yellow', outline='yellow')

            



getPoint(root)



root.mainloop()