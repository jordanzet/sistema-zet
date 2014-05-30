class Pedido():
	
	def __init__(self, codigo, fecha, cliente, detalle, fechaentrega, listocheck):
		self.codigo = codigo
		self.fecha = fecha
		self.cliente = cliente
 		self.detalle = detalle
		self.fechaentrega = fechaentrega
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
