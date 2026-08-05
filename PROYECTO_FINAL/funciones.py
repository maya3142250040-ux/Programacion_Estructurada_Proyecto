import mysql.connector

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