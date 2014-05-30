
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

