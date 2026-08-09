import funciones
from peliculas import crud

def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion = input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion


def agregarPeliculas(conexionBD):
    print("\n\t\t...:::: AGREGAR PELICULAS ::::...\n")
    nombre = input("Introducir el nombre de la pelicula: ").upper().strip()
    categoria = input("Introducir la categoria: ").upper().strip()
    clasificacion = input("Introducir la clasificacion: ").upper().strip()
    genero = input("Introducir el genero: ").upper().strip()
    idioma = input("Introducir el idioma: ").upper().strip()
    respuesta = crud.insertar(nombre, categoria, clasificacion, genero, idioma, conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()


def mostrarPeliculas(conexionBD):
    print("\n\t\t...:::: MOSTRAR PELICULAS ::::...\n")
    pelis = crud.consultar(conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\tNombre\tCategoria\tClasificacion\tGenero\tIdioma\n")
        for i in pelis:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
    else:
        input("...¡No hay peliculas que mostrar!...")
    funciones.espereTecla()


def limpiarPeliculas(conexionBD):
    pelis = crud.consultar(conexionBD)
    if len(pelis) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crud.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay peliculas que borrar!...")
    funciones.espereTecla()


def buscarPeliculas(conexionBD):
    print("\n\t\t...:::: BUSCAR PELICULAS ::::...\n")
    nombre = input("Escribir el nombre de la pelicula: ").upper().strip()
    pelis = crud.buscar(nombre, conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\tNombre\tCategoria\tClasificacion\tGenero\tIdioma\n")
        for i in pelis:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
    else:
        input("...¡No se encontro la pelicula que estas buscando!...")
    funciones.espereTecla()


def borrarPeliculas(conexionBD):
    print("\n\t\t...:::: BORRAR PELICULAS ::::...\n")
    nombre = input("Escribir el nombre de la pelicula: ").upper().strip()
    pelis = crud.buscar(nombre, conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\tNombre\tCategoria\tClasificacion\tGenero\tIdioma\n")
        for i in pelis:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crud.borrar(nombre, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No se encontro la pelicula que estas buscando!...")
    funciones.espereTecla()


def modificarPeliculas(conexionBD):
    print("\n\t\t...:::: MODIFICAR PELICULAS ::::...\n")
    nombre_old = input("Escribir el nombre de la pelicula: ").upper().strip()
    pelis = crud.buscar(nombre_old, conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\tNombre\tCategoria\tClasificacion\tGenero\tIdioma\n")
        for i in pelis:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas modificar la pelicula (Si/No)? ").lower().strip()
        if opc == "si":
            nombre = input("Nuevo nombre de la pelicula: ").upper().strip()
            categoria = input("Nueva categoria: ").upper().strip()
            clasificacion = input("Nueva clasificacion: ").upper().strip()
            genero = input("Nuevo genero: ").upper().strip()
            idioma = input("Nuevo idioma: ").upper().strip()
            respuesta = crud.actualizar(nombre_old, nombre, categoria, clasificacion, genero, idioma, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No se encontro la pelicula que estas buscando!...")
    funciones.espereTecla()


def menuPeliculas(conexionBD):
    opc = ""
    while opc != "7":
        funciones.borrarPantalla()
        opc = menuPrincial()
        match opc:
            case "1":
                agregarPeliculas(conexionBD)
            case "2":
                borrarPeliculas(conexionBD)
            case "3":
                modificarPeliculas(conexionBD)
            case "4":
                mostrarPeliculas(conexionBD)
            case "5":
                buscarPeliculas(conexionBD)
            case "6":
                limpiarPeliculas(conexionBD)
            case "7":
                funciones.borrarPantalla()
                return
            case _:
                funciones.opcionInvalida()