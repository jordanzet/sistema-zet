class Pedido():
	
	def __init__(self, codigo, fecha, cliente, detalle, fecha_entrega, listocheck):
		self.codigo = codigo
		self.fecha = fecha
		self.cliente = cliente
 		self.detalle = detalle
		self.fecha_entrega = fecha_entrega
		self.total = total
		self.listocheck = listocheck

	def get_codigo(self):
		return self.codigo
	def get_fecha(self):
		return self.fecha
	def get_cliente(self):
		return self.cliente
	def get_detalle(self):
		return self.detalle
	def get_fechaentrega(self):
		return self.fechaentrega
	def get_total(self):
		return self.total
	def get_listocheck(self):
		return self.listocheck

	def set_codigo(self,valor):
		self.codigo = valor
	def set_fecha(self,valor):
		self.fecha = valor
	def set_cliente(self,valor):
		self.cliente = valor
	def set_detalle(self,valor):
		self.detalle = valor
	def set_fechaentrega(self,valor):
		self.fechaentrega
	def set_total(self,valor):
		self.total = valor
	def set_listocheck(self,valor):
		self.listocheck = valor


	def seleccionar_pedido():pass
	def listar_pedidos():pass
	def procesar_pedido():pass
	def terminar_pedido ():pass
	def total_pedido():pass
	def cambiar_estado():pass
	def ver_pedido():pass
	def	mostrar_pedidos_pendientes():pass
	def generar_venta():pass
	def realizar_pedido():pass
	def ver_producto():pass
	def seleccionar_producto():pass
	def generar_pedido():pass
