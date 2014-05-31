
class Proveedor:

	def __init__(self,codigo_proveedor, nombre_proveedor, direccion, telefono, departamento, provincia, distrito ):
		self.codigo_proveedor = codigo_proveedor		
		self.nombre_proveedor = nombre_proveedor
		self.direccion = direccion
		self.telefono = telefono
		self.departamento = departamento
		self.provincia = provincia
		self.distrito = distrito
		
	def get_codigo_proveedor(self):
		return self.codigo_proveedor
	def get_nombre_proveedor(self):
		return self.nombre_proveedor
	def get_direccion(self):
		return self.direccion
	def get_telefono(self):
		return self.telefono
	def get_departamento(self):
		return self.departamento
	def get_provincia():
		return self.provincia
	def get_distrito():
		return self.distrito


	def set_codigo_proveedor(self,valor):
		self.codigo_proveedor = valor
	def set_nombre_proveedor(self,valor):
		self.nombre_proveedor
	def set_direccion(self,valor):
		self.direccion = valor
	def set_telefono(self,valor):
		self.telefono = valor
	def set_departamento(self,valor):
		self.departamento = valor
	def set_provincia(self,valor):
		self.provincia = valor
	def set_distrito(self,valor):
		self.distrito = valor


