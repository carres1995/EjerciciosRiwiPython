# reportes.py
import csv
import os
from datetime import datetime

PRESTAMOS_CSV = os.path.join("data", "prestamos.csv")

def generar_reporte_csv(mes, anio, salida=None):
    mes = str(mes).zfill(2)
    anio = str(anio)
    prestamos = []
    if not os.path.exists(PRESTAMOS_CSV):
        return False, "No existe archivo de prestamos."
    with open(PRESTAMOS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('estado') == 'DEVUELTO' and row.get('mes') == mes and row.get('anio') == anio:
                prestamos.append(row)
    if not prestamos:
        return False, "No hay prestamos DEVUELTOS para el mes y año indicados."
    if not salida:
        salida = f"reporte_prestamos_{anio}_{mes}.csv"
    with open(salida, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['prestamo_id','equipo_id','nombre_equipo','usuario_prestatario','tipo_usuario','dias_autorizados','dias_reales_usados','retraso','estado','mes','anio']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in prestamos:
            row = {k:p.get(k,'') for k in fieldnames}
            writer.writerow(row)
    return True, salida
