import funciones
from usuarios import crudUs


def menuPrincUsuario():
    print(r"""
 _   _ ____  _   _   _    ____  ___ ___  ____  
| | | / ___|| | | | / \  |  _ \|_ _/ _ \/ ___| 
| | | \___ \| | | |/ _ \ | |_) || | | | \___ \ 
| |_| |___) | |_| / ___ \|  _ < | | |_| |___) |
 \___/|____/ \___/_/   \_\_| \_\___\___/|____/ 
                                               
Ｇｅｓｔｉóｎ ｄｅ ｕｓｕａｒｉｏｓ
""")
    opcion = input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion


def agregarUsuario(conexionBD):
    print("\n\t\t...:::: AGREGAR USUARIO ::::...\n")
    usuario = input("Introducir el nombre de usuario: ").upper().strip()
    correo=input("Introducir el correo(Gmail): ").lower().strip()
    while not funciones.ValidarGmail(correo):
        input("\t\t...Correo invalido, debe de ser un correo @gmail.com...")
        correo=input("Introducir el correo(Gmail): ")
    respuesta = crudUs.insertar(usuario,correo, conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()
    funciones.espereTecla()


def mostrarUsuarios(conexionBD):
    print("\n\t\t...:::: MOSTRAR USUARIOS ::::...\n")
    usuarios = crudUs.consultar(conexionBD)
    if len(usuarios) > 0:
        print("\tCodigo\t\tUsuario\n")
        for i in usuarios:
            print(f"\t{i[0]}\t\t{i[1]}")
    else:
        input("...¡No hay usuarios que mostrar!...")
    funciones.espereTecla()


def buscarUsuario(conexionBD):
    print("\n\t\t...:::: BUSCAR USUARIO ::::...\n")
    usuario = int(input("Escribir el nombre del usuario: ")).strip()
    usuarios = crudUs.buscar(usuario, conexionBD)
    if len(usuarios) > 0:
        print("\tCodigo\t\tUsuario\n")
        for i in usuarios:
            print(f"\t{i[0]}\t\t{i[1]}")
    else:
        input("...¡No se encontro el usuario que estas buscando!...")
    funciones.espereTecla()


def borrarUsuario(conexionBD):
    print("\n\t\t...:::: BORRAR USUARIO ::::...\n")
    usuario = input("Escribir el nombre del usuario: ").upper().strip()
    usuarios = crudUs.buscar(usuario, conexionBD)
    if len(usuarios) > 0:
        print("\tCodigo\t\tUsuario\n")
        for i in usuarios:
            print(f"\t{i[0]}\t\t{i[1]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar al usuario (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crudUs.borrar(usuario, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No se encontro el usuario que estas buscando!...")
    funciones.espereTecla()


def modificarUsuario(conexionBD):
    print("\n\t\t...:::: MODIFICAR USUARIO ::::...\n")
    usuario = input("Escribir el nombre del usuario: ").upper().strip()
    usuarios = crudUs.buscar(usuario, conexionBD)
    if len(usuarios) > 0:
        print("\tCodigo\t\tUsuario\n")
        for i in usuarios:
            print(f"\t{i[0]}\t\t{i[1]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas modificar al usuario (Si/No)? ").lower().strip()
        if opc == "si":
            usuario2 = input("Escribir el nuevo nombre del usuario: ").upper().strip()
            respuesta = crudUs.actualizar(usuario, usuario2, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No se encontro el usuario que estas buscando!...")
    funciones.espereTecla()


def limpiarUsuarios(conexionBD):
    usuarios = crudUs.consultar(conexionBD)
    if len(usuarios) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar TODOS los usuarios (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crudUs.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay usuarios que borrar!...")
    funciones.espereTecla()


def menuUsuario(conexionBD):
    opc = ""
    while opc != "7":
        funciones.borrarPantalla()
        opc = menuPrincUsuario()
        match opc:
            case "1":
                agregarUsuario(conexionBD)
            case "2":
                borrarUsuario(conexionBD)
            case "3":
                modificarUsuario(conexionBD)
            case "4":
                mostrarUsuarios(conexionBD)
            case "5":
                buscarUsuario(conexionBD)
            case "6":
                limpiarUsuarios(conexionBD)
            case "7":
                funciones.borrarPantalla()
                return
            case _:
                funciones.opcionInvalida()