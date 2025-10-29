class Alumno:
    """
    Representa el Modelo para un Alumno.
    """
    def __init__(self, nombre, apellido, dni, id=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"Alumno(ID: {self.id}, DNI: '{self.dni}', Nombre: '{self.nombre}', Apellido: '{self.apellido}')"