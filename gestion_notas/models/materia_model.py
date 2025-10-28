class Materia:
    """
    Modelo para representar una materia
    """
    def __init__(self, id_materias=None, descripcion=None, condicion=1, **kwargs):
        self.id_materias = id_materias
        self.descripcion = descripcion
        self.condicion = condicion

    def __str__(self):
        return f"Materia(ID: {self.id_materias}, Descripción: '{self.descripcion}')"
