import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='123',
                db='curso'
            )
        except Error as ex:
            print('Error al intentar la conexción: {0}'.format(ex))
            
    def listarProductos(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM productos ORDER BY nombre ASC")
                resultados=cursor.fetchall()
                return resultados
                
            except Error as ex:
                print('Error al itnentar la conexción: {0}'.format(ex))
        

    def registrarProducto(self, producto):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="INSERT INTO productos (ID, nombre, precio) VALUES('{0}','{1}','{2}')"
                cursor.execute(sql.format(producto[0],producto[1], producto[2]))
                self.conexion.commit()
                print('Producto registrado!')
            except Error as ex:
                print('Error al itnentar la conexción: {0}'.format(ex))

    def actualizarProducto(self, producto):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="UPDATE productos SET nombre = '{0}', precio = '{1}' WHERE id = '{2}'"
                cursor.execute(sql.format(producto[1],producto[2], producto[0]))
                self.conexion.commit()
                print('Producto actualizado!')
            except Error as ex:
                print('Error al itnentar la conexción: {0}'.format(ex))

    def eliminarProducto(self, codigoProductoEliminar):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="DELETE FROM productos WHERE id = '{0}'"
                cursor.execute(sql.format(codigoProductoEliminar))
                self.conexion.commit()
                print('Producto Eliminado!')
            except Error as ex:
                print('Error al itnentar la conexción: {0}'.format(ex))
                
    
        