"""1. Validación de datos con condicionales:
Crea un menú que pregunte al usuario qué acción desea realizar:
Agregar producto
Mostrar inventario
Calcular estadísticas
Salir
Usa condicionales if, elif y else para procesar la opción elegida.
Si el usuario ingresa una opción inválida, muestra un mensaje de error y pide nuevamente la entrada."""
lista=[]

while True:
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    while True:
        try:
            ingresa=int(input("Ingresa una de las opciones: "))
            break
        except ValueError:
            print("La opcion debe ser un numero")
    if ingresa == 1:
        while True:
            producto=input("ingrese Producto: ")
            try:    
                cantidad=int(input("Ingrese las cantidades: "))
            except ValueError:
                print("La opcion debe ser un numero")    
                break
            try:    
                precio=int(input("Ingrese el precio: "))
                break
            except ValueError:
                print("La opcion debe ser un numero") 
                break 
        lista.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio
        })
        print("Lista Creada con exito.")                
    elif ingresa == 2:
            if not lista:
                print("Lista vacia!!")
            else:   
                print("\n------INVENTARIO-PRODUCTOS------")
                for item in lista:
                    print(f" Producto: {item['producto']} | Cantidad: {item['cantidad']} | Precio: ${item['precio']:.0f}")
                print("---------------------------------\n")
    elif ingresa == 3:
        pass
    elif ingresa == 4:
        print("Gracias por ingresar!!")
        break
                