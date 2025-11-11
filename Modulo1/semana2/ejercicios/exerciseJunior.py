"""11. Banco “PythonBank” – Simulación de ahorro mensual
Como cliente, quiero usar un for que sume mi ahorro mensual durante 6 meses.
Si en algún mes el total supera $1,000,000, mostrar “¡Meta alcanzada!”.
Al final, mostrar el total acumulado."""

"""mensual=int(input("Ingrese valor: "))
ahorro= mensual * 0.20
ahorro_total=0
for i in range(1,7):
    ahorro_total += ahorro
    if ahorro_total >= 1000000:
        print(f"Ahorro total: {ahorro_total}")
        print("Meta alcanzada!")
        break
    else:
        print(f"Ahorro total: {ahorro_total}")"""


"""12. Gimnasio “Level Up” – Control de repeticiones
Como deportista, quiero ingresar un número de repeticiones y usar un for para imprimir “Repetición X completada”.
Si X es divisible por 3, mostrar además “¡Excelente ritmo!”."""

"""print("Gimnasio “Level Up”")
repeticion=int(input("Nuemro de repeticiones: "))
for i in range(repeticion):
    repeticion += 1
    if repeticion %3 == 0:
        print("¡Excelente ritmo!")
    else:
        print("Repetición X completada")   """ 

"""13. Parqueadero “AutoLoop” – Control de vehículos
Como vigilante, quiero usar un while que cuente vehículos hasta llegar a 20.
Si entra un número par, mostrar “Vehículo par registrado”.
Si el total llega a 20, mostrar “Capacidad completa”."""    
"""print("Parqueadero “AutoLoop”")   
vehiculo=0
while vehiculo <= 20:
    vehiculo += 1
    if vehiculo %2 == 0:
        print(f"Vehiculo par {vehiculo} registrado")
    if vehiculo == 20:
        print("Capacidad completa!") """



"""14. Tienda “Ahorra Más” – Caja registradora básica
Como cajero, quiero pedir montos de venta hasta que el usuario escriba 0.
Si la venta supera $100,000, mostrar “Venta destacada”.
Al final, mostrar el total vendido."""
"""print("Tienda “Ahorra Más”")     
acumulado=0
while True:
    ventas=float(input("Ingresa valor de la venta: "))
    acumulado += ventas
    if ventas >= 100000:
        print("Venta destada!!")
    if ventas < 1:
        print(f"Caja cerrada tus ventas fueron de {acumulado:.0f}")
        break 
    print(f"venta de {ventas}") """

"""15. Academia “CodeStart” – Contador de ejercicios completados
Como estudiante, quiero usar un for del 1 al número que indique.
Si el número es múltiplo de 5, mostrar “¡Gran avance!”.
Si no, solo mostrar “Ejercicio X completado”."""            
"""print("Academia “CodeStart”")

ejercicio=int(input("Numero de ejercicios: "))
for i in range(ejercicio):
    i += 1
    if i %5 == 0:
        print("Gran avance!!!")
    else:    
        print(f'Ejercicio {i} completado')  """  

        