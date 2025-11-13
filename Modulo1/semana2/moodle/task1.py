"""1. Validación de datos con condicionales:
Crea un menú que pregunte al usuario qué acción desea realizar:
Agregar producto
Mostrar inventario
Calcular estadísticas
Salir
Usa condicionales if, elif y else para procesar la opción elegida.
Si el usuario ingresa una opción inválida, muestra un mensaje de error y pide nuevamente la entrada."""

def menu():#este es el menu de entrada.
    while True:
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")#opciones ninguna tiene funcion
        
        try:#el try se utiliza para generar validacion de tipos de errores
            ingresa=int(input("Ingresa una de las opciones: "))#variable de entrada de menu
            
        except ValueError:#valuerror se utiliza para capturar errores de entrada en un input
            print("La opcion debe ser un numero")
            continue#con el continue evitamos que se rompa el codigo con el error
        if ingresa == 1:#condicionales de el menu comparando numero de opcion
            producto=input("ingrese Producto: ")
            try: #validacion tipo de dato
                cantidad=int(input("Ingrese las cantidades: "))   
                precio=int(input("Ingrese el precio: "))
                
            except ValueError:
                print("La opcion debe ser un numero") 
                continue 
            agregar(producto,cantidad, precio)#se envia la funcion con los parametros asignados
                           
        elif ingresa == 2:
                mostrar_lista()
        elif ingresa == 3:
            estadisticas()
        elif ingresa == 4:
            print("Gracias por ingresar!!")
            break#aqui cierra el programa
lista=[]#lista vacia
def agregar(producto, cantidad, precio):#parametro que se solicitan
    total=cantidad*precio 

    lista.append({
                    "producto": producto,
                    "cantidad": cantidad,
                    "precio": precio,
                    "total": total
                })#se crea un diccionario para agregarlo como item de la lista vacia
    print("Lista Creada con exito.") 
   
            
    
def mostrar_lista():
    if not lista:#validacion de que no este vacia
        print("Lista vacia!!")
    else:   
        print("\n------INVENTARIO-PRODUCTOS------")
        for i,item in enumerate(lista):#se recorre la lista con la funcion enumerate, para tomar numeracion del item y los valores segun la llave del diccionario.
            i+=1
            print(f"{i}. Producto: {item['producto']} | Cantidad: {item['cantidad']} | Precio: ${item['precio']:.0f} | Total: {item['total']:.0f}")#los valores del diccionario se llaman por medio de la llave
        print("---------------------------------\n")  
            

def estadisticas():
    if not lista:#validacion de la lista
        print("No se pueden obtener datos, esta vacia")
    else:
        suma_cantidades=0#variables en cero para guardar valores en este caso sumar cantidades
        suma_total=0
        inventario_producto=len(lista)#len para tomar la cantidad de elementos de la lista
        precio_max=0 
        for p in lista:#for para recorrer la lista
            suma_cantidades += p['cantidad']#+= suma y guarda en la variable, y toma el item del diccionario de la lista que va a operar
            suma_total += p['total']
            if p['precio']>precio_max:
                precio_max = p['precio']#esta variable guarda el precio mas alto calculando el actual con el guardado.
        print(f'\nCantidad de productos en el inventario: {inventario_producto}\nCAntidad de productos totales: {suma_cantidades}\nMaximo precio: {precio_max}\nEl valor de tu inventario es: {suma_total}\n')#informacion de devuelve la funcion
    
                       
    
    
if __name__=="__main__":#funcion ejecutable de ejercicio
    menu()               