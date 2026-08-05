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
    opcion = input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion


def agregarReseña(conexionBD):
    print("\n\t\t...:::: AGREGAR RESEÑA ::::...\n")
    libro = input("Introduce el libro a reseñar: ").upper().strip()
    libros = crudLi.buscar(libro, conexionBD)
    if len(libros) == 0:
        input("...¡No se encontro el libro que estas buscando!...")
        funciones.espereTecla()
        return

    print("\tCodigo\tLibro\tAutor\tGenero\tClasificacion\tOrigen\n")
    for i in libros:
        print(f"\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")

    nombreUsuario = input("\nIntroducir tu nombre de usuario: ").upper().strip()
    usuarios = crudUs.buscar(nombreUsuario, conexionBD)
    if len(usuarios) == 0:
        input("...¡Ese usuario no esta registrado, registralo primero en el menu de Usuarios!...")
        funciones.espereTecla()
        return

    titulo = input("Escribe el titulo de tu reseña: ").strip()
    reseña = input("Escribe tu reseña: ").strip()
    id_libro = libros[0][0]
    id_usuario = usuarios[0][0]

    respuesta = crudRe.insertar(id_libro, id_usuario, titulo, reseña, conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()
    funciones.espereTecla()


def mostrarReseñas(conexionBD):
    print("\n\t\t...:::: MOSTRAR RESEÑAS ::::...\n")
    reseñas = crudRe.consultar(conexionBD)
    if len(reseñas) > 0:
        print("\tCodigo\tLibro\t\tUsuarios\n")
        for i in reseñas:
            print(f"\t{i[0]}\t{i[1]}\t\t{i[2]}")
    else:
        input("...¡No hay reseñas que mostrar!...")
    funciones.espereTecla()


def seleccionarReseña(conexionBD):
    """Busca un libro, muestra la lista de reseñas de ese libro y
    regresa el id de la reseña elegida por el usuario (o None)."""
    libro = input("Escribir el nombre del libro: ").upper().strip()
    libros = crudLi.buscar(libro, conexionBD)
    if len(libros) == 0:
        input("...¡No se encontro el libro que estas buscando!...")
        return None

    id_libro = libros[0][0]
    reseñas = crudRe.buscarPorLibro(id_libro, conexionBD)
    if len(reseñas) == 0:
        input("...¡Ese libro no tiene reseñas!...")
        return None

    print(f"\n\tReseñas de: {libros[0][1]}\n")
    print("\tID\tTitulo\t\tUsuario\n")
    for i in reseñas:
        print(f"\t{i[0]}\t{i[1]}\t\t{i[2]}")

    return input("\nEscribe el ID de la reseña: ").strip()


def buscarReseña(conexionBD):
    print("\n\t\t...:::: BUSCAR RESEÑA ::::...\n")
    id_reseña = seleccionarReseña(conexionBD)
    if id_reseña:
        reseña = crudRe.buscarPorId(id_reseña, conexionBD)
        if len(reseña) > 0:
            i = reseña[0]
            print(f"\n\tID: {i[0]}\n\tLibro: {i[4]}\n\tUsuario: {i[3]}\n\tTitulo: {i[1]}\n\tReseña: {i[2]}")
        else:
            input("...¡No se encontro esa reseña!...")
    funciones.espereTecla()


def modificarReseña(conexionBD):
    print("\n\t\t...:::: MODIFICAR RESEÑA ::::...\n")
    id_reseña = seleccionarReseña(conexionBD)
    if id_reseña:
        reseña = crudRe.buscarPorId(id_reseña, conexionBD)
        if len(reseña) > 0:
            i = reseña[0]
            print(f"\n\tID: {i[0]}\n\tLibro: {i[4]}\n\tUsuario: {i[3]}\n\tTitulo: {i[1]}\n\tReseña: {i[2]}")
            opc = ""
            while opc != "si" and opc != "no":
                opc = input("¿Deseas modificar esta reseña (Si/No)? ").lower().strip()
            if opc == "si":
                titulo = input("Introducir el nuevo titulo: ").strip()
                nuevaReseña = input("Introducir la nueva reseña: ").strip()
                respuesta = crudRe.actualizar(id_reseña, titulo, nuevaReseña, conexionBD)
                if respuesta:
                    funciones.accionExitosa()
                else:
                    funciones.accionNoExitosa()
        else:
            input("...¡No se encontro esa reseña!...")
    funciones.espereTecla()


def borrarReseña(conexionBD):
    print("\n\t\t...:::: BORRAR RESEÑA ::::...\n")
    id_reseña = seleccionarReseña(conexionBD)
    if id_resena:
        reseña = crudRe.buscarPorId(id_reseña, conexionBD)
        if len(reseña) > 0:
            i = reseña[0]
            print(f"\n\tID: {i[0]}\n\tLibro: {i[4]}\n\tUsuario: {i[3]}\n\tTitulo: {i[1]}\n\tReseña: {i[2]}")
            opc = ""
            while opc != "si" and opc != "no":
                opc = input("¿Deseas borrar esta reseña (Si/No)? ").lower().strip()
            if opc == "si":
                respuesta = crudRe.borrar(id_reseña, conexionBD)
                if respuesta:
                    funciones.accionExitosa()
                else:
                    funciones.accionNoExitosa()
        else:
            input("...¡No se encontro esa reseña!...")
    funciones.espereTecla()


def limpiarReseñas(conexionBD):
    reseñas = crudRe.consultar(conexionBD)
    if len(reseñas) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar TODAS las reseñas (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crudRe.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay reseñas que borrar!...")
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
                funciones.borrarPantalla()
                return
            case _:
                funciones.opcionInvalida()