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
            database="bd_peliculas"
        )
        return conexion
    except Exception as e:
        print("ERROR DE CONEXION:", e)
        return None

def menuPrincipal():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Películas")
    print("2. Actores")
    print("3. Salir")
    return input("Elige una opción: ")