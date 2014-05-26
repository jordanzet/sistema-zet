import MySQLdb
 
DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = 'mysqlroot' 
DB_NAME = 'a' 
 
def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
 
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 
 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
 
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 
 
    return data

#12.2.1.1. Insertar datos

dato = raw_input("Dato: ")
query = "INSERT INTO b (b2) VALUES ('%s')" % dato
run_query(query)

#12.2.1.2. Seleccionar todos los registros
query = "SELECT b1, b2 FROM b ORDER BY b2 DESC" 
result = run_query(query) 
print result

#12.2.1.3. Seleccionar solo registros coincidentes
criterio = raw_input("Ingrese criterio de búsqueda: ") 
query = "SELECT b1, b2 FROM b WHERE b2 = '%s'" % criterio 
result = run_query(query)
print result

#12.2.1.4. Eliminar registros
criterio = raw_input("Ingrese criterio p7 eliminar coincidencias: ") 
query = "DELETE FROM b WHERE b2 = '%s'" % criterio 
run_query(query)

#12.2.1.5. Actualizar datos
b1 = raw_input("ID: ") 
b2 = raw_input("Nuevo valor: ") 
query = "UPDATE b SET b2='%s' WHERE b1 = %i" % (b2, int(b1)) 
run_query(query)


