from gestion_notas.models.nota_model import Nota
import mysql.connector

class NotaService:
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

    def crear_nota(self, nota):
        """
        Inserta una nueva nota en la base de datos.
        """
        # A implementar por el equipo de backend.
        pass

    def obtener_notas_por_alumno(self, alumno_id):
        """
        Obtiene todas las notas de un alumno específico.
        """
        # A implementar por el equipo de backend.
        pass

    def actualizar_nota(self, nota):
        """
        Actualiza una nota existente en la base de datos.
        """
        # A implementar por el equipo de backend.
        pass

    def eliminar_nota(self, id_nota):
        """
        Elimina una nota de la base de datos usando su ID.
        """
        # A implementar por el equipo de backend.
        pass