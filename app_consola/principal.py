from bd.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print('----MENÚ PRINCIPAL----')
            print('1.- Listar Cursos')
            print('2.- Registrar Cursos')
            print('3.- Actualizar Cursos')
            print('4.- Eliminar Cursos')
            print('5.- Salir Cursos')
            print('----------------------')
            opcion = int(input('Seleccione una opcion: '))

            if opcion < 1 or opcion >5:
                print('opcion intente intente nuevamente')
            elif opcion == 5:
                # -----SALIR DEL SISTEMA------
                continuar= False
                print('¡Gracias por usar este sistema!')
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion(opcion)
        
def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion ==1:
        # ---LISTAR PRODUCTOS----
        try:
            productos=dao.listarProductos()
            if len(productos)>0:
                funciones.listarProductos(productos)
            else:
                print('No se encontraron los cursos')
        except:
                print('Ocurrio un error')
    elif opcion ==2:
        # ----REGISTRAR PRODUCTO-----
        producto = funciones.pedirDatosRegistro()
        try:
            dao.registrarProducto(producto)
        except:
                print('Ocurrio un error')
                
    elif opcion ==3:
        # ----ACTUALIZAR PRODUCTO----
        try:
            productos=dao.listarProductos()
            if len(productos)>0:
                producto = funciones.pedirDatosActualizacion(productos)
                if producto:
                    dao.actualizarProducto(producto)
                else:
                    print('codigo del curso a actualizar no encontrado...\n')
            else:
                print('No se encontraron los cursos')
        except:
            print('Ocurrio un error...')
            
    elif opcion ==4:        
        # -----ELIMINAR PRODUCTO-----
        try:
            productos=dao.listarProductos()
            if len(productos)>0:
                codigoEliminar= funciones.pedirDatosEliminacion(productos)
                if not(codigoEliminar ==""):
                   dao.eliminarProducto(codigoEliminar) 
                else:
                    print('Codigo de curso no encontrado...\n')
            else:
                print('No se encontraron los cursos')
        except:
            print('Ocurrio un error...')
    else:
        print('Opcion no valida')
    
menuPrincipal()