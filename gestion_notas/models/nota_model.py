import datetime

class Nota:
    """
    Representa el Modelo para una nota académica.
    Este modelo ahora coincide con los campos de la base de datos 
    y la lógica de nota_service.py.
    """
    def __init__(self, id_alumnos, id_materias, nota_final, id_anios, id_estados, id_notas=None, fecha=None, **kwargs):
        """
        Inicializador que mapea los campos de la tabla 'notas'.
        Usamos **kwargs para absorber campos extra de los JOINs (como 'materia').
        """
        self.id_notas = id_notas
        self.id_alumnos = id_alumnos
        self.id_materias = id_materias
        self.nota_final = nota_final
        self.id_anios = id_anios
        self.id_estados = id_estados
        
        # Asignar la fecha de hoy si no se provee una
        self.fecha = fecha if fecha else datetime.date.today()

        # Atributos extra que vienen de los JOINs (para la vista)
        # Se asignarán si existen en los kwargs
        self.materia = kwargs.get('materia', None)
        self.estado = kwargs.get('estado', None)
        self.anio = kwargs.get('anio', None)

    def __str__(self):
        # Un __str__ más completo
        return f"Nota(ID: {self.id_notas}, Alumno: {self.id_alumnos}, Materia: {self.materia} ({self.id_materias}), Nota: {self.nota_final})"
