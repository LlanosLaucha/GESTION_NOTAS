import mysql.connector
from models.nota_model import Nota
from config.db_config import DB_CONFIG


class NotaService:
    """
    Servicio para gestionar operaciones CRUD de notas
    """
    def __init__(self):
        self.conn = None
        self.cursor = None
        self._crear_conexion()

    def _crear_conexion(self):
        """Crea o renueva la conexión a la base de datos"""
        try:
            if self.conn is None or not self.conn.is_connected():
                self.conn = mysql.connector.connect(**DB_CONFIG)
                self.cursor = self.conn.cursor(dictionary=True)
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def crear_nota(self, nota: Nota):
        """Inserta una nueva nota en la base de datos"""
        try:
            self._crear_conexion()
            query = """
                INSERT INTO notas (id_notas, id_alumnos, id_materias, nota_final, id_anios, id_estados, condicion)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (nota.id_notas, nota.id_alumnos, nota.id_materias, nota.nota_final, 
                     nota.id_anios, nota.id_estados, nota.condicion)
            self.cursor.execute(query, values)
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error al crear nota: {e}")
            return False

    def obtener_notas_por_alumno(self, alumno_id: int):
        """Obtiene todas las notas de un alumno con información de materia, estado y año"""
        try:
            self._crear_conexion()
            query = """
                SELECT n.*, 
                       m.descripcion AS materia, 
                       e.descripcion AS estado, 
                       a.descripcion AS anio
                FROM notas n
                JOIN materias m ON n.id_materias = m.id_materias
                JOIN estados e ON n.id_estados = e.id_estados
                JOIN anios a ON n.id_anios = a.id_anios
                WHERE n.id_alumnos = %s 
                ORDER BY a.descripcion DESC, m.descripcion
            """
            self.cursor.execute(query, (alumno_id,))
            rows = self.cursor.fetchall()
            return [Nota(**row) for row in rows]
        except mysql.connector.Error as e:
            print(f"Error al obtener notas: {e}")
            return []

    def actualizar_nota(self, nota: Nota):
        """Actualiza una nota existente"""
        try:
            self._crear_conexion()
            query = """
                UPDATE notas
                SET id_materias = %s,
                    nota_final = %s,
                    id_anios = %s,
                    id_estados = %s
                WHERE id_notas = %s
            """
            values = (nota.id_materias, nota.nota_final, nota.id_anios, 
                     nota.id_estados, nota.id_notas)
            self.cursor.execute(query, values)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except mysql.connector.Error as e:
            print(f"Error al actualizar nota: {e}")
            return False

    def eliminar_nota(self, id_nota: int):
        """Elimina lógicamente una nota (cambio de condición)"""
        try:
            self._crear_conexion()
            query = "UPDATE notas SET condicion = 0 WHERE id_notas = %s"
            self.cursor.execute(query, (id_nota,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except mysql.connector.Error as e:
            print(f"Error al eliminar nota: {e}")
            return False

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos"""
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
