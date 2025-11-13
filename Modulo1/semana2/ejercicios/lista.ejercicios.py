'''1) Restaurante “Menú Dinámico” — Agregar plato del día
Como chef, quiero una función agregar_plato(menu, plato) que valide que plato no esté vacío y lo agregue a la lista menu.

Si el plato ya existe, mostrar “plato duplicado”.
Recorre el menú al final para imprimirlo numerado.
Sugerencia: usa list.append().'''
"""menu=[]

def agregar_plato(menu):#averiguar como lo puedo hacer con los dos parametros
    while True:
        plato=input("Agregar plato: ")
        if not plato.strip():
            print("El espacion no puede estar en vacio.")
        elif plato in menu:
            print("El plato ya existe.")
        elif plato == "fin".lower():  
            print("Gracias.")
            break  
        else:
            menu.append(plato)
        print("\n--------LISTA---------")    
        for i,p in enumerate(menu, start=1):
            print(f"{i} Plato: {p}")
        print("-------------------------\n")    

agregar_plato(menu)"""

'''2) Teatro “Butacas VIP” — Insertar reserva en posición
Como encargado de reservas, quiero una función insertar_reserva(butacas, nombre, posicion) que valide que posicion esté en rango y ubique la reserva en esa posición.

Si la posición no es válida, no inserta y muestra error.
Luego, recorre la lista para confirmar el orden.
Sugerencia: usa list.insert().'''
"""butacas=["Andres", "camilo", "Felipe", "Mateo"]
def insertar_reserva(butacas, nombre, posicion):
    if not posicion in range(len(butacas)):
        print("posicion no esta en lista")
    else:
        butacas.insert(posicion, nombre)
    for i, p in enumerate(butacas):
        print(f"{i}. {p}")        

insertar_reserva(butacas, "Mariana", 2)"""

'''3) Tienda “Combo Pack” — Extender inventario
Como supervisor, quiero una función extender_inventario(actual, nuevos) que valide que nuevos no esté vacío y una ambas listas.

Muestra el tamaño total al final.
Recorre la lista para destacar los recién agregados.
Sugerencia: usa list.extend().'''
"""lista=["Papel higienico","Papel Cocina","Servilletas"]
nuevo=[]
def extender_inventario(actual, nuevos):
    if not nuevos:
        print("Nueva lista no puede estar vacia.")
    else:
        actual.extend(nuevos)
        for l in actual:
            print(l)      

extender_inventario(lista, nuevo)"""

'''4) Biblioteca “Depuración de catálogo” — Eliminar libro específico
Como bibliotecario, quiero una función eliminar_libro(catalogo, titulo) que verifique si el título está y lo quite.

Si no existe, mostrar “no encontrado”.
Imprimir los libros restantes con un bucle.
Sugerencia: usa list.remove().'''
"""lista=["Biblia", "Kibalion","Coran"]
def eliminar_libro(catalogo, titulo):
    if not titulo in catalogo:
        print("El libro no esta en el catalogo.")
    else:
        catalogo.remove(titulo) 
        for i, libro in enumerate(catalogo):
            i+=1
            print(f"{i}. {libro}")   
eliminar_libro(lista, "Biblia")"""  

'''5) Cine “Liberar última silla” — Quitar el final
Como administrador de sala, quiero una función liberar_ultima(butacas) que valide que hay elementos y quite el último asiento reservado; debe retornar el valor removido.

Si no hay butacas, mostrar “sala vacía”.
Imprimir el estado final.
Sugerencia: usa list.pop() sin índice.'''
"""lista=["Camilo","Mateo","Felipe","Sebastian","Jorge"]
def liberar_ultima(butacas):
    if not butacas:
        print("No hay butacas.")
    else:
        print(f"Elemento eliminado: {butacas.pop()}")
    print("\n------Lista------")    
    for i,l in enumerate(butacas):
        i+=1
        print(f"{i}. {l}")
    print("----------------")    
    
liberar_ultima(lista)"""

'''6) Soporte “Búsqueda de ticket” — Encontrar primera coincidencia
Como agente de soporte, quiero una función buscar_ticket(tickets, codigo) que valide si codigo está y devuelva su índice.

Si no existe, retorna -1.
Usa un bucle para confirmar si hay duplicados y contarlos.
Sugerencia: usa list.index() (maneja excepciones) y/o list.count().'''
"""tickets=["1234","5678","9123","4567","1234","5678"]
def buscar_ticket(tickets, codigo):
    try:
        indice=tickets.index(codigo)    
        duplicado=tickets.count(codigo)
        
        print(f'El codigo esta en la posicion: {indice} y esta repetido {duplicado} veces.')
    except ValueError:
        print("Codigo no existente")    

buscar_ticket(tickets, "1234")  """  

"""Deportes “Marcador frecuente” — Contar apariciones
Como estadístico, quiero una función contar_marcador(marcadores, valor) que valide tipos y devuelva cuántas veces aparece valor.

Si no aparece, retornar 0.
Recorre la lista para imprimir posiciones donde aparece.
Sugerencia: usa list.count()."""
lista=[123,123,434,543,543,423,344]
def contar_marcador(marcadores, valor):
    if not marcadores:
        print("No existe lista.")
    else:
        for m in marcadores:
            if not valor in marcadores:
                return print(0)
            else:
                v= marcadores.count(valor)
                p=marcadores.index(valor)
        print(f"El valor aparece en {v}, posicion {p}")
        
#contar_marcador(lista,434)

"""Academia “Registro ordenado” — Orden asc/desc configurable
Como coordinador, quiero una función ordenar_registros(registros, descendente=False) que valide que todos los elementos sean comparables y ordene.

Si descendente es True, ordenar en orden inverso.
Recorre la lista para imprimir el TOP 3."""
lista=[11,52,3,True,False,32,0]
def ordenar_registros(registros, descendente=False):
    grupo_numerico=(int, float, bool)
    grupo_text=(str,)
    inicio=registros[0]
    if isinstance(inicio, grupo_numerico):
        grupo= grupo_numerico
    if isinstance(inicio,grupo_text):
        grupo= grupo_text
    for i in registros:
        if not isinstance(i, grupo):
            print("No se puede comparar")
        else:    
            if descendente == False:
                registros.sort()
            else:
                registros.sort(reverse=True)
    for t in registros[0:3]:
        print(t) 
#ordenar_registros(lista, False)

"""9) Música “Playlist Reversa” — Escucha en orden invertido
Como DJ, quiero una función invertir_playlist(playlist) que valide que no esté vacía y la invierta en sitio.

Luego, recorre la lista para reproducir las primeras 5 canciones (o menos si no hay suficientes)."""
listado=["luna","esta noche","tu furor", "male", "somos","si te vas", "como fue", "hola", "moon"]
def invertir_playlist(playlist):
    if not playlist:
        print("No puede estar vacia")
    else:
        playlist.reverse()
        for r in playlist[0:5]:
            print(r)

#invertir_playlist(listado)

"""10) Cursos “Duplicar plan de estudio” — Copia segura
Como tutor, quiero una función clonar_plan(modulos) que cree una copia independiente de la lista original para probar cambios sin afectar la original.

Verifica con un cambio en la copia que la original no se altere.
Usa bucles para mostrar diferencias."""
l=["estadistica","ingles", "habilidades blandas", "sociales","biologia"]
def clonar_modulos(modulos):
    n_modulo=modulos.copy()
    n_modulo.append("matematicas")
    for o in modulos:
        original=len(modulos)
    for n in n_modulo:
        nuevo=len(n_modulo)
    print(f"Original: {original}")
    print(f"Nuevo: {nuevo}")    
#clonar_modulos(l)