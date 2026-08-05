import funciones
from peliculas import peliculas
from actores import actor

conexionBD = funciones.conectar()

opc = ""
while opc != "3":
    funciones.borrarPantalla()
    
    opc = funciones.menuPrincipal()
    match opc:
        case "1":
            peliculas.menuPeliculas(conexionBD)
        case "2":
            actor.menuActor(conexionBD)
        case "3":
            funciones.borrarPantalla()
            funciones.terminarSistema()
        case _:
            funciones.opcionInvalida()