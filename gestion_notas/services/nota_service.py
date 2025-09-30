from gestion_notas.models.nota_model import Nota
import mysql.connector


class NotaService:
    def __init__(self):
        # Configura la conexión a la base de datos.
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root2025", # Cambiar por la contraseña real
            database="gestion_notas"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def _crear_conexion(self):
        # Establece conexión con la base de datos.
        if not self.conn.is_connected():
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root2025",
                database="gestion_notas"
            )
            self.cursor = self.conn.cursor(dictionary=True)

    def crear_nota(self, nota: Nota):
        # Inserta una nueva nota en la base de datos.
        query = """
            INSERT INTO notas (id_materias, calificacion, fecha_calificado)
            VALUES (%s, %s, %s, %s)
        """
        values = (nota.alumno_id, nota.materia, nota.calificacion, nota.fecha)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener_notas_por_alumno(self, alumno_id: int):
        # Obtiene todas las notas de un alumno específico.
        query = "SELECT * FROM notas WHERE id_alumnos = %s"
        self.cursor.execute(query, (alumno_id,))
        rows = self.cursor.fetchall()
        return [Nota(**row) for row in rows]

    def actualizar_nota(self, nota: Nota):
        # Actualiza una nota existente en la base de datos.
        query = """
            UPDATE notas
            SET id_materias = %s, calificacion = %s, fecha = %s
            WHERE id = %s
        """
        values = (nota.materia, nota.calificacion, nota.fecha, nota.id)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.rowcount

    def eliminar_nota(self, id_nota: int):
        # Elimina una nota de la base de datos usando su ID.
        query = "DELETE FROM notas WHERE id = %s"
        self.cursor.execute(query, (id_nota,))
        self.conn.commit()
        return self.cursor.rowcount
