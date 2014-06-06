create table area_producto(
cod_area_producto int,
nombre_area_producto varchar(30),
primary key(cod_area_producto))


create table area_producto(
cod_area_producto int,
nombre_area_producto varchar(30),
primary key(cod_area_producto))


create table cajero(
id_cajero int,
clave_cajero varchar(15),
cod_tienda int,
nombre_cajero varchar(30),
apellidos_cajero varchar(30),
dni_cajero varchar(8),
primary key(id_cajero,clave_cajero))


create table cliente(
ruc_cliente varchar(15),
nombre_cliente varchar(30),
telefono_cliente int,
primary key(ruc_cliente))

create table factura_compra(
factura_compra int,
nombre_proveedor varchar(30),
id_jefe_inventario int,
cod_tienda int,
cod_producto int,
fecha_compra date,
detalle text,
importe_neto real,
importe_total real,
primary key(factura_compra))


create table factura_venta(
factura_venta int,
nombre_tienda varchar(30),
nombre_cajero varchar(30),
nombre_cliente varchar(30),
fecha_venta date,
detalle text,
importe_total real,
primary key(factura_venta))


create table jefe_inventario(
id_jefe_inventario int,
clave_jefe_inventario varchar(15),
cod_tienda int,
nombre_jefe_inventario varchar(30),
apellidos_jefe_inventario varchar(30),
dni_jefe_inventario varchar(8),
primary key(id_jefe_inventario,clave_jefe_inventario))

create table producto(
cod_producto int,
cod_proveedor int,
cod_tipo_producto int,
cod_area_producto int,
descripcion_producto varchar(50),
costo_producto real,
venta_producto real,
stock_producto int,
fecha_ingreso date,
primary key(cod_producto))

create table proveedor(
cod_proveedor int,
nombre_proveedor varchar(30),
direccion_proveedor varchar(30),
telefono_proveedor int,
primary key(cod_proveedor))

create table tipo_producto(
cod_tipo_producto int,
nombre_tipo_producto varchar(30),
primary key(cod_tipo_producto))