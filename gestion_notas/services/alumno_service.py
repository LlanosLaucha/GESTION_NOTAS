from gestion_notas.models.alumno_model import Alumno
from gestion_notas.config.db_config import get_db_connection
from mysql.connector import Error 

class AlumnoService:

    def __init__(self):
        pass

    def crear_alumno(self, alumno: Alumno):
        """
        Inserta un nuevo alumno en la base de datos como 'activo'.
        """
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                return None

            cursor = conn.cursor()
            query = "INSERT INTO alumnos (nombre, apellido, dni, activo) VALUES (%s, %s, %s, %s)"
            values = (alumno.nombre, alumno.apellido, alumno.dni, 1)
            
            cursor.execute(query, values)
            conn.commit()
            
            return cursor.lastrowid
        
        except Error as e:
            print(f"Error al crear alumno: {e}")
            return None
        
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def obtener_alumnos(self):
        """
        Obtiene una lista de todos los alumnos marcados como 'activos'.
        """
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                return []

            cursor = conn.cursor(dictionary=True) 
            query = "SELECT id_alumnos as id, nombre, apellido, dni, activo FROM alumnos WHERE activo = 1"
            
            cursor.execute(query)
            rows = cursor.fetchall()
            
            return [Alumno(**row) for row in rows]

        except Error as e:
            print(f"Error al obtener alumnos: {e}")
            return []
        
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def obtener_alumno_por_id(self, id_alumno: int):
        """
        Obtiene un único alumno activo por su ID.
        """
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                return None
                
            cursor = conn.cursor(dictionary=True)
            query = "SELECT id_alumnos as id, nombre, apellido, dni, activo FROM alumnos WHERE id_alumnos = %s AND activo = 1"
            
            cursor.execute(query, (id_alumno,))
            row = cursor.fetchone()
            
            return Alumno(**row) if row else None

        except Error as e:
            print(f"Error al obtener alumno por ID: {e}")
            return None
        
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def actualizar_alumno(self, alumno: Alumno):
        """
        Actualiza los datos (nombre, apellido, dni) de un alumno existente.
        """
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                return 0
                
            cursor = conn.cursor()
            query = """
                UPDATE alumnos
                SET nombre = %s, apellido = %s, dni = %s
                WHERE id_alumnos = %s 
            """
            values = (alumno.nombre, alumno.apellido, alumno.dni, alumno.id)
            
            cursor.execute(query, values)
            conn.commit()
            
            return cursor.rowcount

        except Error as e:
            print(f"Error al actualizar alumno: {e}")
            return 0
        
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def eliminar_alumno(self, id_alumno: int):
        """
        Implementa el Borrado Lógico (Soft Delete).
        Actualiza el estado del alumno a 'inactivo' (activo = 0).
        """
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                return 0
                
            cursor = conn.cursor()
            query = "UPDATE alumnos SET activo = 0 WHERE id_alumnos = %s"
            
            cursor.execute(query, (id_alumno,))
            conn.commit()
            
            return cursor.rowcount

        except Error as e:
            print(f"Error al eliminar alumno: {e}")
            return 0
        
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()