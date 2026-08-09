'''
Crear un proyecto que permita gestionar (administrar) peliculas. Colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar, Buscar, Limpiar una lista de peliculas.

Notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas
3.- Utilizar o implementar BD relacional con MySQL para guardar la información

'''
import peliculas

movies=[]

answ=""

while answ !="7":
    peliculas.clearScrean()
    answ=peliculas.mainMenu()
    match answ:
        case"1":
            peliculas.clearScrean()
            peliculas.addMovies(movies)
        case"2":
            peliculas.clearScrean()
            peliculas.cleanMovies(movies)
        case"3":
            peliculas.clearScrean()
            peliculas.editMovies(movies)
        case"4":
            peliculas.clearScrean()
            peliculas.showMovies(movies)
        case"5":
            peliculas.clearScrean()
            peliculas.searchMovies(movies)
        case"6":
            peliculas.clearScrean()
            peliculas.erasedMovies(movies)
        case"7":
            peliculas.clearScrean()
            peliculas.endSystem()
        case _:
            peliculas.invalidOption()

