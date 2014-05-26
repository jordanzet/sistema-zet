from Tkinter import *

class ProductoView:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.saludo = Button(frame, text="Bienvenido", command=self.saludar)
		self.saludo.pack(side=LEFT)
	
	def saludar(self):
		print "hola todo el mundo!"

root = Tk()
vista_producto = ProductoView(root)
root.mainloop()