#!/usr/bin/python
 
import MySQLdb
 
# Establecemos la conexión con la base de datos
bd = MySQLdb.connect("localhost","usuarioadmin","prueba123","sistemazet_db" )
# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()
 
# Ejecutamos un query SQL usando el método execute() que nos proporciona el cursor
cursor.execute("SELECT VERSION()")
 
# Extraemos una sola fila usando el método fetchone()
data = cursor.fetchone()
 
print "Versión Base de Datos : %s " % data
 
# Nos desconectamos de la base de datos
bd.close()
