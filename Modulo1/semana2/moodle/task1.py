"""1. Validación de datos con condicionales:
Crea un menú que pregunte al usuario qué acción desea realizar:
Agregar producto
Mostrar inventario
Calcular estadísticas
Salir
Usa condicionales if, elif y else para procesar la opción elegida.
Si el usuario ingresa una opción inválida, muestra un mensaje de error y pide nuevamente la entrada."""

def menu():
    while True:
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        
        try:
            ingresa=int(input("Ingresa una de las opciones: "))
            
        except ValueError:
            print("La opcion debe ser un numero")
            continue
        if ingresa == 1:
            
        
            producto=input("ingrese Producto: ")
            try:    
                cantidad=int(input("Ingrese las cantidades: "))   
                precio=int(input("Ingrese el precio: "))
                
            except ValueError:
                print("La opcion debe ser un numero") 
                continue 
            agregar(producto,cantidad, precio)
                           
        elif ingresa == 2:
                mostrar_lista()
        elif ingresa == 3:
            estadisticas()
        elif ingresa == 4:
            print("Gracias por ingresar!!")
            break
lista=[]
def agregar(producto, cantidad, precio) :
    total=cantidad*precio 

    lista.append({
                    "producto": producto,
                    "cantidad": cantidad,
                    "precio": precio,
                    "total": total
                })
    print("Lista Creada con exito.") 
   
            
    
def mostrar_lista():
    if not lista:
        print("Lista vacia!!")
    else:   
        print("\n------INVENTARIO-PRODUCTOS------")
        for i,item in enumerate(lista):
            print(f"{i}. Producto: {item['producto']} | Cantidad: {item['cantidad']} | Precio: ${item['precio']:.0f} | Total: {item['total']:.0f}")
        print("---------------------------------\n")  
            

def estadisticas():
    if not lista:
        print("No se pueden obtener datos, esta vacia")
    else:
        suma_cantidades=0
        suma_total=0
        inventario_producto=len(lista)
        precio_max=0 
        for p in lista:
            suma_cantidades += p['cantidad']
            suma_total += p['total']
            if p['precio']>precio_max:
                precio_max = p['precio']
        print(f'\nCantidad de productos en el inventario: {inventario_producto}\nCAntidad de productos totales: {suma_cantidades}\nMaximo precio: {precio_max}\nEl valor de tu inventario es: {suma_total}\n')
    
                       
    
    
if __name__=="__main__":
    menu()               