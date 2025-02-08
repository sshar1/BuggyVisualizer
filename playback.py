from tkinter import *
from tkinter import ttk

class Playback(Frame):
    def __init__(self, parent, path_visualizers=None):
        Frame.__init__(self, parent, bg="#282828", bd=2, relief="groove")
        self.path_visualizers = path_visualizers or []
        self.max_length = 0
        
        # Set a fixed height for the playback bar
        self.configure(height=50)
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        
        # Create the scrollbar/timeline
        self.timeline = ttk.Scale(
            self,
            from_=0,
            to=100,
            orient='horizontal',
            command=self.on_scroll
        )
        self.timeline.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        
        # Create a frame for control buttons
        self.controls_frame = Frame(self, bg="white")
        self.controls_frame.grid(row=0, column=0, pady=(0, 5))
        
        # Add play/pause button
        self.play_button = Button(
            self.controls_frame,
            text="▶",
            command=self.toggle_play,
            bg='#282828',
            fg='#282828',
            relief='flat'
        )
        self.play_button.pack(side=LEFT, padx=5)
        
        # Add time label
        self.time_label = Label(
            self.controls_frame,
            text="0:00 / 0:00",
            bg='#282828',
            fg='white'
        )
        self.time_label.pack(side=LEFT, padx=5)
        
        self.playing = False
        self.current_value = 0
        self.after_id = None
        self.total_time = "0:00"

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
    
    def toggle_play(self):
        self.playing = not self.playing
        self.play_button.config(text="⏸" if self.playing else "▶")

        if self.playing:
            self.update_playback()
        else:
            if self.after_id:
                self.after_cancel(self.after_id)
                self.after_id = None
    
    def update_playback(self):
        if not self.playing:
            return
            
        self.current_value = float(self.timeline.get())
        if self.current_value >= 100:
            self.current_value = 0
            self.playing = False
            self.play_button.config(text="▶")
        else:
            self.current_value += 0.1
            
        self.timeline.set(self.current_value)
        self.on_scroll(str(self.current_value))
        self.after_id = self.after(50, self.update_playback)
    
    def on_scroll(self, value):
        percentage = float(value) / 100.0
        current_points = percentage * self.max_length
        print(f"Scrolling to {percentage:.2f}, points: {current_points:.1f}, max_length: {self.max_length}")
        
        current_time = int(percentage * self.max_length / 10)
        minutes = current_time // 60
        seconds = current_time % 60
        self.time_label.config(text=f"{minutes}:{seconds:02d} / {self.total_time}")
        
        for visualizer in self.path_visualizers:
            if hasattr(visualizer, 'data_loaded') and visualizer.data_loaded:
                visualizer.update_position(current_points)
    
    def add_visualizer(self, path_visualizer):
        self.path_visualizers.append(path_visualizer)
        path_visualizer.set_length_update_callback(self.update_max_length)

    def update_max_length(self, new_length):
        self.max_length = max(self.max_length, new_length)
        if self.max_length > 0:
            total_seconds = int((self.max_length / 10))
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            self.total_time = f"{minutes}:{seconds:02d}"
        else:
            self.total_time = "0:00"