from gestion_notas.models.alumno_model import Alumno
import mysql.connector


class AlumnoService:
    def __init__(self):
        """
        Configura la conexión a la base de datos.
        """
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Root2025',  # Cambiar si corresponde
            database='gestion_notas'
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def _crear_conexion(self):
        """
        Reconecta si la conexión se perdió.
        """
        if not self.conn.is_connected():
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Root2025',
                database='gestion_notas'
            )
            self.cursor = self.conn.cursor(dictionary=True)

    def crear_alumno(self, alumno: Alumno):
        """
        Inserta un nuevo alumno en la base de datos.
        Campos: nombre, apellido, dni
        """
        query = """
            INSERT INTO alumnos (nombre, apellido, dni)
            VALUES (%s, %s, %s)
        """
        values = (alumno.nombre, alumno.apellido, alumno.dni)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid  # Devuelve el ID generado automáticamente

    def obtener_alumnos(self):
        """
        Obtiene todos los alumnos.
        """
        query = "SELECT * FROM alumnos"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Alumno(**row) for row in rows]

    def obtener_alumno_por_id(self, id_alumno: int):
        """
        Obtiene un alumno por su ID.
        """
        query = "SELECT * FROM alumnos WHERE id_alumnos = %s"
        self.cursor.execute(query, (id_alumno,))
        row = self.cursor.fetchone()
        return Alumno(**row) if row else None

    def actualizar_alumno(self, alumno: Alumno):
        """
        Actualiza los datos de un alumno.
        """
        query = """
            UPDATE alumnos
            SET nombre = %s, apellido = %s, dni = %s
            WHERE id_alumnos = %s
        """
        values = (alumno.nombre, alumno.apellido, alumno.dni, alumno.id_alumnos)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.rowcount  # Devuelve cantidad de filas modificadas

    def eliminar_alumno(self, id_alumno: int):
        """
        Elimina un alumno por su ID.
        """
        query = "DELETE FROM alumnos WHERE id_alumnos = %s"
        self.cursor.execute(query, (id_alumno,))
        self.conn.commit()
        return self.cursor.rowcount
