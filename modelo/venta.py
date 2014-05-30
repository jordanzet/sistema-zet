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

		