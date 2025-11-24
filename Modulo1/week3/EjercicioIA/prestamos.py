# prestamos.py
import csv
import os
from datetime import datetime

PRESTAMOS_CSV = os.path.join("data", "prestamos.csv")
FIELDNAMES = ['prestamo_id','equipo_id','nombre_equipo','usuario_prestatario','tipo_usuario','fecha_solicitud','fecha_prestamo','fecha_devolucion','dias_autorizados','dias_reales_usados','retraso','estado','mes','anio']

# límites por tipo de usuario
LIMITE_DIAS = {
    'ESTUDIANTE': 3,
    'INSTRUCTOR': 7,
    'ADMINISTRATIVO': 10
}

def leer_prestamos():
    prestamos = []
    if not os.path.exists(PRESTAMOS_CSV):
        with open(PRESTAMOS_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
        return prestamos
    with open(PRESTAMOS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            prestamos.append(row)
    return prestamos

def guardar_prestamos(prestamos):
    with open(PRESTAMOS_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(prestamos)

def generar_id_prestamo(prestamos):
    if not prestamos:
        return '1'
    ids = [int(p['prestamo_id']) for p in prestamos if p.get('prestamo_id') and p['prestamo_id'].isdigit()]
    return str(max(ids) + 1)

def solicitar_prestamo(equipo_id, nombre_equipo, usuario_prestatario, tipo_usuario, fecha_prestamo_str, dias_solicitados):
    # Validaciones
    tipo_usuario = tipo_usuario.upper()
    if tipo_usuario not in LIMITE_DIAS:
        return False, f"Tipo de usuario inválido: {tipo_usuario}"
    if int(dias_solicitados) > LIMITE_DIAS[tipo_usuario]:
        return False, f"Días solicitados ({dias_solicitados}) exceden límite para {tipo_usuario} ({LIMITE_DIAS[tipo_usuario]})"
    try:
        fecha_prestamo = datetime.strptime(fecha_prestamo_str, '%Y-%m-%d')
    except ValueError:
        return False, "Formato de fecha inválido. Use YYYY-MM-DD"

    prestamos = leer_prestamos()
    nuevo_id = generar_id_prestamo(prestamos)
    hoy = datetime.now()
    prest = {
        'prestamo_id': nuevo_id,
        'equipo_id': str(equipo_id),
        'nombre_equipo': nombre_equipo,
        'usuario_prestatario': usuario_prestatario,
        'tipo_usuario': tipo_usuario,
        'fecha_solicitud': hoy.strftime('%Y-%m-%d'),
        'fecha_prestamo': fecha_prestamo.strftime('%Y-%m-%d'),
        'fecha_devolucion': '',
        'dias_autorizados': str(dias_solicitados),
        'dias_reales_usados': '',
        'retraso': 'NO',
        'estado': 'PENDIENTE',
        'mes': fecha_prestamo.strftime('%m'),
        'anio': fecha_prestamo.strftime('%Y')
    }
    prestamos.append(prest)
    guardar_prestamos(prestamos)
    return True, prest

def listar_prestamos_por_estado(estado):
    prestamos = leer_prestamos()
    return [p for p in prestamos if p['estado'] == estado]

def aprobar_prestamo(prestamo_id):
    prestamos = leer_prestamos()
    changed = False
    for p in prestamos:
        if p['prestamo_id'] == str(prestamo_id):
            if p['estado'] != 'PENDIENTE':
                return False, "El préstamo no está en estado PENDIENTE"
            p['estado'] = 'APROBADO'
            guardar_prestamos(prestamos)
            return True, p
    return False, "Prestamo no encontrado"

def rechazar_prestamo(prestamo_id):
    prestamos = leer_prestamos()
    for p in prestamos:
        if p['prestamo_id'] == str(prestamo_id):
            if p['estado'] != 'PENDIENTE':
                return False, "El préstamo no está en estado PENDIENTE"
            p['estado'] = 'RECHAZADO'
            guardar_prestamos(prestamos)
            return True, p
    return False, "Prestamo no encontrado"

def registrar_devolucion(prestamo_id, fecha_devolucion_str):
    prestamos = leer_prestamos()
    for p in prestamos:
        if p['prestamo_id'] == str(prestamo_id):
            if p['estado'] != 'APROBADO':
                return False, "Solo préstamos APROBADOS pueden devolverse"
            try:
                fecha_prestamo = datetime.strptime(p['fecha_prestamo'], '%Y-%m-%d')
                fecha_devolucion = datetime.strptime(fecha_devolucion_str, '%Y-%m-%d')
            except Exception as e:
                return False, "Formato de fecha inválido. Use YYYY-MM-DD"
            dias_reales = (fecha_devolucion - fecha_prestamo).days
            if dias_reales < 0:
                return False, "La fecha de devolución no puede ser anterior a la fecha de préstamo"
            p['fecha_devolucion'] = fecha_devolucion.strftime('%Y-%m-%d')
            p['dias_reales_usados'] = str(dias_reales)
            autorizados = int(p.get('dias_autorizados') or 0)
            p['retraso'] = 'SI' if dias_reales > autorizados else 'NO'
            p['estado'] = 'DEVUELTO'
            guardar_prestamos(prestamos)
            return True, p
    return False, "Prestamo no encontrado"

def historial_por_equipo(equipo_id):
    prestamos = leer_prestamos()
    return [p for p in prestamos if p['equipo_id'] == str(equipo_id)]

def historial_por_usuario(usuario_prestatario):
    prestamos = leer_prestamos()
    return [p for p in prestamos if p['usuario_prestatario'].lower() == usuario_prestatario.lower()]
