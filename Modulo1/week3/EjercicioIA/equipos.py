# equipos.py
import csv
import os
from datetime import datetime

EQUIPOS_CSV = os.path.join("data", "equipos.csv")
FIELDNAMES = ['equipo_id','nombre_equipo','categoria','estado_actual','fecha_registro','descripcion']

def leer_equipos():
    equipos = []
    if not os.path.exists(EQUIPOS_CSV):
        # crear con header si no existe
        with open(EQUIPOS_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
        return equipos
    with open(EQUIPOS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            equipos.append(row)
    return equipos

def guardar_equipos(equipos):
    with open(EQUIPOS_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(equipos)

def generar_id_equipos(equipos):
    if not equipos:
        return '1'
    ids = [int(e['equipo_id']) for e in equipos if e.get('equipo_id') and e['equipo_id'].isdigit()]
    return str(max(ids) + 1)

def registrar_equipo(nombre, categoria, descripcion=""):
    equipos = leer_equipos()
    nuevo_id = generar_id_equipos(equipos)
    equipo = {
        'equipo_id': nuevo_id,
        'nombre_equipo': nombre,
        'categoria': categoria,
        'estado_actual': 'DISPONIBLE',
        'fecha_registro': datetime.now().strftime('%Y-%m-%d'),
        'descripcion': descripcion
    }
    equipos.append(equipo)
    guardar_equipos(equipos)
    return equipo["nombre_equipo"]

def listar_equipos():
    return leer_equipos()

def mostrar_equipo_por_id(equipo_id):
    equipos = leer_equipos()
    for e in equipos:
        if e['equipo_id'] == str(equipo_id):
            return e
    return None

def actualizar_estado_equipo(equipo_id, nuevo_estado):
    equipos = leer_equipos()
    for e in equipos:
        if e['equipo_id'] == str(equipo_id):
            e['estado_actual'] = nuevo_estado
            guardar_equipos(equipos)
            return True
    return False
