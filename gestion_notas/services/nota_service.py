from gestion_notas.models.nota_model import Nota
import mysql.connector


class NotaService:
    def __init__(self):
        # Conexión inicial a la base de datos
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root2025",  # Cambiar si corresponde
            database="gestion_notas"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def _crear_conexion(self):
        """Reconecta si la conexión se perdió."""
        if not self.conn.is_connected():
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root2025",
                database="gestion_notas"
            )
            self.cursor = self.conn.cursor(dictionary=True)

    def crear_nota(self, nota: Nota):
        """
        Inserta una nueva nota.
        Campos requeridos:
        - id_alumnos
        - id_materias
        - nota_final
        - id_anios
        - id_estados
        """
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
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid  # Devuelve el id_notas generado

    def obtener_notas_por_alumno(self, alumno_id: int):
        """Obtiene todas las notas de un alumno."""
        query = """
            SELECT n.*, m.descripcion AS materia, e.descripcion AS estado, a.descripcion AS anio
            FROM notas n
            JOIN materias m ON n.id_materias = m.id_materias
            JOIN estados e ON n.id_estados = e.id_estados
            JOIN anios a ON n.id_anios = a.id_anios
            WHERE n.id_alumnos = %s
        """
        self.cursor.execute(query, (alumno_id,))
        rows = self.cursor.fetchall()
        return [Nota(**row) for row in rows]

    def actualizar_nota(self, nota: Nota):
        """Actualiza una nota existente."""
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
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.rowcount

    def eliminar_nota(self, id_nota: int):
        """Elimina una nota según su ID."""
        query = "DELETE FROM notas WHERE id_notas = %s"
        self.cursor.execute(query, (id_nota,))
        self.conn.commit()
        return self.cursor.rowcount
