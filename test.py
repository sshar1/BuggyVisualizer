import tkinter as tk
from tkinter import Tk, Label, Button, PhotoImage

root = Tk()
root.title("Buggy Visualizer")
root.geometry("1235x780") 

background_image = PhotoImage(file="buggy-course1.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()
