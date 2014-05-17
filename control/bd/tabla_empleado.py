#!/usr/bin/python
import MySQLdb
 
# Establecemos la conexión con la base de datos
bd = MySQLdb.connect("localhost","usuarioadmin","prueba123","sistemazet_db" )
 
# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()
 
# Creamos la tabla empleado
sql = "CREATE TABLE EMPLEADO (NOMBRE  CHAR(20) NOT NULL,APELLIDO  CHAR(20),EDAD INT,  SEXO CHAR(1),SALARIO FLOAT )"
 
cursor.execute(sql)
 
# Nos desconectamos de la base de datos 
bd.close()