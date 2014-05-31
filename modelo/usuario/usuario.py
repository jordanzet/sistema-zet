
class Usuario:
	#categoria = puesto del empleado
	def __init__(self,id,nombre,apellidos,dni,categoria,clave):
		self.id = id
		self.nombre = nombre
		self.apellidos = apellidos
		self.dni = dni
		self.categoria = categoria
		self.clave = clave

	def get_id(self):
		return self.id
	def get_nombre(self):
		return self.nombre
	def get_apellidos(self):
		return self.apellidos
	def get_dni(self):
		return self.dni
	def get_categoria(self):
		return self.categoria
	def get_clave(self):
		return self.clave

	def set_id(self,valor):
		self.id = valor
	def set_nombre(self,valor):
		self.nombre = valor
	def set_apellidos(self,valor):
		self.apellidos = valor
	def set_dni(self,valor):
		self.dni = valor
	def set_categoria(self,valor):
		self.categoria
	def set_clave(self,valor):
		self.clave = valor



	def forma_de_pago():
		pass

	def despedir_empleado():
		pass


def hola():
	pass