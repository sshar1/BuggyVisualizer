import tkinter as tk
from tkinter import Tk, Label, Button, PhotoImage
import numpy as np
import csv
import time

root = Tk()


canvas = tk.Canvas(root, height=780, width=1235)
canvas.pack()

timer = tk.Text(root, height=1, width=10)
timer.pack()



timer.insert(tk.END, "0:00")


pixels = np.zeros((20000, 2));

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
        data = [row for row in csvreader]  # Read the remaining data rows
        #data = [row for idx, row in enumerate(csvreader) if idx % 2 == 0]  # Read every other data row

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

            pixels[i][0] = 1150 - pixelX
            pixels[i][1] = pixelY + 7


        partPath(1, len(data), False)
        #drawPath(len(data), 1, False)

# draws the full path with inputs for speed and toggle for trail
def drawPath(length, speed, trail):
    timing = 0

    for i in range(length):

        timing += 0.1
        oval = canvas.create_oval(pixels[i][0], pixels[i][1], pixels[i][0] - 3, pixels[i][1] + 2, fill='yellow', outline='yellow')
        canvas.update()

        timer.delete(1.0, tk.END)
        timer.insert(tk.END, str(timing))

        time.sleep(0.1 / speed)
        if not trail:
            canvas.delete(oval)

# def traversePath(length, speed):
#     for i in range(1000):
#         partPath(i/1000.0, length)
#         oval = canvas.create_oval(pixels[i][0], pixels[i][1], pixels[i][0] - 3, pixels[i][1] + 2, fill='yellow', outline='yellow')
#         canvas.update()
#         time.sleep(0.5 / speed)
#         canvas.delete("all")
#         canvas.create_image(0, 0, image=bg_image, anchor="nw")

# pastes a percentage of the path
def partPath(percent, length, trail):
    index = percent * length - 1
    if trail:
        for i in range(int(index)):
            canvas.create_oval(pixels[i][0], pixels[i][1], pixels[i][0] - 3, pixels[i][1] + 2, fill='yellow', outline='yellow')
    # canvas.create_oval(pixels[index][0] + 7, pixels[index][1] - 7, pixels[index][0] - 10, pixels[index][1] + 9, fill='yellow', outline='yellow')
    else:
        canvas.create_oval(pixels[index][0], pixels[index][1], pixels[index][0] - 3, pixels[index][1] + 2, fill='yellow', outline='yellow')
    canvas.update()


getPoint()



root.mainloop()