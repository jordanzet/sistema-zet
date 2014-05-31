class Venta():
	def __init__(self,codigo_venta, numero_comprobante, fecha, detalle, total):
		self.codigo_venta = codigo_venta
		self.numero_comprobante = numero_comprobante
		self.fecha = fecha
		self.detalle = detalle
		self.total = total
	
	def get_codigo_venta(self):
		return self.codigo_venta
	def get_numero_comprobante(self):
		return self.numero_comprobante
	def get_fecha(self):
		return self.fecha
	def get_detalle(self):
		return self.detalle
	def get_total(self):
		return self.total

	def set_codigo_venta(self,valor):
		self.codigo_venta = valor
	def set_numero_comprobante(self,valor):
		self.numero_comprobante = valor
	def set_fecha(self,valor):
		self.fecha = valor
	def set_detalle(self,valor):
		self.detalle
	def set_total(self,valor):
		self.total
		
	