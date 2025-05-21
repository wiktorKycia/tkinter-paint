import tkinter as tk
from tkinter import ttk


class Canvas(tk.Canvas):
    def __init__(self, parent, controller):
        tk.Canvas.__init__(self, parent)


class ShapeMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        circles_button = tk.Button(
            self,
            text="Circles",
            command=controller.draw_circles
        )
        
        rectangles_button = tk.Button(
            self,
            text="Rectangles",
            command=controller.draw_rectangles
        )

        
class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Drawing Application")
        self.geometry("600x500")
        
        shape_menu = ShapeMenu(self, self)
        shape_menu.pack(side="top")
        
    def draw_circles():
        pass
    
    def draw_rectangles():
        pass

if __name__ == "__main__":
    testObj = Window()
    testObj.mainloop()