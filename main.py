import tkinter as tk
from tkinter import ttk


class Canvas(tk.Canvas):
    def __init__(self, parent, controller):
        tk.Canvas.__init__(self, parent, width=600, height=400)
        self.create_rectangle((0, 0, 600, 400), fill="#ffffff", width = 0)
    
    def draw_circles(self, event):
        self.create_oval((event.x - 2), (event.y - 2), (event.x + 2), (event.y + 2))
    
    def draw_rectangles(self, event):
        self.create_rectangle((event.x - 2), (event.y - 2), (event.x + 2), (event.y + 2))


class ShapeMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=600, height=100)
        
        circles_button = tk.Button(
            self,
            text="Circles",
            command=controller.draw_circles
        )
        circles_button.pack()
        
        rectangles_button = tk.Button(
            self,
            text="Rectangles",
            command=controller.draw_rectangles
        )
        rectangles_button.pack()

        
class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Drawing Application")
        self.geometry("600x500")
        
        self.shape_menu = ShapeMenu(self, self)
        self.shape_menu.pack(side="top")
        
        self.canvas = Canvas(self, self)
        
    def draw_circles(self):
        self.canvas.bind("<B1-Motion>", self.canvas.draw_circles)
    
    def draw_rectangles(self):
        self.canvas.bind("<B1-Motion>", self.canvas.draw_rectangles)

if __name__ == "__main__":
    testObj = Window()
    testObj.mainloop()