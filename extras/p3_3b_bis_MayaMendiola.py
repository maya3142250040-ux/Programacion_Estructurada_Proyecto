import mysql.connector

#MENU
def borrarPantalla():
    print("\033c")

def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Mostrar\n\t3.-Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def espereTecla():
    input("\n\t...¡Oprima cualquier tecla para continuar!...")
    
def opcionInvalida():
    input("\n\t...¡Opcion invalidad, por favor verifique !...")
    
def accionExitosa():
    input("\n\t...¡Accion Realizada con Exito !...")

def accionNoExitosa():
    input("\n\t...¡No fue posible realiazr esta accion !...")

def terminarSistema():
    input("\n\t\t...:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA ::::...\n")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="peliculas_exam"
        )
        return conexion
    except Exception as e:
        print("ERROR DE CONEXION:", e)
        return None


#PELICULAS

def agregarPeliculas(conexionBD):
    print("\n\t\t...:::: AGREGAR PELICULAS Y SU CATEGORIA ::::...\n")
    peli=input("Introducir el nombre de la pelicula: ").upper().strip()
    categoria=input("Introducir la categoria de la pelicula: ").upper().strip()
    respuesta=insertar(peli, categoria, conexionBD)
    if respuesta:
        accionExitosa()
    else:
        accionNoExitosa()

def mostrarPeliculas(conexionBD):
    print("\n\t\t...:::: MOSTRAR PELICULAS ::::...\n")
    pelis=consultar(conexionBD)
    if len(pelis)>0:
        print("\tCodigo\t\tPelicula\t\tCategoria")
        for i in pelis:
            print(f"\t{i[0]}\t\t{i[1]}\t\t{i[2]}")
            espereTecla()
    else:
         input("...¡No hay peliculas que mostrar!...") 
    

#CRUD 
def insertar(peli,categoria, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("INSERT INTO peliculas_exam VALUES (NULL,%s,%s)", (peli,categoria,))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL INSERTAR:", e)
        return False
    
def consultar(conexionBD):
    try:
       if conexionBD!=None:
           cursor=conexionBD.cursor()
           cursor.execute("select * from peliculas_exam")
           return cursor.fetchall()
       else:
           return []
    except:
        return []  




conexionBD=conectar()


opc=""

while opc!="3":
    borrarPantalla()
    opc=menuPrincial()
    match opc:
        case "1":
            borrarPantalla()
            agregarPeliculas(conexionBD)
        case "2":
            borrarPantalla()
            mostrarPeliculas(conexionBD)
        case "3":
            borrarPantalla()
            terminarSistema()
        case _:
            opcionInvalida()
