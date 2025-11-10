while True:
    try:    
        precio=float(input("Ingresa el precio: "))
        break
    except ValueError:
        print("Dato ingresado no valido.")
while True:
    try:
        cantidades=int(input("Ingresa cantidades: "))
        break
    except ValueError:
        print("Dato ingresado no valido.")  
precio_total=precio*cantidades    # VARIABLE DE OPERACION DE LAS ENTRADAS PEDIDAS     
print(f"El precio total de la compra es: {precio_total}")             

#SISTEMA DE VALIDACION Y RESULTADO DE OPERACION DE PRECIO