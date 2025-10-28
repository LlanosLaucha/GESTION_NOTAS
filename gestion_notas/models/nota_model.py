class Nota:
    """
    Modelo para representar una nota académica
    """
    def __init__(self, id_notas=None, id_alumnos=None, id_materias=None, 
                 nota_final=None, id_anios=None, id_estados=None, 
                 condicion=1, materia=None, estado=None, anio=None, **kwargs):
        self.id_notas = id_notas
        self.id_alumnos = id_alumnos
        self.id_materias = id_materias
        self.nota_final = nota_final
        self.id_anios = id_anios
        self.id_estados = id_estados
        self.condicion = condicion
        
        # Campos adicionales para JOINs
        self.materia = materia
        self.estado = estado
        self.anio = anio

    def __str__(self):
        return f"Nota(ID: {self.id_notas}, Alumno_ID: {self.id_alumnos}, Materia: '{self.materia}', Nota: {self.nota_final})"
