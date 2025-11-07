import datetime

class Nota:
    """
    Representa el Modelo para una nota académica.
    """
    # MODIFICACIÓN: id_estados ahora es opcional (default=None)
    def __init__(self, id_alumnos, id_materias, nota_final, id_anios, id_estados=None, id_notas=None, fecha=None, **kwargs):
        """
        Inicializador que mapea los campos de la tabla 'notas'.
        """
        self.id_notas = id_notas
        self.id_alumnos = id_alumnos
        self.id_materias = id_materias
        self.nota_final = nota_final
        self.id_anios = id_anios
        self.id_estados = id_estados # Será None al principio
        
        self.fecha = fecha if fecha else datetime.date.today()

        self.materia = kwargs.get('materia', None)
        self.estado = kwargs.get('estado', None)
        self.anio = kwargs.get('anio', None)

    def __str__(self):
        return f"Nota(ID: {self.id_notas}, Alumno: {self.id_alumnos}, Materia: {self.materia} ({self.id_materias}), Nota: {self.nota_final})"