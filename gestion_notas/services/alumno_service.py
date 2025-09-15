from gestion_notas.models.alumno_model import Alumno
import mysql.connector

class AlumnoService:
    def __init__(self):
        """
        Configura la conexión a la base de datos.
        """
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'tu_contraseña_aqui',
            'database': 'gestion_notas_db'
        }

    def _crear_conexion(self):
        """
        Establece conexión con la base de datos.
        """
        # A implementar por el equipo de backend.
        pass

    def crear_alumno(self, alumno):
        """
        Inserta un nuevo alumno en la base de datos.
        """
        # A implementar por el equipo de backend.
        pass

    def obtener_alumnos(self):
        """
        Obtiene todos los alumnos de la base de datos.
        """
        # A implementar por el equipo de backend.
        pass

    def actualizar_alumno(self, alumno):
        """
        Actualiza un alumno existente en la base de datos.
        """
        # A implementar por el equipo de backend.
        pass

    def eliminar_alumno(self, id_alumno):
        """
        Elimina un alumno de la base de datos usando su ID.
        """
        # A implementar por el equipo de backend.
        pass