
class Compra():
	def __init__(self,numero_factura,ruc_proveedor,fecha,detalle,neto,igv,total):
		self.numero_factura = numero_factura
		self.ruc_proveedor = ruc_proveedor
		self.fecha = fecha
		self.detalle = detalle
		self.neto = neto
		self.igv = igv
		self.total = total

	def get_numero_factura(self):
		return self.numero_factura
	def get_ruc_proveedor(self):
		return self.ruc_proveedor
	def get_fecha(self):
		return self.fecha
	def get_detalle(self):
		return self.detalle
	def get_neto(self):
		return self.neto
	def get_igv(self):
		return self.igv
	def get_total(self):
		return self.total

	def set_numero_factura(self,valor):
		self.numero_factura = valor
	def set_ruc_proveedor(self,valor):
		self.ruc_proveedor = valor
	def set_fecha(self,valor):
		self.fecha = valor
	def set_detalle(self,valor):
		self.detalle = valor
	def set_neto(self,valor):
		self.neto = valor
	def set_igv(self,valor):
		self.igv = valor
	def set_total(self,valor):
		self.total = valor

	def	selecCompra()


