import tkinter as tk
from tkinter import Tk, Label, Button, PhotoImage
import numpy as np
import csv
import time

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







def getPoint():
    # Path to the CSV file
    csv_file_path = 'Sheet1.csv'

    with open(csv_file_path, mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        header = next(csvreader)  # Read the header row
        #data = [row for row in csvreader]  # Read the remaining data rows
        data = [row for idx, row in enumerate(csvreader) if idx % 5 == 0]  # Read every 10th data row

        for i in range(len(data)):
            row = data[i]
            lat = row['latitude']
            long = row['longitude']

            y = 40.441778 -float(lat)
            x = float(long) + 79.9418917 
            
            y *= 100000
            x *= 100000
            pixelY = abs(y * 2.14)
            pixelX = abs(x * 1.64)
            
            canvas.create_oval(1150 - pixelX, pixelY + 7, 1150 - pixelX - 3, pixelY + 9, fill='yellow', outline='yellow') 
            time.sleep(0.016)
            canvas.update()

            



getPoint()



root.mainloop()