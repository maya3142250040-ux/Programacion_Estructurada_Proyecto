import mysql.connector
from fpdf import FPDF
import os
import re

CONFIG_BD = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",
    "database": "bookso"
}

def borrarPantalla():
    print("\033c")

def espereTecla():
    input("\n    ⏳ ...Presiona cualquier tecla para continuar... ⏳\n")

def opcionInvalida():
    input("\n    ⚠️  ...Opción inválida, por favor verifique... ⚠️\n")

def accionExitosa():
    input("\n    ✅ ...Acción realizada con éxito... ✅\n")

def accionNoExitosa():
    input("\n    ❌ ...No fue posible realizar esta acción... ❌\n")

def terminarSistema():
    print(
        "\n    ╔══════════════════════════════════════════╗"
        "\n    ║   GRACIAS POR UTILIZAR NUESTRO SISTEMA   ║"
        "\n    ╚══════════════════════════════════════════╝\n"
    )
def conectar():
    try:
        conexion = mysql.connector.connect(**CONFIG_BD)
        return conexion
    except Exception as e:
        print("ERROR DE CONEXION:", e)
        return None

def menuPrincipal():
    print(r"""
     ____   ___   ___  _  ______   ___  
    | __ ) / _ \ / _ \| |/ / ___| / _ \ 
    |  _ \| | | | | | | ' /\___ \| | | |
    | |_) | |_| | |_| | . \ ___) | |_| |
    |____/ \___/ \___/|_|\_\____/ \___/ 
        Sistema de Gestión de Libros
                  y reseñas de usuarios
    """)
    print(
        "\n    ╔══════════════════════════════╗"
        "\n    ║    📚 MENÚ PRINCIPAL 📚      ║"
        "\n    ╚══════════════════════════════╝"
    )
    print("             1.- 📖 Libros")
    print("    ──────────────────────────────")
    print("             2.- 👤 Usuarios")
    print("    ──────────────────────────────")
    print("             3.- ⭐ Reseñas")
    print("    ──────────────────────────────")
    print("             4.- 🚪 Salir")
    print("    ──────────────────────────────")
    return input("       Elige una opción: ")

def exportLibrosPdf(conexionBD, ruta="exportados"):
    os.makedirs(ruta, exist_ok=True)
    cursor = conexionBD.cursor()
    cursor.execute("SELECT id, libro, autor, genero, clasificacion, origen FROM libros")
    libros = cursor.fetchall()

    if len(libros) == 0:
        return False

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Reporte de Libros", ln=True, align="C")
    pdf.ln(5)
    pdf.set_font("Arial", "", 11)

    for i in libros:
        pdf.multi_cell(0, 7,
            f"Codigo: {i[0]}\n"
            f"Libro: {i[1]}\n"
            f"Autor: {i[2]}\n"
            f"Genero: {i[3]}\n"
            f"Clasificacion: {i[4]}\n"
            f"Origen: {i[5]}"
        )
        pdf.ln(2)
        pdf.cell(0, 0, "", border="T")
        pdf.ln(5)

    archivoRuta = os.path.join(ruta, "reporte_libros.pdf")
    pdf.output(archivoRuta)
    print(f"\n\t...¡Archivo generado en: {os.path.abspath(archivoRuta)}!...")
    return True


def exportReseñasPdf(conexionBD, ruta="exportados"):
    os.makedirs(ruta, exist_ok=True)
    cursor = conexionBD.cursor()
    cursor.execute("""
        SELECT l.ID, l.libro, u.usuario, r.titulo, r.reseña
        FROM reseñas r
        JOIN libros l ON r.id_libro = l.ID
        JOIN usuario u ON r.id_usuario = u.id
        ORDER BY l.ID
    """)
    reseñas = cursor.fetchall()

    if len(reseñas) == 0:
        return False

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Reporte de Reseñas", ln=True, align="C")
    pdf.ln(5)

    libroActual = None
    contadorReseñas = 0          

    for id_libro, libro, usuario, titulo, reseña in reseñas:
        if id_libro != libroActual:
            if libroActual is not None:                                    
                pdf.set_font("Arial", "I", 10)                             
                pdf.cell(0, 6, f"Total de reseñas: {contadorReseñas}", ln=True)  
            libroActual = id_libro
            contadorReseñas = 0   
            pdf.ln(3)
            pdf.set_font("Arial", "B", 13)
            pdf.cell(0, 8, f"Libro: {libro}  (Codigo: {id_libro})", ln=True)
            pdf.cell(0, 0, "", border="T")
            pdf.ln(4)

        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 7,
            f"Usuario: {usuario}\n"
            f"Titulo: {titulo}\n"
            f"Reseña: {reseña}"
        )
        pdf.ln(3)
        contadorReseñas += 1     

    
    pdf.set_font("Arial", "I", 10)
    pdf.cell(0, 6, f"Total de reseñas: {contadorReseñas}", ln=True)

    archivoRuta = os.path.join(ruta, "reporte_reseñas.pdf")
    pdf.output(archivoRuta)
    print(f"\n\t...¡Archivo generado en: {os.path.abspath(archivoRuta)}!...")
    return True

def ValidarGmail(correo):
    PATRON = r'^[\w,+-]+@gmail\.com$'
    return re.match(PATRON, correo) is not None