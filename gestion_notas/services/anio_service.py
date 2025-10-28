import mysql.connector
from models.anio_model import Anio
from config.db_config import DB_CONFIG


class AnioService:
    """
    Servicio para gestionar operaciones de años académicos
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

    def obtener_anios(self):
        """Obtiene todos los años académicos"""
        try:
            self._crear_conexion()
            query = "SELECT * FROM anios ORDER BY descripcion DESC"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [Anio(**row) for row in rows]
        except mysql.connector.Error as e:
            print(f"Error al obtener años: {e}")
            return []

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos"""
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
