import funciones
from libros import crudLi
from usuarios import crudUs
from reseñas import crudRe


def menuPrincReseñas():
    print(r"""
 ____  _____ ____  _____ _ ~ _    _    ____  
|  _ \| ____/ ___|| ____| \ | |  / \  / ___| 
| |_) |  _| \___ \|  _| |  \| | / _ \ \___ \ 
|  _ <| |___ ___) | |___| |\  |/ ___ \ ___) |
|_| \_\_____|____/|_____|_| \_/_/   \_\____/ 
                                             
Ｒｅｓｅñａｓ ｄｅ ｕｓｕａｒｉｏｓ
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



def agregarReseña(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: ⭐ AGREGAR RESEÑA ::::...\n")
    libro = input("📖 Introduce el libro a reseñar: ").upper().strip()
    libros = crudLi.buscar(libro, conexionBD)
    if len(libros) == 0:
        input("⚠️  ...¡No se encontró el libro que estás buscando!...")
        funciones.espereTecla()
        return

    print("\t🆔 Codigo\t📖 Libro\t✍️ Autor\t🏷️ Genero\t📊 Clasificacion\t🌎 Origen\n")
    for i in libros:
        print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")

    nombreUsuario = input("\n👤 Introducir tu nombre de usuario: ").upper().strip()
    usuarios = crudUs.buscar(nombreUsuario, conexionBD)
    if len(usuarios) == 0:
        input("⚠️  ...¡Ese usuario no está registrado, regístralo primero en el menú de Usuarios!...")
        funciones.espereTecla()
        return

    titulo = input("📝 Escribe el título de tu reseña: ").strip()
    reseña = input("💬 Escribe tu reseña: ").strip()
    id_libro = libros[0][0]
    id_usuario = usuarios[0][0]

    respuesta = crudRe.insertar(id_libro, id_usuario, titulo, reseña, conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()
    funciones.espereTecla()


def mostrarReseñas(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: 📋 MOSTRAR RESEÑAS ::::...\n")
    reseñas = crudRe.consultar(conexionBD)
    if len(reseñas) > 0:
        print("\t🆔 Codigo\t📖 Libro\t\t👤 Usuarios\n")
        for i in reseñas:
            print(f"\t{i[0]}\t{i[1]}\t\t{i[2]}")
    else:
        input("⚠️  ...¡No hay reseñas que mostrar!...")
    funciones.espereTecla()


def seleccionarReseña(conexionBD):
    funciones.borrarPantalla()
    libro = input("📖 Escribir el nombre del libro: ").upper().strip()
    libros = crudLi.buscar(libro, conexionBD)
    if len(libros) == 0:
        input("⚠️  ...¡No se encontró el libro que estás buscando!...")
        return None

    id_libro = libros[0][0]
    reseñas = crudRe.buscarPorLibro(id_libro, conexionBD)
    if len(reseñas) == 0:
        input("⚠️  ...¡Ese libro no tiene reseñas!...")
        return None

    print(f"\n\t⭐ Reseñas de: {libros[0][1]}\n")
    print("\t🆔 ID\t📝 Titulo\t\t👤 Usuario\n")
    for i in reseñas:
        print(f"\t{i[0]}\t{i[1]}\t\t{i[2]}")

    return input("\n🔎 Escribe el ID de la reseña: ").strip()


def buscarReseña(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: 🔍 BUSCAR RESEÑA ::::...\n")
    id_reseña = seleccionarReseña(conexionBD)
    if id_reseña:
        reseña = crudRe.buscarPorId(id_reseña, conexionBD)
        if len(reseña) > 0:
            i = reseña[0]
            print(f"\n\t🆔 ID: {i[0]}\n\t📖 Libro: {i[4]}\n\t👤 Usuario: {i[3]}\n\t📝 Titulo: {i[1]}\n\t💬 Reseña: {i[2]}")
        else:
            input("⚠️  ...¡No se encontró esa reseña!...")
    funciones.espereTecla()


def modificarReseña(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: ✏️  MODIFICAR RESEÑA ::::...\n")
    id_reseña = seleccionarReseña(conexionBD)
    if id_reseña:
        reseña = crudRe.buscarPorId(id_reseña, conexionBD)
        if len(reseña) > 0:
            i = reseña[0]
            print(f"\n\t🆔 ID: {i[0]}\n\t📖 Libro: {i[4]}\n\t👤 Usuario: {i[3]}\n\t📝 Titulo: {i[1]}\n\t💬 Reseña: {i[2]}")
            opc = ""
            while opc != "si" and opc != "no":
                opc = input("❓ ¿Deseas modificar esta reseña (Si/No)? ").lower().strip()
            if opc == "si":
                titulo = input("📝 Introducir el nuevo título: ").strip()
                nuevaReseña = input("💬 Introducir la nueva reseña: ").strip()
                respuesta = crudRe.actualizar(id_reseña, titulo, nuevaReseña, conexionBD)
                if respuesta:
                    funciones.accionExitosa()
                else:
                    funciones.accionNoExitosa()
        else:
            input("⚠️  ...¡No se encontró esa reseña!...")
    funciones.espereTecla()


def borrarReseña(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: 🗑️  BORRAR RESEÑA ::::...\n")
    id_reseña = seleccionarReseña(conexionBD)
    if id_reseña:
        reseña = crudRe.buscarPorId(id_reseña, conexionBD)
        if len(reseña) > 0:
            i = reseña[0]
            print(f"\n\t🆔 ID: {i[0]}\n\t📖 Libro: {i[4]}\n\t👤 Usuario: {i[3]}\n\t📝 Titulo: {i[1]}\n\t💬 Reseña: {i[2]}")
            opc = ""
            while opc != "si" and opc != "no":
                opc = input("❓ ¿Deseas borrar esta reseña (Si/No)? ").lower().strip()
            if opc == "si":
                respuesta = crudRe.borrar(id_reseña, conexionBD)
                if respuesta:
                    funciones.accionExitosa()
                else:
                    funciones.accionNoExitosa()
        else:
            input("⚠️  ...¡No se encontró esa reseña!...")
    funciones.espereTecla()


def limpiarReseñas(conexionBD):
    funciones.borrarPantalla()
    reseñas = crudRe.consultar(conexionBD)
    if len(reseñas) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("❓ ¿Deseas borrar TODAS las reseñas (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crudRe.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("⚠️  ...¡No hay reseñas que borrar!...")
    funciones.espereTecla()


def menuReseñas(conexionBD):
    opc = ""
    while opc != "7":
        funciones.borrarPantalla()
        opc = menuPrincReseñas()
        match opc:
            case "1":
                agregarReseña(conexionBD)
            case "2":
                borrarReseña(conexionBD)
            case "3":
                modificarReseña(conexionBD)
            case "4":
                mostrarReseñas(conexionBD)
            case "5":
                buscarReseña(conexionBD)
            case "6":
                limpiarReseñas(conexionBD)
            case "7":
                exportarReseñas(conexionBD)
            case "8":
                funciones.borrarPantalla()
                return
            case _:
                funciones.opcionInvalida()


def exportarReseñas(conexionBD):
    funciones.borrarPantalla()
    print("\n\t\t...:::: 📄 EXPORTAR RESEÑAS DE LIBROS A PDF ::::...\n")
    print("....::::📤 Los datos ingresados de los libros se exportarán a PDF::::....")
    reseñas = crudRe.consultar(conexionBD)
    if len(reseñas) > 0:
        respuesta = funciones.exportReseñasPdf(conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    else:
        input("⚠️  ...¡No hay reseñas de libros que exportar!...")
    funciones.espereTecla()