#Este es un ciclo while de validacion en el caso que no cumpla con lo pedido vuelva y pregunte.
 
    #Estas son variables de entrada  
nombre=input("Ingresa nombre producto: ").strip()#este es un metodo que garantiza no enviar inputs vacios con la validacion siguiente
if nombre:
    nombre
        
while True:
    try:
        cantidad=int(input("Ingresa las cantidades: "))
        precio=float(input("Ingresa el precio: "))
        break
    except ValueError:
        print("Error debe ser un numero entero")
#SISTEMA DE VALIDACION Y RESULTADO DE OPERACION DE PRECIO  
costo_total=precio*cantidad    # VARIABLE DE OPERACION DE LAS ENTRADAS PEDIDAS     
print(f"\nProducto: {nombre} | Precio: {precio:.0f} | Cantidades: {cantidad} | Total compra: {costo_total:.0f}")            

print("Gracias por ingresar")   

#GENERA VALIDACION DE LOS ELEMENTOS DE LOS INPUTS.

