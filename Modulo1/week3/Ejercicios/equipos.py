from datetime import datetime
from pathlib import Path
from archivo_csv import leer_archivo, guardar_csv
from utils import id_auto, tabla_general

RUTA_EQUIPOS = Path("Modulo1/week3/Ejercicios/data/equipos.csv")
CABECERAS = ["equipo_id", "nombre_equipo", "categoria",
             "estado_actual", "fecha_registro", "descripcion"]

# ----------  persistencia  ----------
def cargar_equipos():
    """Lee el CSV y devuelve lista de diccionarios."""
    return leer_archivo(RUTA_EQUIPOS) or []


def guardar_equipos(eq):
    """Graba la lista completa en el CSV."""
    guardar_csv(RUTA_EQUIPOS, eq, CABECERAS)


# ----------  lógica  ----------
def registrar_equipo(nombre, categoria, descripcion="", eq=None):
    """Crea el equipo en memoria y lo devuelve."""
    if eq is None:
        eq = cargar_equipos()

    nuevo = {
        "equipo_id": str(id_auto(eq, "equipo_id")),
        "nombre_equipo": nombre,
        "categoria": categoria,
        "estado_actual": "DISPONIBLE",
        "fecha_registro": datetime.now().strftime("%Y-%m-%d"),
        "descripcion": descripcion
    }
    eq.append(nuevo)
    return nuevo


# ----------  presentación  ----------
def listar_equipos(eq=None):
    """Muestra la tabla sin tocar el disco."""
    if eq is None:
        eq = cargar_equipos()

    if not eq:
        print("No hay equipos para mostrar.")
        return

    encabezados = ("ID", "Nombre", "Categoría", "Estado", "Fecha", "Descripción")
    anchos = (5, 12, 10, 10, 10, 30)

    datos = [
        {
            "ID": str(e.get("equipo_id", "")),
            "Nombre": e.get("nombre_equipo", ""),
            "Categoría": e.get("categoria", ""),
            "Estado": e.get("estado_actual", ""),
            "Fecha": e.get("fecha_registro", ""),
            "Descripción": e.get("descripcion", "")
        }
        for e in eq
    ]

    print("--" * 20, "Lista de Equipos", "--" * 20)
    tabla_general(datos, encabezados, anchos)