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
        self.root.title("Sistema de Gestión de Notas")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)

        # Estilo para los widgets
        self.style = ttk.Style()
        self.style.theme_use('clam') # 'clam', 'alt', 'default', 'vista'
        self.style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))
        self.style.configure('TLabel', font=('Arial', 9))
        self.style.configure('TButton', font=('Arial', 9))
        self.style.configure('TEntry', font=('Arial', 9))

        # Instancias de los servicios
        self.alumno_service = AlumnoService()
        self.nota_service = NotaService()

        # Variables de estado
        self.alumno_seleccionado = None
        self.nota_seleccionada = None
        
        # Cache para las notas cargadas (para facilitar la selección)
        self.cache_notas = {}

        # Método principal que construye la UI
        self._crear_widgets()
        
        # Carga inicial de alumnos
        self.cargar_alumnos()

    def _crear_widgets(self):
        """
        Crea todos los componentes visuales (widgets) de la interfaz.
        """
        
        # --- Contenedor Principal (Panel dividido) ---
        main_paned_window = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_paned_window.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- Panel Izquierdo: Alumnos ---
        frame_alumnos_master = ttk.Frame(main_paned_window, padding=10)
        main_paned_window.add(frame_alumnos_master, weight=1)

        ttk.Label(frame_alumnos_master, text="Gestión de Alumnos", font=('Arial', 16, 'bold')).pack(pady=5)

        # Formulario de Alumnos
        form_alumnos = ttk.Frame(frame_alumnos_master)
        form_alumnos.pack(fill=tk.X, pady=5)

        ttk.Label(form_alumnos, text="DNI:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_alumno_dni = ttk.Entry(form_alumnos, width=40)
        self.entry_alumno_dni.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_alumnos, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_alumno_nombre = ttk.Entry(form_alumnos, width=40)
        self.entry_alumno_nombre.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_alumnos, text="Apellido:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_alumno_apellido = ttk.Entry(form_alumnos, width=40)
        self.entry_alumno_apellido.grid(row=2, column=1, padx=5, pady=5)

        # Botones de Alumnos
        btn_frame_alumnos = ttk.Frame(frame_alumnos_master)
        btn_frame_alumnos.pack(fill=tk.X, pady=10)

        self.btn_agregar_alumno = ttk.Button(btn_frame_alumnos, text="Agregar", command=self.agregar_alumno)
        self.btn_agregar_alumno.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.btn_modificar_alumno = ttk.Button(btn_frame_alumnos, text="Modificar", command=self.modificar_alumno)
        self.btn_modificar_alumno.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.btn_eliminar_alumno = ttk.Button(btn_frame_alumnos, text="Eliminar", command=self.eliminar_alumno)
        self.btn_eliminar_alumno.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.btn_limpiar_alumno = ttk.Button(btn_frame_alumnos, text="Limpiar", command=self.limpiar_campos_alumno)
        self.btn_limpiar_alumno.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Tabla de Alumnos (Treeview)
        tree_frame_alumnos = ttk.Frame(frame_alumnos_master)
        tree_frame_alumnos.pack(fill=tk.BOTH, expand=True, pady=10)

        cols_alumnos = ('dni', 'nombre', 'apellido')
        self.tree_alumnos = ttk.Treeview(tree_frame_alumnos, columns=cols_alumnos, show='headings')
        
        self.tree_alumnos.heading('dni', text='DNI')
        self.tree_alumnos.heading('nombre', text='Nombre')
        self.tree_alumnos.heading('apellido', text='Apellido')
        
        self.tree_alumnos.column('dni', width=100)
        self.tree_alumnos.column('nombre', width=150)
        self.tree_alumnos.column('apellido', width=150)

        # Scrollbar para la tabla de alumnos
        scrollbar_alumnos = ttk.Scrollbar(tree_frame_alumnos, orient=tk.VERTICAL, command=self.tree_alumnos.yview)
        self.tree_alumnos.configure(yscrollcommand=scrollbar_alumnos.set)
        
        scrollbar_alumnos.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_alumnos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Evento de selección
        self.tree_alumnos.bind('<<TreeviewSelect>>', self.seleccionar_alumno)

        
        # --- Panel Derecho: Notas ---
        # Guardamos la referencia para poder activarlo/desactivarlo
        self.frame_notas_master = ttk.Frame(main_paned_window, padding=10)
        main_paned_window.add(self.frame_notas_master, weight=1)

        self.lbl_notas_titulo = ttk.Label(self.frame_notas_master, text="Notas (Seleccione un Alumno)", font=('Arial', 16, 'bold'))
        self.lbl_notas_titulo.pack(pady=5)

        # Formulario de Notas
        form_notas = ttk.Frame(self.frame_notas_master)
        form_notas.pack(fill=tk.X, pady=5)

        ttk.Label(form_notas, text="ID Materia:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nota_materia = ttk.Entry(form_notas, width=40)
        self.entry_nota_materia.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_notas, text="Calificación:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nota_calificacion = ttk.Entry(form_notas, width=40)
        self.entry_nota_calificacion.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(form_notas, text="ID Año:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nota_anio = ttk.Entry(form_notas, width=40)
        self.entry_nota_anio.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(form_notas, text="ID Estado:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nota_estado = ttk.Entry(form_notas, width=40)
        self.entry_nota_estado.grid(row=3, column=1, padx=5, pady=5)

        # Botones de Notas
        btn_frame_notas = ttk.Frame(self.frame_notas_master)
        btn_frame_notas.pack(fill=tk.X, pady=10)

        self.btn_agregar_nota = ttk.Button(btn_frame_notas, text="Agregar", command=self.agregar_nota)
        self.btn_agregar_nota.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.btn_modificar_nota = ttk.Button(btn_frame_notas, text="Modificar", command=self.modificar_nota)
        self.btn_modificar_nota.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.btn_eliminar_nota = ttk.Button(btn_frame_notas, text="Eliminar", command=self.eliminar_nota)
        self.btn_eliminar_nota.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.btn_limpiar_nota = ttk.Button(btn_frame_notas, text="Limpiar", command=self.limpiar_campos_nota)
        self.btn_limpiar_nota.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Tabla de Notas (Treeview)
        tree_frame_notas = ttk.Frame(self.frame_notas_master)
        tree_frame_notas.pack(fill=tk.BOTH, expand=True, pady=10)

        cols_notas = ('materia', 'anio', 'calificacion', 'estado')
        self.tree_notas = ttk.Treeview(tree_frame_notas, columns=cols_notas, show='headings')
        
        self.tree_notas.heading('materia', text='Materia')
        self.tree_notas.heading('anio', text='Año')
        self.tree_notas.heading('calificacion', text='Calificación')
        self.tree_notas.heading('estado', text='Estado')
        
        self.tree_notas.column('materia', width=200)
        self.tree_notas.column('anio', width=80)
        self.tree_notas.column('calificacion', width=80, anchor=tk.CENTER)
        self.tree_notas.column('estado', width=100)

        # Scrollbar para la tabla de notas
        scrollbar_notas = ttk.Scrollbar(tree_frame_notas, orient=tk.VERTICAL, command=self.tree_notas.yview)
        self.tree_notas.configure(yscrollcommand=scrollbar_notas.set)
        
        scrollbar_notas.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_notas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Evento de selección
        self.tree_notas.bind('<<TreeviewSelect>>', self.seleccionar_nota)

        # Desactivar el panel de notas al inicio
        self.desactivar_panel_notas(True)


    # --- MÓDULOS DE LÓGICA PARA ALUMNOS ---

    def cargar_alumnos(self):
        """
        Limpia la tabla de alumnos y la vuelve a cargar con datos frescos
        de la base de datos.
        """
        # Limpiar tabla
        for item in self.tree_alumnos.get_children():
            self.tree_alumnos.delete(item)
            
        # Obtener y cargar alumnos
        try:
            alumnos = self.alumno_service.obtener_alumnos()
            for alumno in alumnos:
                # Usamos el 'id' del alumno como 'iid' (ID interno) en el Treeview
                self.tree_alumnos.insert('', 'end', iid=alumno.id, values=(alumno.dni, alumno.nombre, alumno.apellido))
        except Exception as e:
            self._mostrar_error("Error al Cargar", f"No se pudieron cargar los alumnos: {e}")

    def seleccionar_alumno(self, event):
        """
        Se activa al hacer clic en un alumno en la tabla.
        Guarda el alumno seleccionado y carga sus notas.
        """
        try:
            selected_item_id = self.tree_alumnos.focus()
            if not selected_item_id:
                return

            # Obtener los datos del item seleccionado
            item = self.tree_alumnos.item(selected_item_id)
            values = item['values']
            
            # Crear un objeto Alumno para guardarlo en estado
            # El ID es el 'iid' que definimos al insertar
            self.alumno_seleccionado = Alumno(
                id=int(selected_item_id),
                dni=values[0],
                nombre=values[1],
                apellido=values[2]
            )

            # Rellenar el formulario de alumnos
            self.entry_alumno_dni.delete(0, tk.END)
            self.entry_alumno_dni.insert(0, self.alumno_seleccionado.dni)
            self.entry_alumno_nombre.delete(0, tk.END)
            self.entry_alumno_nombre.insert(0, self.alumno_seleccionado.nombre)
            self.entry_alumno_apellido.delete(0, tk.END)
            self.entry_alumno_apellido.insert(0, self.alumno_seleccionado.apellido)

            # Activar y cargar el panel de notas
            self.desactivar_panel_notas(False)
            self.lbl_notas_titulo.config(text=f"Notas de: {self.alumno_seleccionado.nombre} {self.alumno_seleccionado.apellido}")
            self.cargar_notas_por_alumno()

        except Exception as e:
            self._mostrar_error("Error de Selección", f"Error al seleccionar alumno: {e}")
            self.limpiar_campos_alumno()

    def agregar_alumno(self):
        """
        Recoge los datos del formulario de alumnos, los valida y llama al
        servicio para crear un nuevo alumno.
        """
        # Recoger datos
        dni = self.entry_alumno_dni.get()
        nombre = self.entry_alumno_nombre.get()
        apellido = self.entry_alumno_apellido.get()

        # Validar
        if not dni or not nombre or not apellido:
            self._mostrar_error("Datos incompletos", "Todos los campos (DNI, Nombre, Apellido) son obligatorios.")
            return
        
        try:
            # Crear objeto y llamar al servicio
            alumno = Alumno(nombre=nombre, apellido=apellido, dni=dni)
            nuevo_id = self.alumno_service.crear_alumno(alumno)

            if nuevo_id:
                self._mostrar_info("Éxito", f"Alumno '{nombre} {apellido}' creado con ID: {nuevo_id}")
                self.cargar_alumnos()
                self.limpiar_campos_alumno()
            else:
                self._mostrar_error("Error en Creación", "No se pudo crear el alumno en la base de datos.")
        
        except Exception as e:
            self._mostrar_error("Error en Creación", f"Error al guardar el alumno: {e}")

    def modificar_alumno(self):
        """
        Recoge los datos del formulario y actualiza al alumno seleccionado.
        """
        if not self.alumno_seleccionado:
            self._mostrar_error("Sin selección", "Por favor, seleccione un alumno de la lista para modificar.")
            return

        # Recoger datos
        dni = self.entry_alumno_dni.get()
        nombre = self.entry_alumno_nombre.get()
        apellido = self.entry_alumno_apellido.get()

        # Validar
        if not dni or not nombre or not apellido:
            self._mostrar_error("Datos incompletos", "Todos los campos (DNI, Nombre, Apellido) son obligatorios.")
            return

        try:
            # Actualizar el objeto y llamar al servicio
            alumno_actualizado = Alumno(id=self.alumno_seleccionado.id, nombre=nombre, apellido=apellido, dni=dni)
            filas_afectadas = self.alumno_service.actualizar_alumno(alumno_actualizado)

            if filas_afectadas > 0:
                self._mostrar_info("Éxito", "Alumno actualizado correctamente.")
                self.cargar_alumnos()
                self.limpiar_campos_alumno()
            else:
                self._mostrar_error("Error en Modificación", "No se pudo actualizar el alumno (o no hubo cambios).")
        
        except Exception as e:
            self._mostrar_error("Error en Modificación", f"Error al actualizar el alumno: {e}")

    def eliminar_alumno(self):
        """
        Pide confirmación y elimina al alumno seleccionado.
        """
        if not self.alumno_seleccionado:
            self._mostrar_error("Sin selección", "Por favor, seleccione un alumno de la lista para eliminar.")
            return

        # Confirmación
        if not messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de que desea eliminar a {self.alumno_seleccionado.nombre} {self.alumno_seleccionado.apellido}?\n\nESTO ELIMINARÁ TODAS SUS NOTAS ASOCIADAS (por la configuración de la BD)."):
            return

        try:
            filas_afectadas = self.alumno_service.eliminar_alumno(self.alumno_seleccionado.id)

            if filas_afectadas > 0:
                self._mostrar_info("Éxito", "Alumno eliminado correctamente.")
                self.cargar_alumnos()
                self.limpiar_campos_alumno()
            else:
                self._mostrar_error("Error en Eliminación", "No se pudo eliminar el alumno.")
        
        except Exception as e:
            # Manejar error de clave foránea si no está configurado ON DELETE CASCADE
            if "foreign key constraint" in str(e).lower():
                self._mostrar_error("Error de Integridad", f"No se puede eliminar el alumno porque tiene notas asociadas. Primero debe eliminar sus notas.")
            else:
                self._mostrar_error("Error en Eliminación", f"Error al eliminar el alumno: {e}")

    def limpiar_campos_alumno(self):
        """
        Limpia los campos de entrada del formulario de alumnos y la selección.
        """
        self.entry_alumno_dni.delete(0, tk.END)
        self.entry_alumno_nombre.delete(0, tk.END)
        self.entry_alumno_apellido.delete(0, tk.END)
        
        # Deseleccionar item en el treeview
        if self.tree_alumnos.selection():
            self.tree_alumnos.selection_remove(self.tree_alumnos.selection())
        
        self.alumno_seleccionado = None
        
        # Desactivar y limpiar el panel de notas
        self.desactivar_panel_notas(True)
        self.lbl_notas_titulo.config(text="Notas (Seleccione un Alumno)")


    # --- MÓDULOS DE LÓGICA PARA NOTAS ---

    def cargar_notas_por_alumno(self):
        """
        Limpia la tabla de notas y la carga con las notas del alumno
        que esté actualmente seleccionado.
        """
        # Limpiar tabla
        for item in self.tree_notas.get_children():
            self.tree_notas.delete(item)
            
        # Limpiar cache de notas
        self.cache_notas = {}
        
        if not self.alumno_seleccionado:
            return

        try:
            notas = self.nota_service.obtener_notas_por_alumno(self.alumno_seleccionado.id)
            for nota in notas:
                # Usamos el 'id_notas' como 'iid'
                self.tree_notas.insert('', 'end', iid=nota.id_notas, values=(
                    nota.materia,
                    nota.anio,
                    nota.nota_final,
                    nota.estado
                ))
                # Guardamos el objeto completo en el cache
                self.cache_notas[nota.id_notas] = nota
        
        except Exception as e:
            self._mostrar_error("Error al Cargar", f"No se pudieron cargar las notas: {e}")

    def seleccionar_nota(self, event):
        """
        Se activa al hacer clic en una nota en la tabla.
        Guarda la nota seleccionada y llena el formulario de notas.
        """
        try:
            selected_item_id = self.tree_notas.focus()
            if not selected_item_id:
                return

            # Obtenemos el objeto Nota completo desde el cache
            self.nota_seleccionada = self.cache_notas.get(int(selected_item_id))
            if not self.nota_seleccionada:
                return # No se encontró en el cache, raro

            # Rellenar el formulario de notas con los IDs
            self.entry_nota_materia.delete(0, tk.END)
            self.entry_nota_materia.insert(0, self.nota_seleccionada.id_materias)
            
            self.entry_nota_calificacion.delete(0, tk.END)
            self.entry_nota_calificacion.insert(0, self.nota_seleccionada.nota_final)
            
            self.entry_nota_anio.delete(0, tk.END)
            self.entry_nota_anio.insert(0, self.nota_seleccionada.id_anios)
            
            self.entry_nota_estado.delete(0, tk.END)
            self.entry_nota_estado.insert(0, self.nota_seleccionada.id_estados)

        except Exception as e:
            self._mostrar_error("Error de Selección", f"Error al seleccionar la nota: {e}")
            self.limpiar_campos_nota()

    def agregar_nota(self):
        """
        Recoge los datos del formulario de notas y crea una nueva nota
        para el alumno seleccionado.
        """
        if not self.alumno_seleccionado:
            self._mostrar_error("Sin Alumno", "Debe seleccionar un alumno para agregarle una nota.")
            return

        # Recoger datos
        try:
            id_materia = int(self.entry_nota_materia.get())
            nota_final = float(self.entry_nota_calificacion.get())
            id_anio = int(self.entry_nota_anio.get())
            id_estado = int(self.entry_nota_estado.get())
        except ValueError:
            self._mostrar_error("Datos Inválidos", "Los campos de ID deben ser números enteros y la calificación debe ser un número.")
            return

        try:
            # Crear objeto Nota y llamar al servicio
            nueva_nota = Nota(
                id_alumnos=self.alumno_seleccionado.id,
                id_materias=id_materia,
                nota_final=nota_final,
                id_anios=id_anio,
                id_estados=id_estado
            )
            
            nuevo_id = self.nota_service.crear_nota(nueva_nota)
            
            if nuevo_id:
                self._mostrar_info("Éxito", f"Nueva nota agregada con ID: {nuevo_id}")
                self.cargar_notas_por_alumno()
                self.limpiar_campos_nota()
            else:
                self._mostrar_error("Error en Creación", "No se pudo crear la nota.")
        
        except Exception as e:
            self._mostrar_error("Error en Creación", f"Error al guardar la nota: {e}")

    def modificar_nota(self):
        """
        Recoge los datos del formulario y actualiza la nota seleccionada.
        """
        if not self.nota_seleccionada:
            self._mostrar_error("Sin selección", "Por favor, seleccione una nota de la lista para modificar.")
            return

        # Recoger datos
        try:
            id_materia = int(self.entry_nota_materia.get())
            nota_final = float(self.entry_nota_calificacion.get())
            id_anio = int(self.entry_nota_anio.get())
            id_estado = int(self.entry_nota_estado.get())
        except ValueError:
            self._mostrar_error("Datos Inválidos", "Los campos de ID deben ser números enteros y la calificación debe ser un número.")
            return

        try:
            # Crear objeto Nota actualizado
            nota_actualizada = Nota(
                id_notas=self.nota_seleccionada.id_notas,
                id_alumnos=self.nota_seleccionada.id_alumnos, # Mismo alumno
                id_materias=id_materia,
                nota_final=nota_final,
                id_anios=id_anio,
                id_estados=id_estado
            )
            
            filas_afectadas = self.nota_service.actualizar_nota(nota_actualizada)

            if filas_afectadas > 0:
                self._mostrar_info("Éxito", "Nota actualizada correctamente.")
                self.cargar_notas_por_alumno()
                self.limpiar_campos_nota()
            else:
                self._mostrar_error("Error en Modificación", "No se pudo actualizar la nota (o no hubo cambios).")
        
        except Exception as e:
            self._mostrar_error("Error en Modificación", f"Error al actualizar la nota: {e}")

    def eliminar_nota(self):
        """
        Pide confirmación y elimina la nota seleccionada.
        """
        if not self.nota_seleccionada:
            self._mostrar_error("Sin selección", "Por favor, seleccione una nota de la lista para eliminar.")
            return

        # Confirmación
        if not messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de que desea eliminar la nota seleccionada?"):
            return

        try:
            filas_afectadas = self.nota_service.eliminar_nota(self.nota_seleccionada.id_notas)

            if filas_afectadas > 0:
                self._mostrar_info("Éxito", "Nota eliminada correctamente.")
                self.cargar_notas_por_alumno()
                self.limpiar_campos_nota()
            else:
                self._mostrar_error("Error en Eliminación", "No se pudo eliminar la nota.")
        
        except Exception as e:
            self._mostrar_error("Error en Eliminación", f"Error al eliminar la nota: {e}")

    def limpiar_campos_nota(self):
        """
        Limpia los campos de entrada del formulario de notas.
        """
        self.entry_nota_materia.delete(0, tk.END)
        self.entry_nota_calificacion.delete(0, tk.END)
        self.entry_nota_anio.delete(0, tk.END)
        self.entry_nota_estado.delete(0, tk.END)
        
        # Deseleccionar item en el treeview
        if self.tree_notas.selection():
            self.tree_notas.selection_remove(self.tree_notas.selection())
        
        self.nota_seleccionada = None

    # --- MÓDULOS AUXILIARES ---

    def desactivar_panel_notas(self, desactivar):
        """
        Desactiva o activa todos los widgets del panel de notas.
        """
        estado = tk.DISABLED if desactivar else tk.NORMAL
        
        for child in self.frame_notas_master.winfo_children():
            # No desactivar la etiqueta del título
            if child == self.lbl_notas_titulo:
                continue
            
            # Recorrer widgets anidados (frames de formulario, botones, tabla)
            if isinstance(child, (ttk.Frame, ttk.PanedWindow)):
                for widget in child.winfo_children():
                    try:
                        widget.config(state=estado)
                    except tk.TclError:
                        pass # Algunos widgets como Scrollbar no tienen 'state'
            else:
                try:
                    child.config(state=estado)
                except tk.TclError:
                    pass

        if desactivar:
            self.limpiar_campos_nota()
            # Limpiar tabla
            for item in self.tree_notas.get_children():
                self.tree_notas.delete(item)

    def _mostrar_error(self, titulo, mensaje):
        """
Muestra un cuadro de diálogo de error.
        """
        messagebox.showerror(titulo, mensaje, parent=self.root)

    def _mostrar_info(self, titulo, mensaje):
        """
        Muestra un cuadro de diálogo de información.
        """
        messagebox.showinfo(titulo, mensaje, parent=self.root)

