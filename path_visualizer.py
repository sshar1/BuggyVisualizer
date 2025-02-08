import csv
import numpy as np

class PathVisualizer():
    def __init__(self, canvas, buggy):
        self.buggy = buggy
        self.canvas = canvas
        self.pixels = np.zeros((20000, 2))
        self.current_oval = None
        self.trail_ovals = []
        self.data_loaded = False
        self.path_length = 0
        self.length_update_callback = None
        self.last_point = -1
        
        # Initialize data if CSV path is already set
        if hasattr(self.buggy, 'csv_file_path') and self.buggy.csv_file_path:
            print('buggy has data!')
            self.getPoint()
        else:
            print('buggy has no data!')
    
    def set_length_update_callback(self, callback):
        """Set callback function to be called when path length changes"""
        self.length_update_callback = callback
    
    def get_path_length(self):
        return self.path_length
    
    def getPoint(self):
        if not hasattr(self.buggy, 'csv_file_path') or not self.buggy.csv_file_path:
            print("No CSV file path set")
            return

        print(f"Loading data from {self.buggy.csv_file_path}")
        with open(self.buggy.csv_file_path, mode='r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            header = next(csvreader)
            data = [row for idx, row in enumerate(csvreader) if idx % 2 == 0]

            for i in range(len(data)):
                row = data[i]
                lat = row['latitude']
                long = row['longitude']

                y = 40.441778 - float(lat)
                x = float(long) + 79.948917 
                
                y *= 100000
                x *= 100000
                pixelY = abs(y * 2.14)
                pixelX = abs(x * 1.64)

                self.pixels[i][0] = pixelX
                self.pixels[i][1] = pixelY + 7
            
            old_length = self.path_length
            self.path_length = len(data)
            print(f"Loaded {self.path_length} points")
            self.data_loaded = True
            
            # Notify about length change if callback is set and length actually changed
            if self.length_update_callback and old_length != self.path_length:
                self.length_update_callback(self.path_length)
    
    def update_position(self, current_point):
        if not self.data_loaded and hasattr(self.buggy, 'csv_file_path') and self.buggy.csv_file_path:
            self.getPoint()
            
        if not self.data_loaded:
            return
        
        # Clear previous visualization
        if self.current_oval:
            self.canvas.delete(self.current_oval)
        #for oval in self.trail_ovals:
            #self.canvas.delete(oval)
        #self.trail_ovals.clear()
        
        current_index = min(int(current_point), self.path_length - 1)
        
        # Draw trail up to current position
        #for i in range(current_index + 1):
            #if self.pixels[i][0] == 0 and self.pixels[i][1] == 0:
                #continue
            #oval = self.canvas.create_oval(
                #self.pixels[i][0], self.pixels[i][1], 
                #self.pixels[i][0] - 3, self.pixels[i][1] + 2, 
                #fill=self.buggy.trail_color, outline=self.buggy.trail_color
            #)
            #self.trail_ovals.append(oval)
        
        # Draw trail up to current position
        if self.last_point <= current_index:
            oval = self.canvas.create_oval(
                self.pixels[current_index][0], self.pixels[current_index][1], 
                self.pixels[current_index][0] - 3, self.pixels[current_index][1] + 2,
                fill=self.buggy.trail_color, outline=self.buggy.trail_color
            )
            self.trail_ovals.append(oval)


        
        # Draw current position
        if 0 <= current_index < self.path_length:
            self.current_oval = self.canvas.create_oval(
                self.pixels[current_index][0], self.pixels[current_index][1],
                self.pixels[current_index][0] - 3, self.pixels[current_index][1] + 2,
                fill='yellow', outline='yellow'
            )
        
        self.last_point = current_point