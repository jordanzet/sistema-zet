class Producto():

	def __init__(self, codigo,nombre, precio, stock, tipo, vencimiento):
		self.codigo = codigo
		self.nombre = nombre
		self.precio = precio 
		self.stock = stock
		self.tipo = tipo 
		self.vencimiento = vencimiento
	
	def validar_nombre(self):pass
	def mod_stock():pass
	def get_codigo(self):return self.codigo
	def get_nombre(self):return self.nombre
	def get_vencimiento(self):return self.vencimiento
	def get_precio(self):return self.precio
	def get_stock(self):return self.stock

	def set_codigo(self,valor):
		self.codigo = valor

	def set_nombre(self,valor):
		self.nombre = valor

	def set_precio(self,valor):
		self.precio = valor

	def set_stock(self,valor):
		self.stock = valor

	def set_tipo(self,valor):
		self.tipo = valor
		
	def set_vencimiento(self,valor):
		self.vencimiento = valor

	def producto(codigo):pass
	def listarProductos(tipo):pass
	def stockcigarrillos(tipostock):pass
	def stocktarjetas():pass
	def informecelcarga():pass

