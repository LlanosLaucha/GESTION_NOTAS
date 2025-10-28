import mysql.connector
from models.alumno_model import Alumno
from config.db_config import DB_CONFIG


class AlumnoService:
    """
    Servicio para gestionar operaciones CRUD de alumnos
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

    def crear_alumno(self, alumno: Alumno):
        """Inserta un nuevo alumno en la base de datos"""
        try:
            self._crear_conexion()
            query = """
                INSERT INTO alumnos (id_alumnos, nombre, apellido, dni, condicion)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (alumno.id_alumnos, alumno.nombre, alumno.apellido, alumno.dni, alumno.condicion)
            self.cursor.execute(query, values)
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error al crear alumno: {e}")
            return False

    def obtener_alumnos(self):
        """Obtiene todos los alumnos activos"""
        try:
            self._crear_conexion()
            query = "SELECT * FROM alumnos WHERE condicion = 1 ORDER BY apellido, nombre"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [Alumno(**row) for row in rows]
        except mysql.connector.Error as e:
            print(f"Error al obtener alumnos: {e}")
            return []

    def obtener_alumno_por_id(self, id_alumno: int):
        """Obtiene un alumno por su ID"""
        try:
            self._crear_conexion()
            query = "SELECT * FROM alumnos WHERE id_alumnos = %s"
            self.cursor.execute(query, (id_alumno,))
            row = self.cursor.fetchone()
            return Alumno(**row) if row else None
        except mysql.connector.Error as e:
            print(f"Error al obtener alumno: {e}")
            return None

    def actualizar_alumno(self, alumno: Alumno):
        """Actualiza los datos de un alumno"""
        try:
            self._crear_conexion()
            query = """
                UPDATE alumnos
                SET nombre = %s, apellido = %s, dni = %s
                WHERE id_alumnos = %s
            """
            values = (alumno.nombre, alumno.apellido, alumno.dni, alumno.id_alumnos)
            self.cursor.execute(query, values)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except mysql.connector.Error as e:
            print(f"Error al actualizar alumno: {e}")
            return False

    def eliminar_alumno(self, id_alumno: int):
        """Elimina lógicamente un alumno (cambio de condición)"""
        try:
            self._crear_conexion()
            query = "UPDATE alumnos SET condicion = 0 WHERE id_alumnos = %s"
            self.cursor.execute(query, (id_alumno,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except mysql.connector.Error as e:
            print(f"Error al eliminar alumno: {e}")
            return False

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos"""
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
