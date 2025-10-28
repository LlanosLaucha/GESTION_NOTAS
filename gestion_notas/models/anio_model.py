class Anio:
    """
    Modelo para representar un año académico
    """
    def __init__(self, id_anios=None, descripcion=None, **kwargs):
        self.id_anios = id_anios
        self.descripcion = descripcion

    def __str__(self):
        return f"Año(ID: {self.id_anios}, Descripción: '{self.descripcion}')"
