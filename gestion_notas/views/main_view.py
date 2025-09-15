import tkinter as tk
from tkinter import ttk, messagebox
from gestion_notas.services.alumno_service import AlumnoService
from gestion_notas.services.nota_service import NotaService
from gestion_notas.models.alumno_model import Alumno
from gestion_notas.models.nota_model import Nota

class MainView:
    """
    Clase que construye y gestiona la interfaz gráfica principal de la aplicación.
    """
    def __init__(self, root):
        """
        Constructor de la vista principal.
        """
        self.root = root
        self.root.title("Sistema de Gestión de Notas por Alumno")
        self.root.geometry("1100x600")

        # Instancias de los servicios que se comunican con la base de datos
        self.alumno_service = AlumnoService()
        self.nota_service = NotaService()

        # Variables para guardar el estado de la selección
        self.alumno_seleccionado = None
        self.nota_seleccionada = None

        # Método principal que construye todos los componentes visuales
        self._crear_widgets()

    def _crear_widgets(self):
        """
        Crea todos los componentes visuales (widgets) de la interfaz.
        A implementar por el equipo de frontend.
        """
        # Aquí iría todo el código para crear los PanedWindow, Frames,
        # Labels, Entries, Buttons y Treeviews.
        # Por ahora, lo dejamos vacío para que el equipo lo complete.
        pass

    # --- MÓDULOS DE LÓGICA PARA ALUMNOS ---

    def cargar_alumnos(self):
        """
        Limpia la tabla de alumnos y la vuelve a cargar con datos frescos
        de la base de datos.
        A implementar por el equipo de frontend.
        """
        pass

    def seleccionar_alumno(self, event):
        """
        Se activa al hacer clic en un alumno en la tabla.
        Guarda el alumno seleccionado y carga sus notas.
        A implementar por el equipo de frontend.
        """
        pass

    def agregar_alumno(self):
        """
        Recoge los datos del formulario de alumnos, los valida y llama al
        servicio para crear un nuevo alumno.
        A implementar por el equipo de frontend.
        """
        pass

    def modificar_alumno(self):
        """
        Recoge los datos del formulario y actualiza al alumno seleccionado.
        A implementar por el equipo de frontend.
        """
        pass

    def eliminar_alumno(self):
        """
        Pide confirmación y elimina al alumno seleccionado.
        A implementar por el equipo de frontend.
        """
        pass

    def limpiar_campos_alumno(self):
        """
        Limpia los campos de entrada del formulario de alumnos.
        A implementar por el equipo de frontend.
        """
        pass

    # --- MÓDULOS DE LÓGICA PARA NOTAS ---

    def cargar_notas_por_alumno(self):
        """
        Limpia la tabla de notas y la carga con las notas del alumno
        que esté actualmente seleccionado.
        A implementar por el equipo de frontend.
        """
        pass
        
    def seleccionar_nota(self, event):
        """
        Se activa al hacer clic en una nota en la tabla.
        Guarda la nota seleccionada y llena el formulario de notas.
        A implementar por el equipo de frontend.
        """
        pass

    def agregar_nota(self):
        """
        Recoge los datos del formulario de notas y crea una nueva nota
        para el alumno seleccionado.
        A implementar por el equipo de frontend.
        """
        pass

    def modificar_nota(self):
        """
        Recoge los datos del formulario y actualiza la nota seleccionada.
        A implementar por el equipo de frontend.
        """
        pass

    def eliminar_nota(self):
        """
        Pide confirmación y elimina la nota seleccionada.
        A implementar por el equipo de frontend.
        """
        pass

    def limpiar_campos_nota(self):
        """
        Limpia los campos de entrada del formulario de notas.
        A implementar por el equipo de frontend.
        """
        pass

    # --- MÓDULOS AUXILIARES ---

    def _mostrar_error(self, titulo, mensaje):
        """
        Muestra un cuadro de diálogo de error.
        A implementar por el equipo de frontend.
        """
        messagebox.showerror(titulo, mensaje)

    def _mostrar_info(self, titulo, mensaje):
        """
        Muestra un cuadro de diálogo de información.
        A implementar por el equipo de frontend.
        """
        messagebox.showinfo(titulo, mensaje)

