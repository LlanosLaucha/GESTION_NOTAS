import datetime

class Nota:
    """
    Modelo de datos que representa una Nota académica.
    """
    def __init__(self, id_alumnos, id_materias, nota_final, id_anios, id_estados=None, id_notas=None, fecha=None, **kwargs):
        """
        Constructor del modelo.
        **kwargs absorbe campos adicionales de los JOINs (ej: 'materia', 'estado').
        """
        self.id_notas = id_notas
        self.id_alumnos = id_alumnos
        self.id_materias = id_materias
        self.nota_final = nota_final
        self.id_anios = id_anios
        self.id_estados = id_estados # Calculado por el servicio
        
        self.fecha = fecha if fecha else datetime.date.today()

        # Atributos extra (de JOINs)
        self.materia = kwargs.get('materia', None)
        self.estado = kwargs.get('estado', None)
        self.anio = kwargs.get('anio', None)

    def __str__(self):
        return f"Nota(ID: {self.id_notas}, Alumno: {self.id_alumnos}, Nota: {self.nota_final})"