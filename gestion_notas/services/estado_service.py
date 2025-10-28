import mysql.connector
from models.estado_model import Estado
from config.db_config import DB_CONFIG


class EstadoService:
    """
    Servicio para gestionar operaciones de estados de notas
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

    def obtener_estados(self):
        """Obtiene todos los estados"""
        try:
            self._crear_conexion()
            query = "SELECT * FROM estados ORDER BY descripcion"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [Estado(**row) for row in rows]
        except mysql.connector.Error as e:
            print(f"Error al obtener estados: {e}")
            return []

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos"""
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
