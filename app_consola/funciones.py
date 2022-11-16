def listarProductos(productos):
    # METODO PARA LSITAR LOS PRODUCTOS
    print('\nProductos: \n')
    contador=1
    for prod in productos:
        datos='{0}.ID: {1} | Nombre: {2} ({3} pesos)'
        print(datos.format(contador,prod[0], prod[1],prod[2]))
        contador=contador + 1
    print('')
    
# -----------------------------------------------

def pedirDatosRegistro():
    # METODO PARA EL REGISTRO DE UN PRODUCTO
    codigoCorrecto=False
    while(not codigoCorrecto):
        identificador=input('Ingrese código: ')
        if len(identificador)==1:
            codigoCorrecto=True
        else:
            print('codigo incorrecto: sobrepasa los digitos aceptados')
    nombre=input('Ingrese nombre: ')
    precioCorrectos=False
    while(not precioCorrectos):
        precio=input('Ingresese el precio: ')
        if precio.isnumeric():
            if (int(precio)>0):
                precioCorrectos=True
                precio = int(precio)
            else:
                print('los precios deben ser mayor a 0')
        else:
            print('Precios incorrectos: deben ser positivos únicamente')
    producto= (identificador, nombre, precio)
    return producto

# -----------------------------------------------

def pedirDatosActualizacion(productos):
    # METODO PARA ACTUALIZAR LA LISTA DE PRECIOS
    listarProductos(productos)
    existeCodigo=False
    codigoEditar= input('Ingrese el ID del producto a editar: ')
    for prod in productos:
        if prod[0] == codigoEditar:
            existeCodigo=True
            break
        
    if existeCodigo:
        nombre=input('Ingrese nombre a modificar: ')
        precioCorrectos=False
        while(not precioCorrectos):
            precio=input('Ingresese el precio a modificar: ')
            if precio.isnumeric():
                if (int(precio)>0):
                    precioCorrectos=True
                    precio = int(precio)
                else:
                    print('los precios deben ser mayor a 0')
            else:
                print('Precios incorrectos: deben ser positivos únicamente')
        producto= (codigoEditar, nombre, precio)
    else:
        producto=None
        
    return producto

# -----------------------------------------------

def pedirDatosEliminacion(productos):
    # METODO PARA ELIMINAR LOS PRODUCTO
    listarProductos(productos)
    existeCodigo=False
    codigoEliminar= input('Ingrese el ID del producto a eliminar: ')
    for prod in productos:
        if prod[0] == codigoEliminar:
            existeCodigo=True
            break
    if not existeCodigo:
        codigoEliminar=''
    return codigoEliminar
        
