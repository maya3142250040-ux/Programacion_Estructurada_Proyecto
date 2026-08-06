import mysql.connector
from fpdf import FPDF
import os
import re

def borrarPantalla():
    print("\033c")
    
def espereTecla():
    input("\n\t...¡Oprima cualquier tecla para continuar!...")
    
def opcionInvalida():
    input("\n\t...¡Opcion invalidad, por favor verifique !...")
    
def accionExitosa():
    input("\n\t...¡Accion Realizada con Exito !...")

def accionNoExitosa():
    input("\n\t...¡No fue posible realiazr esta accion !...")

def terminarSistema():
    input("\n\t\t...:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA ::::...\n")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bookso"
        )
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
    print("=== MENÚ PRINCIPAL ===")
    print("1. Libros")
    print("2. Usuarios")
    print("3. Reseñas")
    print("4. Salir")
    return input("Elige una opción: ")

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

def ValidarGmail(conexionBD):
    patron = r'^[\w,+-]+@gmail\.com$'
    return re.match(patron, correo) is not None