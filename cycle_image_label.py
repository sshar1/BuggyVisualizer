import tkinter as tk
from PIL import Image, ImageTk

class CycleImageLabel(tk.Label):
    def __init__(self, parent, image_paths, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.image_paths = image_paths
        self.current_image = 0
        self.images = []  # Store all PhotoImage objects
        
        # Pre-load all images
        for path in self.image_paths:
            self.images.append(self.get_icon_from_path(path))
            
        # Set initial image
        self.configure(image=self.images[self.current_image])
        self.bind("<Button-1>", self.cycle_image)

    def cycle_image(self, event=None):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.configure(image=self.images[self.current_image])
    
    def get_icon_from_path(self, path):
        return ImageTk.PhotoImage(Image.open(path).resize((30, 20)))