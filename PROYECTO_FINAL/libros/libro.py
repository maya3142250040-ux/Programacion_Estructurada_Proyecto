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
    opcion = input(
        "\n    ╔══════════════════════════════╗"
        "\n    ║      📋 MENÚ PRINCIPAL 📋    ║"
        "\n    ╚══════════════════════════════╝"
        "\n"
        "\n           1.- ➕ Agregar"
        "\n    ──────────────────────────────"
        "\n           2.- 🗑️  Borrar"
        "\n    ──────────────────────────────"
        "\n           3.- ✏️  Modificar"
        "\n    ──────────────────────────────"
        "\n           4.- 📄 Mostrar"
        "\n    ──────────────────────────────"
        "\n           5.- 🔍 Buscar"
        "\n    ──────────────────────────────"
        "\n           6.- 🧹 Limpiar"
        "\n    ──────────────────────────────"
        "\n           7.-📂 Exportar a PDF "
        "\n    ──────────────────────────────"
        "\n           8.- 🚪 Salir"
        "\n    ──────────────────────────────"
        "\n                         Escribe una opción: "
    ).strip()
    return opcion


def agregarLibros(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: 📚 AGREGAR LIBRO ::::...\n")
    libro = input("📖 Introducir el nombre del libro: ").upper().strip()
    autor = input("✍️  Introducir el autor: ").upper().strip()
    genero = input("🏷️  Introducir el genero: ").upper().strip()
    clasificacion = input("📊 Introducir la clasificacion: ").upper().strip()
    origen = input("🌎 Introducir el pais de origen: ").upper().strip()
    respuesta = crudLi.insertar(libro,autor,genero,clasificacion,origen,conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()


def mostrarLibros(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: 📋 MOSTRAR LIBROS ::::...\n")
    libros = crudLi.consultar(conexionBD)
    if len(libros) > 0:
        print("\t🆔 Codigo\t📖 Libro\t✍️ Autor\t🏷️ Genero\t📊 Clasificacion\t🌎 Origen\n")
        for i in libros:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
    else:
        input("⚠️  ...¡No hay libros que mostrar!...")
    funciones.espereTecla()


def limpiarLibros(conexionBD):
    funciones.borrarPantalla()
    libros = crudLi.consultar(conexionBD)
    if len(libros) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("❓ ¿Deseas borrar TODOS los libros (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crudLi.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("⚠️  ...¡No hay libros que borrar!...")
    funciones.espereTecla()


def buscarLibros(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: 🔍 BUSCAR LIBROS ::::...\n")
    libro = input("✏️  Escribir el nombre del Libro: ").upper().strip()
    libros = crudLi.buscar(libro, conexionBD)
    if len(libros) > 0:
        print("\t🆔 Codigo\t📖 Libro\t✍️ Autor\t🏷️ Genero\t📊 Clasificacion\t🌎 Origen\n")
        for i in libros:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
    else:
        input("⚠️  ...¡No se encontró el libro que estás buscando!...")
    funciones.espereTecla()


def borrarLibros(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: 🗑️  BORRAR LIBROS ::::...\n")
    libro = input("✏️  Escribir el nombre del Libro: ").upper().strip()
    libros = crudLi.buscar(libro, conexionBD)
    if len(libros) > 0:
        print("\t🆔 Codigo\t📖 Libro\t✍️ Autor\t🏷️ Genero\t📊 Clasificacion\t🌎 Origen\n")
        for i in libros:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("❓ ¿Deseas borrar el libro (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crudLi.borrar(libro, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("⚠️  ...¡No se encontró el libro que estás buscando!...")
    funciones.espereTecla()


def modificarLibros(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: ✏️  MODIFICAR LIBROS ::::...\n")
    libro_old = input("✏️  Escribir el nombre del libro: ").upper().strip()
    libros = crudLi.buscar(libro_old, conexionBD)
    if len(libros) > 0:
        print("\t🆔 Codigo\t📖 Libro\t✍️ Autor\t🏷️ Genero\t📊 Clasificacion\t🌎 Origen\n")
        for i in libros:
            print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("❓ ¿Deseas modificar el libro (Si/No)? ").lower().strip()
        if opc == "si":
            libro = input("📖 Introducir el nombre del libro: ").upper().strip()
            autor = input("✍️  Introducir el autor: ").upper().strip()
            genero = input("🏷️  Introducir el genero: ").upper().strip()
            clasificacion = input("📊 Introducir la clasificacion: ").upper().strip()
            origen = input("🌎 Introducir el pais de origen: ").upper().strip()
            respuesta = crudLi.actualizar(libro_old, libro, autor, genero, clasificacion, origen, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("⚠️  ...¡No se encontró el libro que estás buscando!...")
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
    funciones.borrarPantalla()
    print("\n\t\t...:::: 📄 EXPORTAR LIBROS A PDF ::::...\n")
    print("....::::📤 Los datos ingresados de los libros se exportarán a PDF::::....")
    libros = crudLi.consultar(conexionBD)
    if len(libros) > 0:
        respuesta = funciones.exportLibrosPdf(conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    else:
        input("⚠️  ...¡No hay libros que exportar!...")
    funciones.espereTecla()