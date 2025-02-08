from tkinter import *
from PIL import Image, ImageTk

from buggy_widget import BuggyWidget
from path_visualizer import PathVisualizer
from playback import Playback

root = Tk()
root.geometry('1235x780')

min_w = 0  # Minimum width of the frame
max_w = 250  # Maximum width of the frame
cur_width = min_w  # Increasing width of the frame
expanded = False  # Check if it is completely expanded
frame_visible = False  # Check if the frame is visible

buggy_widgets = []  # List to hold the buggy widgets
path_visualizers = []  # List to hold the path visualizers

MAX_BUGGIES = 6

def toggle_frame():
    global frame_visible, cur_width

    if frame_visible:
        # Contract the frame
        contract()
    else:
        # Expand the frame
        expand()

    frame_visible = not frame_visible  # Toggle the visibility state

def expand():
    global cur_width, expanded
    cur_width += 10  # Increase the width by 10
    rep = root.after(5, expand)  # Repeat this func every 5 ms
    frame.config(width=cur_width)  # Change the width to new increase width
    toggle_button.config(text='>')  # Change the button text to '>'
    if cur_width >= max_w:  # If width is greater than maximum width
        expanded = True  # Frame is expanded
        root.after_cancel(rep)  # Stop repeating the func

def contract():
    global cur_width, expanded
    cur_width -= 10  # Reduce the width by 10
    rep = root.after(5, contract)  # Call this func every 5 ms
    frame.config(width=cur_width)  # Change the width to new reduced width
    toggle_button.config(text='<')  # Change the button text to '<'
    if cur_width <= min_w:  # If it is back to normal width
        expanded = False  # Frame is not expanded
        root.after_cancel(rep)  # Stop repeating the func

def add_buggy():
    if len(buggy_widgets) >= MAX_BUGGIES: return

    buggy_widget = BuggyWidget(frame, 'New Buggy', buggy_widgets, buggy_add_button)
    buggy_widgets.append(buggy_widget)

    path_visualizer = PathVisualizer(course_canvas, buggy_widget)
    buggy_widget.path_visualizer = path_visualizer
    path_visualizers.append(path_visualizer)
    playback_bar.add_visualizer(path_visualizer)
    
    # Correctly position each widget
    for idx, widget in enumerate(buggy_widgets):
        widget.grid(row=idx, column=0, pady=10)
    
    # Move add button to the correct row
    buggy_add_button.grid(row=len(buggy_widgets), column=0, sticky='sew')

root.update()

# Create a main frame to hold everything
main_frame = Frame(root)
main_frame.pack(fill='both', expand=True)

course_canvas = Canvas(main_frame, height=780, width=1235)
course_canvas.grid(row=0, column=0, sticky='nsew')
bg_image = PhotoImage(file="imgs/buggy-course2.png")
# Create the image on the canvas
course_canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Create a frame for the expanding sidebar
frame = Frame(main_frame, bg='#282828', width=min_w, height=root.winfo_height(), padx=0)
frame.grid(row=0, column=1, sticky='nse')
frame.grid_columnconfigure(0, weight=1)

playback_bar = Playback(main_frame, path_visualizers)
playback_bar.grid(row=1, column=0, columnspan=2, sticky='ew')

# Bind to the frame, if entered or left
toggle_button = Button(
    main_frame, text="<", command=toggle_frame,
    bg='#282828', fg="#282828",  # Ensure text is visible
    relief='flat', width=2, height=2,
    activebackground='#282828',  # Prevents color change on click
    highlightbackground='#282828',  # Ensures consistent color
)
toggle_button.grid(row=0, column=0, sticky='ne')

buggy_add_button = Button(frame, text="+", bg='#282828', relief='flat', width=2, height=2, command=add_buggy)
buggy_add_button.grid(row=len(buggy_widgets), column=0, sticky='sew')

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)

# Configure the grid to allow the frame to stick to the right
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=0)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=0, minsize=50)

root.mainloop()