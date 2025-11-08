#Este es un ciclo while de validacion en el caso que no cumpla con lo pedido vuelva y pregunte.
while True:  
    #Estas son variables de entrada  
    nombre=input("Ingresa tu nombre: ").strip()#este es un metodo que garantiza no enviar inputs vacios
    if nombre:
        break
    else:
        print("Error no se puede el espacio en vacio")
    
        
    
while True:
    #HACE LA FUNCION DE VALIDADOR PARA EVITAR ERROR DE VALOR EN LA VARIABLE
    try:
        precio=float(input("Ingresa el precio: "))
        break
    except ValueError:#EL TIPO DE ERROR ES EL QUE GARANTIZA EL TIPO DE ERROR EN ESTE CASO EL VALOR DE ENTRADA DE LA VARIABLE
        print("Error debe ser un numero o un numero decimal")
        
    
        
while True:
    try:
        cantidad=int(input("Ingresa las cantidades: "))
        break
    except ValueError:
        print("Error debe ser un numero entero")

print("Gracias por ingresar")   

#GENERA VALIDACION DE LOS ELEMENTOS DE LOS INPUTS.

