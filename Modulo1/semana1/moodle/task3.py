while True:
        nombre_producto=input("Ingresa tu nombre del producto: ").strip()
        if nombre_producto:
            break
        else:
            print("No puede estar vacio")
while True:
    try:
        precio_unitario=float(input("Ingresa el precio: "))
        break
    except ValueError:
        print("Debe ser un numero o un decimal.")
while True:
    try:
        cantidades=int(input("Ingresa las cantidades: "))
        break
    except ValueError:
         print("debe ser un numero entero.")
     
total=cantidades*precio_unitario

print(f"Producto: {nombre_producto} | Precio: {precio_unitario:.0f} | Cantidades: {cantidades} | Total compra: {total:.0f}") #RESULTADO DE 