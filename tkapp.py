import tkinter as tk

class HelloWorld:
	def __init__(self):
		self.window = tk.Tk() # tworzenie okna głównego
		self.window.title( "Hello World" ) # ustawienie tytułu okna głównego
		# tworzenie kontrolki typu label
		self.label = tk.Label( self.window, text = "Witaj Świecie programowania\nCo swym urokiem nas zabawia\nCo otwiera nowe możliwości\nZ binarnych liczb złożoności" )
		self.label.pack( side = tk.BOTTOM ) # podpinanie kontrolki pod okno
		self.window.mainloop() # wywołanie pętli komunikatów

class CanvasDrawing:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Rysowanie")
		self.window.geometry("500x500")

		self.canvas = tk.Canvas(self.window, width = 450, height = 450) # tworzę kontrolkę typu Canvas
		self.canvas.place( x= 25, y = 25) # umieszczam ją na ekranie

		self.canvas.create_rectangle((0, 0, 450, 450), fill="#ffffff", width = 0) # rysuję biały prostokąt
		self.canvas.bind("<B1-Motion>", self.draw) # podpinam zdarzenie pod kontrolkę

		self.window.mainloop()
    
	def draw(self, event): # metoda, którą podepnę pod zdarzenie ruchu myszki nad kontrolką canvas z wciśniętym lewym przyciskiem myszy
		self.canvas.create_oval((event.x - 2), (event.y - 2), (event.x + 2), (event.y + 2)) # tworzę okrąg na kontrolce canvas przy każdym ruchu myszką


# helloworld = HelloWorld()
can = CanvasDrawing()