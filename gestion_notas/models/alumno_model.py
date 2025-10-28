class Alumno:
    """
    Modelo para representar un alumno
    """
    def __init__(self, id_alumnos=None, nombre=None, apellido=None, dni=None, condicion=1, **kwargs):
        self.id_alumnos = id_alumnos
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.condicion = condicion

    def __str__(self):
        return f"Alumno(ID: {self.id_alumnos}, DNI: '{self.dni}', Nombre: '{self.nombre}', Apellido: '{self.apellido}')"
