import datetime

class Nota:
    """
    Representa el Modelo para una nota académica.
    """
    def __init__(self, materia, calificacion, alumno_id, fecha=None, id=None):
        self.id = id
        self.materia = materia
        self.calificacion = calificacion
        self.alumno_id = alumno_id
        
        if fecha is None:
            self.fecha = datetime.date.today()
        else:
            self.fecha = fecha

    def __str__(self):
        return f"Nota(ID: {self.id}, Alumno_ID: {self.alumno_id}, Materia: '{self.materia}', Calificación: {self.calificacion}, Fecha: {self.fecha})"