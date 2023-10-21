import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

class MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Map")

        # Load the map image
        self.map_image = Image.open("..\map.jpg")
        self.map_width, self.map_height = self.map_image.size

        # Create a canvas to display the map
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Create an initial zoom level
        self.zoom_level = 1

        # Display the initial map
        self.show_map()

        self.panning = False
        self.last_x = 0
        self.last_y = 0

    def add_marker(self, x, y, id,color):
        # 将红点坐标调整到地图的缩放和平移中
        self.canvas.coords('marker_%s' % id, x - 5, y - 5, x + 5, y + 5)
        self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color, tag='marker_%s' % id)

    def show_marker_id(self, id):
        tk.messagebox.showinfo(title='Marker %s' % id, message='Marker ID: %s' % id)

    def show_map(self):
        # Resize the map image based on the current zoom level
        new_width = int(self.map_width * self.zoom_level)
        new_height = int(self.map_height * self.zoom_level)
        resized_image = self.map_image.resize((new_width, new_height))
        self.photo = ImageTk.PhotoImage(resized_image)

        # Clear the canvas and display the resized map
        self.canvas.delete("all")
        self.map_item = self.canvas.create_image(0, 0, image=self.photo, anchor="nw")

        # Bind mouse drag events for map panning
        self.canvas.bind("<ButtonPress-1>", self.on_map_click)
        self.canvas.bind("<B1-Motion>", self.on_map_drag)


        for i in range(10):
            x = random.randint(0, new_width)
            y = random.randint(0, new_height)
            self.add_marker(x, y, i,'red')

        # 为每个小红点绑定点击事件
        for i in range(10):
            self.canvas.tag_bind('marker_%s' % i, '<ButtonPress-1>',
                                 lambda evt, id=i: self.show_marker_id(id))

    def on_map_click(self, event):
        self.panning = True
        self.last_x = event.x
        self.last_y = event.y

    def on_map_drag(self, event):
        if self.panning:
            dx = event.x - self.last_x
            dy = event.y - self.last_y
            self.last_x = event.x
            self.last_y = event.y

            # Calculate the current map position
            current_x, current_y = self.canvas.coords(self.map_item)
            new_x = current_x + dx
            new_y = current_y + dy

            # Calculate the boundaries
            min_x = 800 - self.map_width
            min_y = 600 - self.map_height

            # Ensure the new position is within bounds
            new_x = max(min_x, min(0, new_x))
            new_y = max(min_y, min(0, new_y))

            self.canvas.move(self.map_item, new_x - current_x, new_y - current_y)

            # Update marker positions
            for i in range(10):
                x1, y1, x2, y2 = self.canvas.coords('marker_%s' % i)
                self.canvas.coords('marker_%s' % i, x1 + new_x - current_x, y1 + new_y - current_y,
                                   x2 + new_x - current_x, y2 + new_y - current_y)

if __name__ == "__main__":
    root = tk.Tk()
    app = MapApp(root)
    root.mainloop()
