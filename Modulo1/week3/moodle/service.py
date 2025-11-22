import archivos
"""Logica del proyecto"""
"""Se hace el proyecto modulado como buena practica de programacion"""

def generar_id(inventario):
    """#funcion para generar id, iterando y compara el numero maximo y se le suma 1 para evitar errores de duplicados"""
    if not inventario:
        return 1
    return max(int(i["id"]) for i in inventario) + 1

def agregar_producto(inventario, nombre, precio, cantidad):
    """Aqui se agrega producto, se solicitan los parametros de entrada y se autogeneran id y la operacion del total, se crea un diccionario para anexarla a la lista y se guarda en el archivo"""
    id=generar_id(inventario)
    total=precio * cantidad
    new={
        "id":id,
        "producto":nombre,
        "precio":precio,
        "cantidad":cantidad,
        "total":total
    }
    inventario.append(new)
    archivos.guardar_csv(inventario)
    print(f"Producto agregado con exito ID: {id}")
    
def mostrar_inventario(inventario):
    """Aca va imprimir en el fromato cargado todos los diccionarios de la lista"""
    if not inventario:
        print("Lista vacia")
        return
    print(f"| {'ID':5} | {'Producto':15} | {'Precio':10} | {'Cantidad':10} | {'Total':10} |")
    for i in inventario:
        print(f'| {i['id']:5} | {i['producto']:15} | {i['precio']:10} | {i['cantidad']:10} | {i['total']:10} |')  
                    
def buscar_producto(inventario, id):
    """carga archivo como parametro y aca se itera nuevamente la lista y se filtra por id comparando el input que solicitamos"""
    if not inventario:
        print("Lista vacia")
        return None
    try:
        for i in inventario:
            if int(i['id']) == id: 
                print(f'| {i['id']} | {i['producto']} | {i['precio']} | {i['cantidad']} | {i['total']} |') 
                return i
    except ValueError:
        print("ID invalido")    
        return None   
    print("ID no existe")
    return None
def actualizar_producto(inventario, id, nombre=None, nuevo_precio=None, nueva_cantidad=None):
    """se solicita el id reciclando la funcion buscar , se genera condicional en los parametros a actualizar para que solo se modifiquen si se ingresa algo en el tipado solicitado, sino no no modifica y transforma el valor y guarda."""
    producto=buscar_producto(inventario, id)
    if producto is None:
        print("No existe un producto con ese ID.")
        return
    if nombre is not None and nombre != "":
        producto["producto"] = nombre
        
    if nuevo_precio is not None and nuevo_precio != "":
        try:
            producto["precio"] = float(nuevo_precio)
        except ValueError:
            print("Debe ser un valor numerico")
    if nueva_cantidad is not None and nueva_cantidad != "":
        try:
            producto["cantidad"] = int(nueva_cantidad)
        except ValueError:
            print("Debe ser un valor numerico")    
    producto["total"] = producto["precio"] * producto["cantidad"]
    archivos.guardar_csv(inventario)
    print("Producto actualizado corectamente")
    
def eliminar_producto(inventario, id):
    """recicla buscar id como parametro y elimina el parametro con metodo remove"""
    producto=buscar_producto(inventario, id)
    if not producto:
        print("No existe un producto con ese ID.")
    inventario.remove(producto)   
     
def unidades_totales(inventario):
    """operacion como estadistica del archivo suma todas las cantidades de lista,NOTA: siempre que se carga el archivo csv, el valor operativo se debe transformar de str a int para poder que acepte funciones de operacion"""
    suma = sum(int(i['cantidad']) for i in inventario)
    print(f'Cantidades totales: {suma}')    

def valor_total(inventario):
    """suma los totales de la lista"""
    suma = sum(int(i['total']) for i in inventario)
    print(f'Costo total de todo el inventario: {suma}')
   
def producto_mas_caro(inventario):
    """compara y imprime el valor "precio mas caro"""
    if not inventario:
        print("No hay productos en el inventario.")
        return
    
    mas_caro = max(inventario, key=lambda i: float(i["precio"]))
    print(f"El productomas caro es: {mas_caro['producto']} con un precio de {mas_caro['precio']}")  
    
def producto_mayor_stock(inventario):
    """compara e imprime la cantidad mas cara"""
    if not inventario:
        print("No hay productos en el inventario.")
        return  
    mayor_stock=max(inventario, key=lambda i: int(i['cantidad']))
    
    print(f'El producto con el stock mas alto es: {mayor_stock['producto']} con un stock de: {mayor_stock['cantidad']}')       