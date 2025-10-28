import mysql.connector
from models.materia_model import Materia
from config.db_config import DB_CONFIG


class MateriaService:
    """
    Servicio para gestionar operaciones CRUD de materias
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

    def crear_materia(self, materia: Materia):
        """Inserta una nueva materia en la base de datos"""
        try:
            self._crear_conexion()
            query = """
                INSERT INTO materias (id_materias, descripcion, condicion)
                VALUES (%s, %s, %s)
            """
            values = (materia.id_materias, materia.descripcion, materia.condicion)
            self.cursor.execute(query, values)
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error al crear materia: {e}")
            return False

    def obtener_materias(self):
        """Obtiene todas las materias activas"""
        try:
            self._crear_conexion()
            query = "SELECT * FROM materias WHERE condicion = 1 ORDER BY descripcion"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [Materia(**row) for row in rows]
        except mysql.connector.Error as e:
            print(f"Error al obtener materias: {e}")
            return []

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos"""
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
