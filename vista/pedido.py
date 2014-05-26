from Tkinter import *

class PedidoView:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.pedido = Button(frame, text="Pedido", command=self.pedir)
		self.pedido.pack(side=LEFT)
	
	def pedir(self):
		print "Que quiere comprar??"

root = Tk()
vista_producto = PedidoView(root)
root.mainloop()