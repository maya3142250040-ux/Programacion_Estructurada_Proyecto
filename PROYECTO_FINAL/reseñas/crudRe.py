import funciones

def insertar(id_libro, id_usuario, titulo, reseña, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("INSERT INTO reseñas VALUES (NULL,%s,%s,%s,%s)", (id_libro, id_usuario, titulo, reseña))
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
            cursor.execute("""
                SELECT libros.ID, libros.libro, GROUP_CONCAT(usuario.usuario SEPARATOR ', ')
                FROM libros
                INNER JOIN reseñas ON libros.ID = reseñas.id_libro
                INNER JOIN usuario ON reseñas.id_usuario = usuario.id
                GROUP BY libros.ID, libros.libro
            """)
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print("ERROR AL CONSULTAR:", e)
        return []


def buscarPorLibro(id_libro, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("""
                SELECT reseñas.id, reseñas.titulo, usuario.usuario
                FROM reseñas
                INNER JOIN usuario ON reseñas.id_usuario = usuario.id
                WHERE reseñas.id_libro = %s
            """, (id_libro,))
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print("ERROR AL CONSULTAR:", e)
        return []


def buscarPorId(id_reseña, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("""
                SELECT reseñas.id, reseñas.titulo, reseñas.reseña, usuario.usuario, libros.libro
                FROM reseñas
                INNER JOIN usuario ON reseñas.id_usuario = usuario.id
                INNER JOIN libros ON reseñas.id_libro = libros.ID
                WHERE reseñas.id = %s
            """, (id_reseña,))
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print("ERROR AL BUSCAR:", e)
        return []


def actualizar(id_reseña, titulo, reseña, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("update reseñas set titulo=%s, reseña=%s where id=%s", (titulo, reseña, id_reseña))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL ACTUALIZAR:", e)
        return False


def borrar(id_reseña, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from reseñas where id=%s", (id_reseña,))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL BORRAR:", e)
        return False


def vaciar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("truncate reseñas")
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print("ERROR AL VACIAR:", e)
        return False