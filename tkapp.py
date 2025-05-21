import tkinter as tk

class HelloWorld:
  def __init__(self):
    self.window = tk.Tk() # tworzenie okna głównego
    self.window.title( "Hello World" ) # ustawienie tytułu okna głównego
    # tworzenie kontrolki typu label
    self.label = tk.Label( self.window, text = "Witaj Świecie programowania\nCo swym urokiem nas zabawia\nCo otwiera nowe możliwości\nZ binarnych liczb złożoności" )
    self.label.pack( side = tk.BOTTOM ) # podpinanie kontrolki pod okno
    self.window.mainloop() # wywołanie pętli komunikatów
    
helloworld = HelloWorld()