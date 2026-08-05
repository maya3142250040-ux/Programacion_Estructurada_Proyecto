import funciones

def insertar(nombre, categoria, clasificacion, genero, idioma, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "INSERT INTO peliculas VALUES (NULL,%s,%s,%s,%s,%s)",
                (nombre, categoria, clasificacion, genero, idioma)
            )
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL INSERTAR:", e)
        return False


def consultar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("select * from peliculas")
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print("ERROR AL CONSULTAR:", e)
        return []


def buscar(peli, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("select * from peliculas where nombre=%s", (peli,))
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print("ERROR AL BUSCAR:", e)
        return []


def vaciar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("truncate peliculas")
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL VACIAR:", e)
        return False


def borrar(peli, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from peliculas where nombre=%s", (peli,))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL BORRAR:", e)
        return False


def actualizar(peli, nombre, categoria, clasificacion, genero, idioma, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "update peliculas set nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s where nombre=%s",
                (nombre, categoria, clasificacion, genero, idioma, peli)
            )
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL ACTUALIZAR:", e)
        return False