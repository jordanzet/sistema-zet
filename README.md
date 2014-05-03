sistema-zet
===========

Sistema de Inventariado de la Empresa Zet

ACTORES
=======

Usuario

	Caso de uso:
		Validar Usuario [CU-0001]

	Descripcion: 
		Es una persona detrás de la computadora, ésta todavía no sa ha logeado por lo tanto no podrá ver ni modificar el contenido del sistema.
		Una vez logeado el usuario pasará a tener ciertas funciones y privilegios, dependiendo del tipo de cuenta con el que esté registrado.
	

Administrador

	Caso de uso
	    Gestionar Reportes [CU-0006]
	    Reporte Dinámico [CU-0007]
	    Reporte Estático [CU-0008]
	    Gestionar Productos [CU-0009]
	    Crear Producto [CU-0012]
	    Eliminar Producto [CU-0011]
	    Modificar Producto [CU-0010]
	    Gestionar Usuario [CU-0013]
	    Crear Usuario [CU-0016]
	    Eliminar Usuario [CU-0015]
	    Modificar Usuario [CU-0014]
	    Registrar Datos [CU-0017]
	    Inventario [CU-0018]

	Descripcion 	
		El dueño es un actor mas que nada administrativo. Podrá realizar el alta, baja, modificacion del personal, como tambien de los productos. 
		Para mejorar la administración del sistema podrá consultar las estadisticas del sistema.

Cajero
	Caso de uso
	    Ingresar Pedidos [CU-0002]
	    Ingresar Insumos [CU-0004]
	    Facturar [CU-0003]
	    Actualizar Stock [CU-0005]
	    Registrar Datos [CU-0017]

	Descripcion 	
		El cajero será capaz de registrar los ingresos como también los egresos. 
		Será responsable de la devolución del ticket, que emite el sistema al facturar alguna mesa.
		Estarán en continuo contacto con los mozos, pero hay que aclarar que estos no son considerados como actores ya que sol registran los pedidos de forma manual.
		