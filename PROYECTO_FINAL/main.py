import funciones
from libros import libro
from usuarios import usuario
from reseñas import reseña

conexionBD = funciones.conectar()

opc = ""
while opc != "4":
    funciones.borrarPantalla()
    opc = funciones.menuPrincipal()
    match opc:
        case "1":
            libro.menuLibros(conexionBD)
        case "2":
            usuario.menuUsuario(conexionBD)
        case "3":
            reseña.menuReseñas(conexionBD)
        case "4":
            funciones.borrarPantalla()
            funciones.terminarSistema()
        case _:
            funciones.opcionInvalida()