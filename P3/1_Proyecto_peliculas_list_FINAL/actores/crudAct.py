import funciones

def insertar(actor, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("INSERT INTO actores VALUES (NULL,%s)", (actor,))
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
            cursor.execute("SELECT * FROM actores")
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print("ERROR AL CONSULTAR:", e)
        return []


def buscar(actor, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM actores where nombre=%s", (actor,))
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
            cursor.execute("truncate actores")
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL VACIAR:", e)
        return False


def borrar(actor, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from actores where nombre=%s", (actor,))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL BORRAR:", e)
        return False


def actualizar(actorOld, actorNew, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("update actores set nombre=%s where nombre=%s", (actorNew, actorOld))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL ACTUALIZAR:", e)
        return False