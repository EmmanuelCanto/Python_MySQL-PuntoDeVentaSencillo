import mysql.connector 
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123',
        db='curso',
    )
    
    if conexion.is_connected():
        print('conexion exitosa.')
        infoServer=conexion.get_server_info()
        print('info del servidor', infoServer)
except Error as ex:
    print('Error durante la conexión', ex)
    
finally:
    if conexion.is_connected():
        conexion.close() #se cerró la conexión a la base de datos
        print('la conexión a finalizado')