"""1. Restaurante “Buen Sabor” – Cálculo de propina
Como mesero, quiero una función calcular_propina(total_cuenta) que reciba el valor total de la cuenta y calcule la propina del 10%.
Si el total es mayor de $100.000, aplicar el 15%.
El programa debe mostrar el total final a pagar."""
#cuenta= float(input("Ingrese valor de la cuenta: "))
def calcular_propina(total_cuenta):
    
    propina1= 0.1
    propina2= 0.15
    if cuenta >= 100000:
        total_cuenta= cuenta + (propina2*cuenta)
        print(f"Saldo total con propina del 15% {total_cuenta}")
    elif cuenta > 0:
        total_cuenta= cuenta + (propina1*cuenta)
        print(f"Saldo total con propina del 10% {total_cuenta}")
    
    else:
        print("Precio no valido")    
    return total_cuenta    

#calcular_propina(cuenta)

"""2. Gimnasio “Level Up” – Control de repeticiones
Como entrenador, quiero una función repeticiones(n) que use un bucle for para mostrar las repeticiones del 1 al número indicado.
Si el número actual es par, mostrar “Excelente forma”, si no, “Mantén el ritmo”."""
#numero=int(input("Numero de repeticiones: "))
def repeticiones(n):
    for i in range(n):
        if i %2 == 0:
            print("“Excelente forma”")
        else:
            print("“Mantén el ritmo”")
    return n 

#repeticiones(numero)  

"""3. Tienda “LoopShop” – Descuentos acumulados
Como vendedor, quiero una función aplicar_descuentos() que pida varios precios hasta que el usuario escriba 0.
Si el precio supera 50.000, aplicar 10% de descuento.
Al final, mostrar la suma total de las compras con descuento."""

def aplicar_descuentos():
    acumulado=0
    while True:
        precio= float(input("Ingrese valor de compra: "))
        descuento= precio*0.9
        if precio > 50000:
            acumulado += descuento
            print("precio con descuento ",acumulado)
        elif precio >0:
            acumulado += precio 
            print("precio ",acumulado)
        else:
            print("fin de las ventas")
            print(f"Valor ventas del dia {acumulado}")  
            break
                 
#aplicar_descuentos()
            
"""4. Banco “PythonBank” – Evaluador de crédito
Como asesor financiero, quiero una función evaluar_credito(ingresos, edad) que:

Apruebe el crédito si los ingresos son mayores de 2 millones y la edad está entre 25 y 60.
Si no cumple, mostrar “Crédito rechazado”.
Usar condicionales dentro de la función."""  
#ingresos=float(input("Ingresar tus ingresos: "))
#edad= int(input("Ingresa edad: "))
def evaluar_credito(ingresos, edad):
    if ingresos > 2000000 and edad >24 and edad <61:
        print("Credito aprobado")
    else:
        print("Credito rechazado")

#evaluar_credito(2000000,28)

"""5. Escuela “Aprende Más” – Promedio de notas
Como profesor, quiero una función promedio_notas() que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0 → mostrar “Aprobado”, de lo contrario “Reprobado”.
Debe repetirse para varios estudiantes usando un while."""

def promedio_notas():
    nota1=float(input('Ingrese la nota 1: '))
    nota2=float(input('Ingrese la nota 2: ')) 
    nota3=float(input('Ingrese la nota 3: '))
    promedio= (nota1+nota2+nota3)/3
    if promedio >= 3:
        print('Aprobado, promedio: ', promedio)
    else:
        print('Reprobado, promedio: ', promedio)  

#promedio_notas()

"""6. Estación “LoopBus” – Simulador de pasajeros
Como conductor, quiero una función simular_viaje(pasajeros) que recorra con un for cada pasajero y muestre “Pasajero X a bordo”.
Si llega a 10 pasajeros, mostrar “Bus lleno” y detener el bucle."""
def simular_viaje(pasajeros:int): 
    for pasajero in range(1,(1+pasajeros)):
        if pasajero == 10:
            print('“Bus lleno”')
            break  
        
        print(f'Pasajeros {pasajero} a bordo')
              

