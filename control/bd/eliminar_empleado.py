#!/usr/bin/python
 
import MySQLdb
 
# Establecemos la conexión con la base de datos
bd = MySQLdb.connect("localhost","usuarioadmin","prueba123","sistemazet_db" )
 
# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()
 
# Preparamos el query SQL para eliminar al empleado 
sql = "DELETE FROM EMPLEADO WHERE APELLIDO=‘Picca’"
try:
   # Ejecutamos el comando
   cursor.execute(sql)
   # Efectuamos los cambios en la base de datos
   bd.commit()
except:
   # Si se genero algún error revertamos la operación
   bd.rollback()
 
# Nos desconectamos de la base de datos 
bd.close()