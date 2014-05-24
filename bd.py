import MySQLdb as mdb

coneccion = mdb.connect(user="root", passwd="jordanzet", db="sistemazet")

cursor = coneccion.cursor()

try:
	cursor.execute('CREATE TABLE productos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(45), descripcion TEXT, precio INT )')
except :
	pass   



cursor.execute('INSERT INTO productos VALUES (NULL,%s, %s, %s, %s)', ('ariel', 'lejia',3))
coneccion.commit()
#coneccion.roliback()


cursor.execute('SELECT * FROM productos')


#cursor.fetchnone()
#cursor.fetchmany(n)

resultados = cursor.fetchall()

for res in resultados:
	print res

cursor.close()
coneccion.close()