#simular_viaje(10)              
    
"""7. Panadería “Don Pancho” – Control de producción diaria
Como panadero, quiero una función hornear_pan(lotes) que use un for para indicar qué lote se está horneando.
Si el lote es divisible por 3, mostrar “Verificación de calidad”.
Al final, mostrar “Producción terminada”."""  

def hornear_pan(lotes):
    for lote in range(1,1 +lotes):
        if lote %3 == 0:
            print(f'Verificacion de lote n: {lote}')
        elif lote == lotes:
            print(f'Lote horneado n: {lote}') 
            print('Produccion terminada') 
        else:    
            print(f'Lote horneado n: {lote}')         

#hornear_pan(10)   

'''8. Cine “MovieLoop” – Calculadora de entradas
Como cajero, quiero una función calcular_entradas() que pida edades de los clientes hasta que se ingrese 0.
Aplicar precio:

Menores de 12 → $5.000
De 12 a 59 → $8.000
Mayores de 60 → $4.000
Usar un while y condiciones.''' 

def calcular_entradas():
    while True:
        edad=int(input('Ingresar edad: '))
        if edad > 59:
            print('Tu pagas $4.000')
        elif edad > 11:
            print('Tu pagas $8.000')
        elif edad > 0:
            print('Tu pagas $5.000')        
        else:
            print('Gracias')
            break

#calcular_entradas() 

'''9. Tienda “EnergyStore” – Simulador de puntos
Como cliente, quiero una función calcular_puntos(compras) que use un for para recorrer la cantidad de compras (ingresada por el usuario).
Si el número de compra es múltiplo de 3, agregar 10 puntos; en caso contrario, agregar 5.
Al final, mostrar los puntos totales.'''
#compras=int(input('Numero de compras: '))   
def calcular_puntos(compras):
    if compras <= 0:
        print("No realizaste compras. Gracias por visitarnos.")
        
    acumulado_puntos=0
        
    
    for compra in range(1,compras +1):
        if compra %3 == 0:
            acumulado_puntos += 10
            print('Tienes 10 puntos adicionales')
                    
        else:
            acumulado_puntos += 5
            print('Tienes 5 puntos adicionales')
    print(f"Tus puntos totales son: {acumulado_puntos}")     
#calcular_puntos(compras)                          

'''10. Academia “CodeStart” – Tabla de multiplicar personalizada
Como estudiante, quiero una función tabla_multiplicar(numero) que use un for para mostrar la tabla del número dado hasta el 10.
Si el resultado es mayor de 50, mostrar también “Resultado alto”.'''

def tabla_multiplicar(numero):
    for n in range(1, 11):
        multiplo=n*numero
        print(f'{n} x {numero} = {multiplo}')
        if multiplo > 50:
            print('Resultado alto')
        
#numero=int(input('Ingresa numero a multiplicar: '))

#tabla_multiplicar(numero)  

'''11. Aerolínea “FlyLoop” – Cálculo de millas acumuladas
Como viajero frecuente, quiero una función calcular_millas(viajes) que reciba el número de viajes realizados y sume millas según la distancia:

Viaje corto (< 1000 km): 500 millas
Medio (1000–3000 km): 1000 millas
Largo (> 3000 km): 2000 millas
Debe repetirse hasta que el usuario escriba “fin” y mostrar el total acumulado.'''  


def calcular_millas():
    
    total_millas=0
    while True:
        viajes=(input('Ingresa la distancia recorrida: '))
        if viajes == 'fin':
            print('fin gracias')
            break
        else:
            n_viaje=int(viajes)
            
            
            if n_viaje >= 3000:
                millas = 3000
                
            elif n_viaje >= 1000:
                millas =1000
                
            elif n_viaje > 0:
                millas =500
            else:
                print("Debe existir una distancia positiva")
            total_millas += millas    
            print(f"Recorriste {n_viaje} km, ganaste {millas} millas. Total acumulado: {total_millas} millas.")
    print(f'fin programa millas acumuladas: {total_millas}')            
        
                        


calcular_millas()