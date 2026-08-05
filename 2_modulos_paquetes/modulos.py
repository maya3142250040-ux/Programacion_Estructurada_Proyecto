# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

def borrarPantalla():
    print("\033c")

def funcion1():
    nombre=input("Nombre: ").upper().strip()
    apellidos=input("Apellidos:").upper().strip()
    print(f'El nombre del alumno es {nombre} {apellidos}')

def funcion3(nom,ape):
    nombre=nom
    apellidos=ape
    print(f'El nombre del alumno es {nombre} {apellidos}')

def funcion2():
    nombre=input("Nombre: ").upper().strip()
    apellidos=input("Apellidos:").upper().strip()
    return nombre,apellidos

def funcion4(nom,ape):
    nombre=nom
    apellidos=ape
    return nombre,apellidos


