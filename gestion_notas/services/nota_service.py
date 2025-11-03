from gestion_notas.models.nota_model import Nota
from gestion_notas.config.db_config import get_db_connection
from mysql.connector import Error

class NotaService:

    def __init__(self):
        """
        Constructor vacío. La conexión se maneja por método.
        """
        pass

    def crear_nota(self, nota: Nota):
        """
        Inserta una nueva nota en la base de datos.
        """
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                return None
            
            cursor = conn.cursor()
            query = """
                INSERT INTO notas (id_alumnos, id_materias, nota_final, id_anios, id_estados)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                nota.id_alumnos,
                nota.id_materias,
                nota.nota_final,
                nota.id_anios,
                nota.id_estados
            )
            
            cursor.execute(query, values)
            conn.commit()
            
            return cursor.lastrowid  # Devuelve el id_notas generado

        except Error as e:
            print(f"Error al crear nota: {e}")
            return None
        
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def obtener_notas_por_alumno(self, alumno_id: int):
        """
        Obtiene todas las notas de un alumno específico, uniendo tablas
        para obtener descripciones legibles.
        """
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                return []

            cursor = conn.cursor(dictionary=True)
            # Esta es la consulta compleja del PDF, ahora activa
            query = """
                SELECT n.*, m.descripcion AS materia, e.descripcion AS estado, a.descripcion AS anio
                FROM notas n
                JOIN materias m ON n.id_materias = m.id_materias
                JOIN estados e ON n.id_estados = e.id_estados
                JOIN anios a ON n.id_anios = a.id_anios
                WHERE n.id_alumnos = %s
            """
            
            cursor.execute(query, (alumno_id,))
            rows = cursor.fetchall()
            
            # Usamos el modelo Nota (que ahora acepta **kwargs)
            return [Nota(**row) for row in rows]

        except Error as e:
            print(f"Error al obtener notas por alumno: {e}")
            return []
        
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def actualizar_nota(self, nota: Nota):
        """
        Actualiza una nota existente.
        """
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                return 0
                
            cursor = conn.cursor()
            query = """
                UPDATE notas
                SET id_materias = %s,
                    nota_final = %s,
                    id_anios = %s,
                    id_estados = %s
                WHERE id_notas = %s
            """
            values = (
                nota.id_materias,
                nota.nota_final,
                nota.id_anios,
                nota.id_estados,
                nota.id_notas
            )
            
            cursor.execute(query, values)
            conn.commit()
            
            return cursor.rowcount

        except Error as e:
            print(f"Error al actualizar nota: {e}")
            return 0
        
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def eliminar_nota(self, id_nota: int):
        """
        Elimina una nota según su ID.
        """
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                return 0
                
            cursor = conn.cursor()
            query = "DELETE FROM notas WHERE id_notas = %s"
            
            cursor.execute(query, (id_nota,))
            conn.commit()
            
            return cursor.rowcount

        except Error as e:
            print(f"Error al eliminar nota: {e}")
            return 0
        
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
