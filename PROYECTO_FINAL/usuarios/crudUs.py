import funciones

def insertar(usuario, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("INSERT INTO usuario VALUES (NULL,%s)", (usuario,))
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
            cursor.execute("SELECT * FROM usuario")
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print("ERROR AL CONSULTAR:", e)
        return []


def buscar(usuario, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM usuario where usuario=%s", (usuario,))
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
            cursor.execute("truncate usuario")
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL VACIAR:", e)
        return False


def borrar(usuario, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from usuario where usuario=%s", (usuario,))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL BORRAR:", e)
        return False


def actualizar(usuarioOld, usuarioNew, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("update usuario set usuario=%s where usuario=%s", (usuarioNew, usuarioOld))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL ACTUALIZAR:", e)
        return False