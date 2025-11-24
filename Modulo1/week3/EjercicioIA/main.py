# main.py
from usuarios import validar_login
from equipos import registrar_equipo, listar_equipos, mostrar_equipo_por_id, actualizar_estado_equipo
from prestamos import (solicitar_prestamo, listar_prestamos_por_estado, aprobar_prestamo, rechazar_prestamo,
                       registrar_devolucion, historial_por_equipo, historial_por_usuario)
from reportes import generar_reporte_csv

def menu_principal():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Gestionar equipos")
        print("2. Gestionar prestamos")
        print("3. Historial")
        print("4. Exportar reporte CSV")
        print("5. Salir")
        opt = input("Elige una opción: ").strip()
        if opt == '1':
            gestionar_equipos()
        elif opt == '2':
            gestionar_prestamos()
        elif opt == '3':
            gestionar_historial()
        elif opt == '4':
            exportar_reporte()
        elif opt == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

def gestionar_equipos():
    while True:
        print("\n--- GESTION EQUIPOS ---")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Consultar equipo por ID")
        print("4. Volver")
        opt = input("Opción: ").strip()
        if opt == '1':
            nombre = input("Nombre equipo: ").strip()
            categoria = input("Categoria: ").strip()
            descripcion = input("Descripcion (opcional): ").strip()
            equipo = registrar_equipo(nombre, categoria, descripcion)
            print("Equipo registrado:", equipo)
        elif opt == '2':
            equipos = listar_equipos()
            if not equipos:
                print("No hay equipos registrados.")
            else:
                for e in equipos:
                    print(f"{e['equipo_id']:<10} | {e['nombre_equipo']:<15} | {e['categoria']:<15} | {e['estado_actual']:<10}")
        elif opt == '3':
            eid = input("ID equipo: ").strip()
            e = mostrar_equipo_por_id(eid)
            if not e:
                print("Equipo no encontrado.")
            else:
                for k,v in e.items():
                    print(f"{k}: {v}")
        elif opt == '4':
            break
        else:
            print("Opción inválida.")

def gestionar_prestamos():
    while True:
        print("\n--- GESTION PRESTAMOS ---")
        print("1. Solicitar prestamo (crea PENDIENTE)")
        print("2. Listar solicitudes pendientes")
        print("3. Aprobar solicitud")
        print("4. Rechazar solicitud")
        print("5. Registrar devolucion")
        print("6. Volver")
        opt = input("Opción: ").strip()
        if opt == '1':
            eid = input("ID equipo: ").strip()
            from equipos import mostrar_equipo_por_id
            e = mostrar_equipo_por_id(eid)
            if not e:
                print("Equipo no encontrado.")
                continue
            if e['estado_actual'] != 'DISPONIBLE':
                print("Equipo no disponible para préstamo:", e['estado_actual'])
                continue
            nombre_usr = input("Nombre del solicitante: ").strip()
            tipo_usr = input("Tipo usuario (ESTUDIANTE/INSTRUCTOR/ADMINISTRATIVO): ").strip()
            fecha_prestamo = input("Fecha inicio préstamo (YYYY-MM-DD): ").strip()
            dias = input("Días solicitados: ").strip()
            ok, resp = solicitar_prestamo(eid, e['nombre_equipo'], nombre_usr, tipo_usr, fecha_prestamo, dias)
            if ok:
                print("Solicitud registrada (PENDIENTE). ID:", resp['prestamo_id'])
            else:
                print("Error al registrar solicitud:", resp)
        elif opt == '2':
            pendientes = listar_prestamos_por_estado('PENDIENTE')
            if not pendientes:
                print("No hay solicitudes pendientes.")
            else:
                for p in pendientes:
                    print(f"{p['prestamo_id']} | {p['nombre_equipo']} | {p['usuario_prestatario']} | {p['tipo_usuario']} | {p['estado']}")
        elif opt == '3':
            pid = input("ID de solicitud a aprobar: ").strip()
            ok, resp = aprobar_prestamo(pid)
            if ok:
                # actualizar estado del equipo a PRESTADO
                actualizar_estado_equipo(resp['equipo_id'], 'PRESTADO')
                print("Solicitud aprobada:", resp['prestamo_id'])
            else:
                print("Error:", resp)
        elif opt == '4':
            pid = input("ID de solicitud a rechazar: ").strip()
            ok, resp = rechazar_prestamo(pid)
            if ok:
                print("Solicitud rechazada:", resp['prestamo_id'])
            else:
                print("Error:", resp)
        elif opt == '5':
            pid = input("ID de préstamo (APROBADO) a devolver: ").strip()
            fecha_dev = input("Fecha de devolución (YYYY-MM-DD): ").strip()
            ok, resp = registrar_devolucion(pid, fecha_dev)
            if ok:
                # poner equipo DISPONIBLE
                actualizar_estado_equipo(resp['equipo_id'], 'DISPONIBLE')
                print("Devolución registrada. Retraso:", resp['retraso'])
            else:
                print("Error:", resp)
        elif opt == '6':
            break
        else:
            print("Opción inválida.")

def gestionar_historial():
    while True:
        print("\n--- HISTORIAL ---")
        print("1. Historial por equipo")
        print("2. Historial por usuario")
        print("3. Volver")
        opt = input("Opción: ").strip()
        if opt == '1':
            eid = input("ID equipo: ").strip()
            hist = historial_por_equipo(eid)
            if not hist:
                print("No hay historial para este equipo.")
            else:
                for p in hist:
                    print(f"{p['prestamo_id']} | {p['usuario_prestatario']} | {p['estado']} | autorizados:{p['dias_autorizados']} | reales:{p.get('dias_reales_usados','') } | retraso:{p['retraso']}")
        elif opt == '2':
            user = input("Nombre usuario: ").strip()
            hist = historial_por_usuario(user)
            if not hist:
                print("No hay historial para este usuario.")
            else:
                for p in hist:
                    print(f"{p['prestamo_id']} | {p['nombre_equipo']} | {p['estado']} | {p['mes']}/{p['anio']} | retraso:{p['retraso']}")
        elif opt == '3':
            break
        else:
            print("Opción inválida.")

def exportar_reporte():
    mes = input("Mes (1-12): ").strip()
    anio = input("Año (YYYY): ").strip()
    ok, resp = generar_reporte_csv(mes, anio)
    if ok:
        print("Reporte generado:", resp)
    else:
        print("No se generó reporte:", resp)

if __name__ == "__main__":
    # Login con máximo 3 intentos
    print("==== TechLab Inventory Console ====")
    intentos = 0
    while intentos < 3:
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()
        if validar_login(usuario, contrasena):
            print("Login correcto. Bienvenido", usuario)
            menu_principal()
            break
        else:
            intentos += 1
            print(f"Credenciales incorrectas. Intentos restantes: {3-intentos}")
    else:
        print("Máximo de intentos alcanzado. Cerrando programa.")
