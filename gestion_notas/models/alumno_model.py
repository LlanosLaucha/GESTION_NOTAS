class Alumno:
    """
    Modelo de datos que representa a un Alumno.
    """
    def __init__(self, nombre, apellido, dni, id=None, activo=1):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.activo = activo

    def __str__(self):
        return f"Alumno(ID: {self.id}, DNI: '{self.dni}', Nombre: '{self.nombre}', Apellido: '{self.apellido}')"