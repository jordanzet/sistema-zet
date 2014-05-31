
class Tienda: #tiendas en varios distritos

	def __init__(self, ubicacion, codigo_de_tienda,nombre):
	self.ubicacion = ubicacion
	self.codigo_de_tienda = codigo_de_tienda
	self.nombre = nombre
	
	def get_ubicacion(self):
		return self.ubicacion
	def get_codigo_de_tienda(self):
		return self.codigo_de_tienda
	def get_nombre(self):
		return self.nombre

	def set_ubicacion(self,valor):
		self.ubicacion = valor
	def set_codigo_de_tienda(self,valor):
		self.codigo_de_tienda = valor
	def set_nombre(self,valor):
		self.nombre = valor