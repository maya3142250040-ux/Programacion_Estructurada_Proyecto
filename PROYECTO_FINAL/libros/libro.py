import funciones
from libros import crudLi

def menuPrincialLibros():
    print(r"""
 _     ___ ____  ____   ___  ____  
| |   |_ _| __ )|  _ \ / _ \/ ___| 
| |    | ||  _ \| |_) | | | \___ \ 
| |___ | || |_) |  _ <| |_| |___) |
|_____|___|____/|_| \_\\___/|____/ 
                                   
Ｇｅｓｔｉｏｎ ｄｅ Ｌｉｂｒｏｓ
    """)

    opcion = input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Exportar Datos a Pdf\n\t8.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion


def agregarLibros(conexionBD):
    print("\n\t\t...:::: AGREGAR PELICULAS ::::...\n")
    libro = input("Introducir el nombre del libro: ").upper().strip()
    autor = input("Introducir el autor: ").upper().strip()
    genero = input("Introducir el genero: ").upper().strip()
    clasificacion = input("Introducir la clasificacion: ").upper().strip()
    origen = input("Introducir el pais de origen: ").upper().strip()
    respuesta = crudLi.insertar(libro,autor,genero,clasificacion,origen,conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()


def mostrarLibros(conexionBD):
    print("\n\t\t...:::: MOSTRAR LIBROS ::::...\n")
    libros = crudLi.consultar(conexionBD)
    if len(libros) > 0:
        print("\tCodigo\tLibro\tAutor\tGenero\tClasificacion\tOrigen\n")
        for i in libros:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
    else:
        input("...¡No hay libros que mostrar!...")
    funciones.espereTecla()


def limpiarLibros(conexionBD):
    libros = crudLi.consultar(conexionBD)
    if len(libros) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar TODOS los libros (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crudLi.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay libros que borrar!...")
    funciones.espereTecla()


def buscarLibros(conexionBD):
    print("\n\t\t...:::: BUSCAR Libros ::::...\n")
    libro = input("Escribir el nombre del Libro: ").upper().strip()
    libros = crudLi.buscar(libro, conexionBD)
    if len(libros) > 0:
        print("\tCodigo\tLibro\tAutor\tGenero\tClasificacion\tOrigen\n")
        for i in libros:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
    else:
        input("...¡No se encontro el libro que estas buscando!...")
    funciones.espereTecla()


def borrarLibros(conexionBD):
    print("\n\t\t...:::: BORRAR LIBROS ::::...\n")
    libro = input("Escribir el nombre del Libro: ").upper().strip()
    libros = crudLi.buscar(nombre, conexionBD)
    if len(pelis) > 0:
        print("\tCodigo\tLibro\tAutor\tGenero\tClasificacion\tOrigen\n")
        for i in pelis:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar el libro (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crudLi.borrar(libro, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No se encontro el libro que estas buscando!...")
    funciones.espereTecla()


def modificarLibros(conexionBD):
    print("\n\t\t...:::: MODIFICAR LIBROS ::::...\n")
    libro_old = input("Escribir el nombre del libro: ").upper().strip()
    libros = crudLi.buscar(libro_old, conexionBD)
    if len(libros) > 0:
        print("\tCodigo\tLibro\tAutor\tGenero\tClasificacion\tOrigen\n")
        for i in libros:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas modificar el libro (Si/No)? ").lower().strip()
        if opc == "si":
            libro = input("Introducir el nombre del libro: ").upper().strip()
            autor = input("Introducir el autor: ").upper().strip()
            genero = input("Introducir el genero: ").upper().strip()
            clasificacion = input("Introducir la clasificacion: ").upper().strip()
            origen = input("Introducir el pais de origen: ").upper().strip()
            respuesta = crudLi.actualizar(libro_old, libro, autor, genero, clasificacion, origen, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No se encontro el libro que estas buscando!...")
    funciones.espereTecla()

def menuLibros(conexionBD):
    opc = ""
    while opc != "8":
        funciones.borrarPantalla()
        opc = menuPrincialLibros()
        match opc:
            case "1":
                agregarLibros(conexionBD)
            case "2":
                borrarLibros(conexionBD)
            case "3":
                modificarLibros(conexionBD)
            case "4":
                mostrarLibros(conexionBD)
            case "5":
                buscarLibros(conexionBD)
            case "6":
                limpiarLibros(conexionBD)
            case "7":
                exportarLibros(conexionBD)
            case "8":
                funciones.borrarPantalla()
                return
            case _:
                funciones.opcionInvalida()

def exportarLibros(conexionBD):
    print("\n\t\t...:::: EXPORTAR LIBROS A PDF ::::...\n")
    print("....::::Los datos ingresados de los libros se exportaran a pdf::::....")
    libros = crudLi.consultar(conexionBD)
    if len(libros) > 0:
        respuesta = funciones.exportLibrosPdf(conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    else:
        input("...¡No hay libros que exportar!...")
    funciones.espereTecla()