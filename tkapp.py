import tkinter as tk

window = tk.Tk()
window.geometry("500x300")

label = tk.Label(window, text="hello world")
label.pack()

window.mainloop()