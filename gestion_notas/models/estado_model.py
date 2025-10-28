class Estado:
    """
    Modelo para representar un estado de nota (Aprobado, Desaprobado, etc.)
    """
    def __init__(self, id_estados=None, descripcion=None, **kwargs):
        self.id_estados = id_estados
        self.descripcion = descripcion

    def __str__(self):
        return f"Estado(ID: {self.id_estados}, Descripción: '{self.descripcion}')"
