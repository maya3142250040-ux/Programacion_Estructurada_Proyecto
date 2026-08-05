import funciones

def insertar(libro, autor, genero, clasificacion, origen, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("INSERT INTO libros VALUES (NULL,%s,%s,%s,%s,%s)",
                           (libro, autor, genero, clasificacion, origen))
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
            cursor.execute("SELECT * FROM libros")
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print("ERROR AL CONSULTAR:", e)
        return []


def buscar(libro, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM libros where libro=%s", (libro,))
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
            cursor.execute("truncate libros")
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL VACIAR:", e)
        return False


def borrar(libro, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from libros where libro=%s", (libro,))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL BORRAR:", e)
        return False


def actualizar(libro_old, libro, autor, genero, clasificacion, origen, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "update libros set libro=%s, autor=%s, genero=%s, clasificacion=%s, origen=%s where libro=%s",
                (libro, autor, genero, clasificacion, origen, libro_old))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL ACTUALIZAR:", e)
        return False