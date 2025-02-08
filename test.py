import tkinter as tk
from tkinter import Tk, Label, Button, PhotoImage
import numpy as np
import csv
import time
import asyncio as aio

root = Tk()


canvas = tk.Canvas(root, height=780, width=1235)
canvas.pack()

pause = False

def pause_click():
    global pause
    pause = not pause

timer = tk.Text(root, height=1, width=10)
timer.pack()


timer.insert(tk.END, "0:00")


buggies = np.zeros((3, 20000, 2));

buggy_colors = ['yellow', 'red']


try:
    bg_image = tk.PhotoImage(file="buggy-course1.png")
    # Create the image on the canvas
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
except FileNotFoundError:
    print("Error: Image file not found. Please check the path.")
    # If image not found, set a default background color
    canvas.config(bg="lightblue")

#global index
index = 0

def getPoint():
    # Path to the CSV file
    max_length = 0

    for l in range(2):
        csv_file_path = f'Sheet{l+1}.csv'
        #print(csv_file_path)
    #csv_file_path = 'Sheet2.csv'

        with open(csv_file_path, mode='r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            header = next(csvreader)  # Read the header row
            #data = [row for row in csvreader]  # Read the remaining data rows
            data = [row for idx, row in enumerate(csvreader) if idx % 2 == 0]  # Read every other data row

            if(len(data) > max_length):
                max_length = len(data)

            # Makes a 2D numpy array containing all the values
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

                buggies[l][i][0] = 1150 - pixelX
                buggies[l][i][1] = pixelY + 7

                


        

    partPath(0, 0, len(data), True)
    partPath(1, 0, len(data), True)

    time.sleep(1)
    #resetCanvas()
    drawPath(max_length, 50, True)


def buggyPoint(index):
    for i in range(len(buggies)):
        canvas.create_oval(buggies[i][index][0], buggies[i][index][1], buggies[i][index][0] - 3, buggies[i][index][1] + 2, fill=buggy_colors[i], outline=buggy_colors[i])
        canvas.update()

# draws the full path with inputs for speed and toggle for trail starting at index
def drawPath(length, speed, trail):
    timing = 0

    pause_button = tk.Button(root, text="Pause", command = pause_click)
    pause_button.pack()

    if trail:
        partPath(0, index * 1.0 / length, length, True)
        partPath(1, index * 1.0 / length, length, True)

    for i in range(index, length):  
        ovals = []

        while pause:
            for j in range(2):
                ovals.append(canvas.create_oval(buggies[j][i][0], buggies[j][i][1], buggies[j][i][0] - 3, buggies[j][i][1] + 2, fill=buggy_colors[j], outline=buggy_colors[j]))
                canvas.update()
                canvas.delete(ovals[j])
            #oval = canvas.create_oval(pixels[i][0], pixels[i][1], pixels[i][0] - 3, pixels[i][1] + 2, fill='yellow', outline='yellow')
            #canvas.update()
            #canvas.delete(oval)    

        timing += 0.1

        for j in range(2):
            ovals.append(canvas.create_oval(buggies[j][i][0], buggies[j][i][1], buggies[j][i][0] - 3, buggies[j][i][1] + 2, fill=buggy_colors[j], outline=buggy_colors[j]))
            canvas.update()
            #oval = canvas.create_oval(pixels[i][0], pixels[i][1], pixels[i][0] - 3, pixels[i][1] + 2, fill='yellow', outline='yellow')
        

        timer.delete(1.0, tk.END)
        timer.insert(tk.END, str(timing))

        time.sleep(0.1 / speed)
        if not trail:
            for j in range(len(buggies)):
                canvas.delete(ovals[j])
            #canvas.delete(oval)

# def traversePath(length, speed):
#     for i in range(1000):
#         partPath(i/1000.0, length)
#         oval = canvas.create_oval(pixels[i][0], pixels[i][1], pixels[i][0] - 3, pixels[i][1] + 2, fill='yellow', outline='yellow')
#         canvas.update()
#         time.sleep(0.5 / speed)
#         canvas.delete("all")
#         canvas.create_image(0, 0, image=bg_image, anchor="nw")

# pastes a percentage of the path and changes index
def partPath(buggy, percent, length, trail):
    global index
    index = round(percent * length - 1)
    if trail:
        for i in range(int(index)):
            canvas.create_oval(buggies[buggy][i][0], buggies[buggy][i][1], buggies[buggy][i][0] - 3, buggies[buggy][i][1] + 2, fill=buggy_colors[buggy], outline=buggy_colors[buggy])
    # canvas.create_oval(pixels[index][0] + 7, pixels[index][1] - 7, pixels[index][0] - 10, pixels[index][1] + 9, fill='yellow', outline='yellow')
    else:
        canvas.create_oval(buggies[buggy][index][0], buggies[buggy][index][1], buggies[buggy][index][0] - 3, buggies[buggy][index][1] + 2, fill=buggy_colors[buggy], outline=buggy_colors[buggy])
    canvas.update()

def resetCanvas():
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

getPoint()



root.mainloop()
