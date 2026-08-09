def clearScrean():
    print("\033c")

def waiting():
    input("\n\t...¡Oprima una telca para continuar!...")

def invalidOption():
    input("\n\t...¡Opcion invalida\n Porfavor verifique!...")
    
def missionCompleted():
    input("\n\t...¡Accion realizada con exito, que elegante !...")

def endSystem():
    print("\nt......:::¡GRACIAS POR USAR NUESTRO SISTEMA!:::......")

def mainMenu():
    print("\nt......:::¡M E N U  P R I N C I P A L!:::......")
    option=input("\n\t1.-Agregar\n\t2.-Borrar\n\t3.-Modificar\n\t4.-Mostrar\n\t5.-Buscar\n\t6.-Limpiar\n\t7.-Salir\n\tEscribe una opcion: ").strip()
    return option

def addMovies(movies):
    print("\nt......:::¡AGREGAR PELICULAS!:::......\n")
    movie=input("Introduce el nombre de la pelicula:\n").upper().strip()
    movies.append(movie)
    missionCompleted()
    #return movie

def showMovies(movies):
    print("\nt...¡...:::MOSTRAR PELICULAS:::...!...\n")
    print("\tCodigo\t\tPeliculas\n")
    for i in range(0,len(movies)):
        print(f"{i+1}\t\t{movies[i]}")
    waiting()

def erasedMovie():
    if len(movies)>0:
        movies=movies.clear()
        missionCompleted()
    else:
        input("...¡NO HAY PELICULAS QUE ELIMINAR!...")

def searchMovies(movies):
    print("\nt...¡...:::BUSCAR PELICULAS:::...!...\n")
    movie=input("Escribe el Nombre de la Pelicula: ").upper().strip()
    if movie in movies:
        print("\tCodigo\t\tPeliculas\n")
        for i in range(0,len(movies)):
            if movie==movies[i]:
                print(f"{i+1}\t\t{movies[i]}")
        waiting()
    else:
        input("...¡No existe la pelicula!...")

def cleanMovies(movies):
    positions=[]
    print("\nt...¡...:::BORRAR PELICULAS:::...!...\n")
    movie=input("Escribe el Nombre de la Pelicula: ").upper().strip()
    if movie in movies:
        for i in range(0,len(movies)):
            if movie==movies[i]:
                positions.append(i)
                #movies.remove(movie)
                #missionCompleted()
        if len(positions)>0:
            for i in range(0,len(positions)):
                movies.remove(movie)
    else:
        input("...¡No existe la pelicula!...")

def editMovies(movies):
    print("\nt...¡...:::EDITAR PELICULAS:::...!...\n")
    movie=input("Escribir el nombre de la pelicula: ").upper().strip()
    if movie in movies:
        for i in range(0,len(movies)):
            if movie==movies[i]:
                print(f"{i+1}\t\t{movies[i]}")
        waiting()
        newMovie=input("\nIngrese el nuevo nombre de la pelicula: ").upper().strip()
        confirm=input(f"¿Desea cambiar '{movie} por {newMovie}'?S/N: ").upper().strip()

        while confirm !="S" and confirm !="N":
            print("...:::¡Opcion invalida!:::...")
            confirm=input(f"¿Desea cambiar '{movie} por {newMovie}'?S/N: ").upper().strip()

        if confirm == "S":
            for i in range(0,len(movies)):
                if movies[i]==movie:
                    movies[i] = newMovie
            print(f"\n\t¡Pelicula(s) actualizada(s) exitosamente!")
            waiting()
        else:
            print("..::¡Edicion cancelada!::..")
            waiting()
    else:
        input("...:::No existe la pelicula:::...")




