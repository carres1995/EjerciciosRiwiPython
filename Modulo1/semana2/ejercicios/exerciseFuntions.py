"""21. Tienda “FuncionaShop” – Mensaje de bienvenida
Como dueño de la tienda, quiero crear una función llamada saludo() que imprima “Bienvenido a FuncionaShop”.
Luego, quiero llamarla desde el programa principal."""

def saludo():
    print("Bienvenido a Tienda FuncionaShop")
    
"""22. Gimnasio “StrongFit” – Cálculo de energía
Como entrenador, quiero una función calcularEnergia() que reciba un número de repeticiones y devuelva un mensaje:

Si las repeticiones son menores de 5 → “Necesitas más esfuerzo”.
Si son 5 o más → “¡Buen trabajo!”."""    


def calcularEnergia():
    print('Gimnasio “StrongFit”')
    repeticiones=int(input('Numero de repeticiones: '))
    if repeticiones > 0 and repeticiones < 6:
        print('Necesitas más esfuerzo') 
    elif repeticiones > 5:
        print('¡Buen trabajo!') 
        
"""23. Banco “LoopBank” – Simulación de intereses
Como analista financiero, quiero una función calcularInteres() que reciba un monto y una tasa (porcentaje) y retorne el valor final después de aplicar el interés una vez.
El programa principal debe pedir los datos y mostrar el resultado."""    
def calcularIntereses():
    print('Banco “LoopBank”')
    monto=float(input('Ingresa el monto: '))
    tasa=int(input('Ingresa interes en %: '))
    interes = tasa / 100
    total= monto + (monto * interes)
    print('monta mas intereses: ', total )

"""24. Escuela “Aprende con Funciones” – Promedio de notas
Como profesor, quiero crear una función promedioNotas() que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0, mostrar “Aprobado”; si no, “Reprobado”."""    
def promedioNotas():
    nota1=float(input('Ingrese la nota 1: '))
    nota2=float(input('Ingrese la nota 2: ')) 
    nota3=float(input('Ingrese la nota 3: '))
    promedio= (nota1+nota2+nota3)/3
    if promedio >= 3:
        print('Aprobado, promedio: ', promedio)
    else:
        print('Reprobado, promedio: ', promedio)     

'''25. Restaurante “BuenaFunción” – Verificación de turno
Como gerente, quiero una función verificarTurno(hora) que determine:

Si la hora es menor que 12 → “Turno de mañana”.
Si está entre 12 y 18 → “Turno de tarde”.
Si es mayor → “Turno de noche”.
El programa principal debe pedir la hora e imprimir el resultado.'''  
def verificarTurno(hora):
    if hora < 0:
        print('Error los numeros negativos no hacen parte del horario')
    elif hora < 12:
        print('Turno de la manana')
    elif hora < 18:
        print('Turno de la tarde')
    elif hora < 24:
        print('Turno de la noche')
    else: 
        print('Horario no valido') 
    return                    

def menuEjercicios():
    while True:
        print('\n1. Ejercicio Tienda')
        print('2. Calcular energia')
        print('3. Calcular intereses')
        print('4. Promedio notas')
        print('5. verificar turno de trabajo')
        print('6. Salida\n')
        opcion=input("Que ejercicio quieres probar: ")  
        
        if opcion == '1':
            saludo()
        elif opcion == '2':
            calcularEnergia() 
        elif opcion == '3':
            calcularIntereses() 
        elif opcion =='4':
            promedioNotas() 
        elif opcion == '5':
            hora=float(input('Ingresa la hora: '))
            verificarTurno(hora)             
        elif opcion == '6':
            break    
            

if __name__ == '__main__':            
    menuEjercicios()        