from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

from cycle_image_label import CycleImageLabel
from editable_label import EditableLabel

class BuggyWidget(Frame):

    COLORS = ['red', '#1ad80a', '#14efee', 'yellow', '#961cfb', '#fb1cdd']
    BUGGY_IMAGES = ['imgs/buggy1.png', 'imgs/buggy2.png', 'imgs/buggy3.png', 'imgs/buggy4.png', 'imgs/buggy5.png', 'imgs/buggy6.png']
    MAX_FILENAME_LENGTH = 25

    def __init__(self, parent, label, buggy_widgets, add_button):
        Frame.__init__(self, parent, bg="#282828", bd=2, relief="groove")

        self.buggy_widgets = buggy_widgets # Store reference to buggy widgets list
        self.add_button = add_button  # Store reference to add button
        self.trail_color = self.COLORS[len(buggy_widgets)]

        # Load the icon (replace 'icon.png' with your icon file)
        self.icon = ImageTk.PhotoImage(Image.open("imgs/buggy1.png").resize((80, 60)))

        # Create a label for the icon
        self.icon_label = CycleImageLabel(self, self.BUGGY_IMAGES, image=self.icon, bg="#282828")
        self.icon_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Create a label for the title
        self.title_label = EditableLabel(self, text=label, bg="#282828", anchor="w", fg="white")
        self.title_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Create an "x" button to delete the widget
        self.delete_button = Button(self, text="x", bg="#282828", fg="red", relief="flat", command=self.destroy)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self.file_upload = Button(self, text='Upload CSV', command=self.UploadAction)
        self.file_upload.grid(row=1, column=0, columnspan=3, sticky="sew")
        self.csv_file_path = None

        self.div = Frame(self, height=10)
        self.div.grid(row=2, column=0, columnspan=3, sticky="sew")

        self.trail_color_frame = Frame(self, bg=self.trail_color, height=5)
        self.trail_color_frame.grid(row=3, column=0, columnspan=3, sticky="sew")

        # Configure grid weights to make the entry expand
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
    
    def UploadAction(self, event=None):
        filename = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("CSV files", "*.csv")]  # Only allow CSV files
        )
        
        # Valid file selected
        if filename != '':
            fn = self.get_filename(filename)
            # self.csv_file_path = filename
            self.set_csv_file(filename)
            if len(fn) > self.MAX_FILENAME_LENGTH:
                self.file_upload.config(text=fn[0:self.MAX_FILENAME_LENGTH] + '...' + fn[-self.MAX_FILENAME_LENGTH:])
            else:
                self.file_upload.config(text=fn)
    
    def destroy(self):
        if self.winfo_exists() and self.master.winfo_exists():
            if self in self.buggy_widgets:
                self.buggy_widgets.remove(self)  # Remove from list
                self.update_positions()  # Update widget positions

        super().destroy()

    def update_positions(self):
        """Rearrange widgets and move add button below the last widget"""
        for idx, widget in enumerate(self.buggy_widgets):
            widget.grid(row=idx, column=0, pady=10)
            widget.trail_color = self.COLORS[idx]
            widget.trail_color_frame.config(bg=widget.trail_color)

        # Move the add button to the correct position
        self.add_button.grid(row=len(self.buggy_widgets), column=0, sticky='sew')

    def get_filename(self, path):
        return path.split('/')[-1]

    def set_csv_file(self, file_path):
        self.csv_file_path = file_path
        if hasattr(self, 'path_visualizer'):
            self.path_visualizer.getPoint()
    
    def get_icon(self):
        return self.icon_label.current__big_image

