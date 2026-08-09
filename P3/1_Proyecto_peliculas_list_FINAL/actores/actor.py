import funciones
from actores import crudAct

def menuPrincActor():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion = input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion


def agregarActores(conexionBD):
    print("\n\t\t...:::: AGREGAR ACTORES ::::...\n")
    nombre = input("Introducir el nombre del actor: ").upper().strip()
    respuesta = crudAct.insertar(nombre, conexionBD)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()


def mostrarActores(conexionBD):
    print("\n\t\t...:::: MOSTRAR ACTORES ::::...\n")
    actores = crudAct.consultar(conexionBD)
    if len(actores) > 0:
        print("\tCodigo\t\tActores\n")
        for i in actores:
            print(f"\t{i[0]}\t\t{i[1]}")
    else:
        input("...¡No hay Actores que mostrar!...")
    funciones.espereTecla()


def limpiarActores(conexionBD):
    actores = crudAct.consultar(conexionBD)
    if len(actores) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar TODOS los actores (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crudAct.vaciar(conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No hay actores que borrar!...")
    funciones.espereTecla()


def buscarActores(conexionBD):
    print("\n\t\t...:::: BUSCAR ACTORES ::::...\n")
    nombre = input("Escribir el nombre del actor: ").upper().strip()
    actores = crudAct.buscar(nombre, conexionBD)
    if len(actores) > 0:
        print("\tCodigo\t\tActores\n")
        for i in actores:
            print(f"\t{i[0]}\t\t{i[1]}")
    else:
        input("...¡No se encontraron los actores que estas buscando!...")
    funciones.espereTecla()


def borrarActores(conexionBD):
    print("\n\t\t...:::: BORRAR ACTORES ::::...\n")
    actor = input("Escribir el nombre del actor: ").upper().strip()
    actores = crudAct.buscar(actor, conexionBD)
    if len(actores) > 0:
        print("\tCodigo\t\tActores\n")
        for i in actores:
            print(f"\t{i[0]}\t\t{i[1]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar al actor (Si/No)? ").lower().strip()
        if opc == "si":
            respuesta = crudAct.borrar(actor, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No se encontro el actor que estas buscando!...")
    funciones.espereTecla()


def modificarActores(conexionBD):
    print("\n\t\t...:::: MODIFICAR ACTOR ::::...\n")
    actor = input("Escribir el nombre del actor: ").upper().strip()
    actores = crudAct.buscar(actor, conexionBD)
    if len(actores) > 0:
        print("\tCodigo\t\tActores\n")
        for i in actores:
            print(f"\t{i[0]}\t\t{i[1]}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas modificar al actor (Si/No)? ").lower().strip()
        if opc == "si":
            actor2 = input("Escribir el nuevo nombre del actor: ").upper().strip()
            respuesta = crudAct.actualizar(actor, actor2, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
    else:
        input("...¡No se encontro el actor que estas buscando!...")
    funciones.espereTecla()


def menuActor(conexionBD):
    opc = ""
    while opc != "7":
        funciones.borrarPantalla()
        opc = menuPrincActor()
        match opc:
            case "1":
                agregarActores(conexionBD)
            case "2":
                borrarActores(conexionBD)
            case "3":
                modificarActores(conexionBD)
            case "4":
                mostrarActores(conexionBD)
            case "5":
                buscarActores(conexionBD)
            case "6":
                limpiarActores(conexionBD)
            case "7":
                funciones.borrarPantalla()
                return
            case _:
                funciones.opcionInvalida()