import funciones
      
'''
pelis={
    "nombre":"Toy story 5",
    "duracion":"120 min",
    "idioma":"español",
    "clasificacion":"A",
    "genero":"animada",
  }
'''

def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: DEFINIR PELICULAS ::::...\n")
    caract=input("Introducir el nombre de la caracteristica: ").lower().strip()
    valor=input("Introducir el nombre de la caracteristica: ").upper().strip()
    pelis[caract]=valor
    funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR CARACTERISTICAS DE LA PELICULA ::::...\n")
    if len(pelis)>0:
        print("\tCaracteristica\t\tvalor\n")
        for i in pelis:
            print(f"{i+1}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("\n\tNo hay peliculas\n\t")

def limpiarPeliculas(pelis):
    if len(pelis)>0:
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Deseas borrar TODAS la pelicula (Si/No)? ").lower().strip()
            posiciones.append(i)
            if opc=="si":
                pelis.clear()
                funciones.accionExitosa()
    else:
        input("...¡No hay peliculas que borrar!...") 
        
def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR UNA CARACTERISTICA DE LA PELICULAS ::::...\n")
    caract=input("Escribir el nombre de la caracteristica: ").upper().strip()
    no_encontro=True
    for i in pelis:
        if caract==[i]:
            print("\tCaracteristica\t\tvalor\n")
            print(f"{i}\t\t{pelis[i]}")
            no_encontro=False
        funciones.espereTecla()

    if no_encontro:
        input("...¡No exite la caracteristica que estas buscando, verifique!...")

def borrarPeliculas(pelis):
    print("\n\t\t...:::: BORRAR UNA CARACTERISTICA DE LA PELICULAS ::::...\n")
    peli=input("Escribir el nombre de la caracteristica: ").upper().strip()
    no_encontro=True
    for i in range(0,len(pelis)):
        if caract==i:
            print(f"{i}\t\n\t{pelis[i]}")
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
            if opc=="si":
                pelis.pop(caract)
                funciones.accionExitosa()
                no_encontro=False
    if no_encontro:
        input("...¡No exite la caracteristica que estas buscando, verifique!...")
        
def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR EL VALOR DE UNA CARACTERISTICA DE UNA PELICULAS ::::...\n")
    caract=input("Escribir el nombre de la pelicula: ").upper().strip()
    no_encontro=True
    for i in pelis:
        if caract==i:
            print(f"{i}\t\n\t{pelis[i]}")
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Deseas modificar el valor de la caracteristica de la pelicula (Si/No)? ").lower().strip()
            if opc=="si":
                pelis[caract]=input("Introducir el nuevo valor de la caracteristica: ").upper().strip()
                funciones.accionExitosa()
                no_encontro=False
    if no_encontro:
        input("...¡No exite la caracteristica que estas buscando, verifique!...")