import tkinter as tk
from PIL import Image, ImageTk

class CycleImageLabel(tk.Label):
    def __init__(self, parent, image_paths, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.image_paths = image_paths
        self.current_image_index = 0
        self.images = []  # Store all PhotoImage objects
        self.big_images = []
        
        # Pre-load all images
        for path in self.image_paths:
            self.images.append(self.get_icon_from_path(path))
            self.big_images.append(self.get_bigger_icon_from_path(path))
            
        # Set initial image
        self.current__big_image = self.big_images[self.current_image_index]
        self.configure(image=self.images[self.current_image_index])
        self.bind("<Button-1>", self.cycle_image)

    def cycle_image(self, event=None):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.current__big_image = self.big_images[self.current_image_index]
        self.configure(image=self.images[self.current_image_index])
    
    def get_icon_from_path(self, path):
        return ImageTk.PhotoImage(Image.open(path).resize((50, 30)))
    
    def get_bigger_icon_from_path(self, path):
        return ImageTk.PhotoImage(Image.open(path).resize((100, 60)))

    # For path visualizer
    # def get_image(self):
    #     # print(self.image_paths[self.current_image])
    #     return ImageTk.PhotoImage(Image.open(self.image_paths[self.current_image_index]).resize((100, 60)))