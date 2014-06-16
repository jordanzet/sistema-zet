import MySQLdb as mdb

coneccion = mdb.connect(user="root", passwd="123456", db="sistemazet")

# creo un cursosr para poder interactuar con la base de datos
cursor = coneccion.cursor()

cursor.execute('CREATE TABLE administrador( id_administrador INT AUTO_INCREMENT,\
											clave_administrador varchar(15),\
											nombre_administrador varchar(30),\
											apellidos_administrador varchar(30),\
											dni_administrador varchar(8),\
											PRIMARY KEY(id_administrador,clave_administrador))')

cursor.execute('CREATE TABLE cajero(id_cajero int AUTO_INCREMENT,\
									clave_cajero varchar(15),\
									cod_tienda int,\
									nombre_cajero varchar(30),\
									apellidos_cajero varchar(30),\
									dni_cajero varchar(8),\
									primary key(id_cajero,clave_cajero))')

cursor.execute('CREATE TABLE cliente(ruc_cliente varchar(15),nombre_cliente varchar(30),telefono_cliente int,primary key(ruc_cliente))')

cursor.execute('CREATE TABLE factura_compra(id_factura_compra int AUTO_INCREMENT,\
											nombre_proveedor varchar(30),\
											id_jefe_inventario int,\
											cod_tienda int,\
											cod_producto int,\
											fecha_compra date,\
											detalle text,\
											importe_neto real,\
											importe_total real,\
											primary key(id_factura_compra))')

cursor.execute('CREATE TABLE factura_venta( id_factura_venta int AUTO_INCREMENT,\
											nombre_tienda varchar(30),\
											nombre_cajero varchar(30),\
											nombre_cliente varchar(30),\
											fecha_venta date,\
											detalle text,\
											importe_total real,\
											primary key(id_factura_venta))')

cursor.execute('CREATE TABLE jefe_inventario(id_jefe_inventario int AUTO_INCREMENT,\
											clave_jefe_inventario varchar(15),\
											cod_tienda int,\
											nombre_jefe_inventario varchar(30),\
											apellidos_jefe_inventario varchar(30),\
											dni_jefe_inventario varchar(8),\
											primary key(id_jefe_inventario,clave_jefe_inventario))')

cursor.execute('CREATE TABLE producto(	cod_producto int,\
										cod_proveedor int,\
										cod_tipo_producto int,\
										cod_area_producto int,\
										descripcion_producto varchar(50),\
										costo_producto real,\
										venta_producto real,\
										stock_producto int,\
										fecha_ingreso date,\
										primary key(cod_producto))')

cursor.execute('CREATE TABLE proveedor(	cod_proveedor int,\
										nombre_proveedor varchar(30),\
										direccion_proveedor varchar(30),\
										telefono_proveedor int,\
										primary key(cod_proveedor))')

cursor.execute('CREATE TABLE tienda(cod_tienda int,nombre_tienda varchar(30),primary key(cod_tienda));')

cursor.execute('CREATE TABLE tipo_producto(	cod_tipo_producto int,nombre_tipo_producto varchar(30),primary key(cod_tipo_producto))')


cursor.execute('INSERT INTO administrador VALUES (NULL, %s, %s, %s,%s)', ('password', 'jordan','medina',73077024 ))
cursor.execute('INSERT INTO cajero VALUES (NULL, %s, %s, %s, %s, %s)', ('password', 1001,'marco','lopez',74856936 ))
cursor.execute('INSERT INTO cliente VALUES (%s, %s, %s)', (987536548345725, 'carlos',963619029 ))
#cursor.execute('INSERT INTO factura_compra VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s)', ('empresa www',1,'T101','P101','26-06-1014','nuevo producto',12,18))
#cursor.execute('INSERT INTO factura_venta VALUES (NULL, %s, %s, %s, %s, %s, %s)', ('tiendita de don pepe', 'jeefrey','juan', '26-06-1014', 'venta 1',14))

#coneccion.commit()
#coneccion.roliback()

#cursor.execute('SELECT * FROM producto')

#cursor.fetchnone()
#cursor.fetchmany(n)

#resultados = cursor.fetchall()
#
#for res in resultados:
#	print res

cursor.close()
coneccion.close()