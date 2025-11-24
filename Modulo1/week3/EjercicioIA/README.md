# TechLab Inventory Console – Gestión de equipos tecnológicos

Autor: Carlos Andrés Restrepo Yepes (por ejemplo)
Descripción: Aplicación de consola en Python para gestión de equipos y préstamos del TechLab.

Requisitos:
- Python 3.8+
- Estructura de carpetas:
  - data/usuarios.csv
  - data/equipos.csv
  - data/prestamos.csv

Cómo ejecutar:
1. Coloca los CSV en la carpeta data/ (ver ejemplos en el repositorio).
2. Ejecuta: python main.py
3. Login con usuario y contraseña (default: admin/admin123).

CSV necesarios:
- usuarios.csv (usuario,contrasena,rol) — solo un ADMIN permitido.
- equipos.csv (equipo_id,...)
- prestamos.csv (prestamo_id,...)

Reglas de préstamo:
- Estudiante: máximo 3 días.
- Instructor: máximo 7 días.
- Administrativo: máximo 10 días.
- Un equipo debe ser DISPONIBLE para poder solicitar un préstamo.

Estructura del proyecto:
- main.py: entrada y menú.
- usuarios.py: login.
- equipos.py: CRUD de equipos.
- prestamos.py: lógica de préstamos y devoluciones.
- reportes.py: exportar reportes CSV.

Limitaciones:
- Interfaz en consola (no GUI).
- No hay control de sesiones multiusuario simultáneas.
- No cifrado de contraseñas (en texto plano por simplicidad).

Mejoras futuras:
- Encriptación de contraseñas.
- Interfaz web.
- Integración con base de datos SQL.
