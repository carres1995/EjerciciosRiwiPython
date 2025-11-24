import csv
import os

USUARIOS_CSV = os.path.join("data", "usuarios.csv")

def cargar_usuarios():
    # Si no existe el archivo, se crea con un usuario por defecto
    if not os.path.exists(USUARIOS_CSV):
        os.makedirs("data", exist_ok=True)
        with open(USUARIOS_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['usuario', 'contrasena', 'rol'])
            writer.writerow(['admin', 'admin123', 'ADMIN'])

    usuarios = []
    with open(USUARIOS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            usuarios.append(row)
    return usuarios

def validar_login(usuario_input, contrasena_input):
    usuarios = cargar_usuarios()
    for u in usuarios:
        if u.get('usuario') == usuario_input and u.get('contrasena') == contrasena_input:
            return True
    return False
