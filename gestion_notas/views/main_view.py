import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from gestion_notas.services.alumno_service import AlumnoService
from gestion_notas.services.nota_service import NotaService
from gestion_notas.services.catalogo_service import CatalogoService
from gestion_notas.models.alumno_model import Alumno
from gestion_notas.models.nota_model import Nota

class MainView:
    """
    Clase principal de la Vista. Construye y gestiona la interfaz gráfica (UI)
    y maneja los eventos de usuario.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Notas")
        self.root.minsize(1000, 600)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Inyección de dependencias (Servicios)
        self.alumno_service = AlumnoService()
        self.nota_service = NotaService()
        self.catalogo_service = CatalogoService()

        # Variables de estado
        self.alumno_seleccionado = None
        self.nota_seleccionada = None
        self.cache_notas = {}
        
        # Mapas para traducción de UI <-> Lógica
        self.materias_map = {}
        self.anios_map = {}
        self.materias_map_inv = {}
        self.anios_map_inv = {}

        self._cargar_catalogos()
        self._crear_widgets()
        self.cargar_alumnos()

    def _cargar_catalogos(self):
        """
        Carga las listas de materias y años desde la BD al iniciar
        para poblar los Combobox y los mapas de traducción.
        """
        try:
            for m in self.catalogo_service.obtener_materias():
                descripcion = str(m['descripcion']).strip() 
                self.materias_map[descripcion] = m['id_materias']
                self.materias_map_inv[m['id_materias']] = descripcion
            
            for a in self.catalogo_service.obtener_anios():
                descripcion = str(a['descripcion']).strip()
                self.anios_map[descripcion] = a['id_anios']
                self.anios_map_inv[a['id_anios']] = descripcion
                
        except Exception as e:
            self._mostrar_error("Error de Catálogos", f"No se pudieron cargar las listas de materias/años: {e}")

    def _crear_widgets(self):
        """
        Construye todos los componentes (widgets) de la interfaz gráfica.
        """
        
        main_paned_window = ttk.Panedwindow(self.root, orient=HORIZONTAL) 
        main_paned_window.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

        # --- Panel Alumnos ---
        frame_alumnos_master = ttk.Frame(main_paned_window, padding=10)
        frame_alumnos_master.columnconfigure(0, weight=1)
        frame_alumnos_master.rowconfigure(2, weight=1) 
        main_paned_window.add(frame_alumnos_master, weight=1)

        ttk.Label(frame_alumnos_master, text="Gestión de Alumnos", font=('Arial', 16, 'bold')).grid(row=0, column=0, pady=5, sticky=W)

        form_alumnos = ttk.Frame(frame_alumnos_master)
        form_alumnos.grid(row=1, column=0, sticky=EW, pady=5)
        form_alumnos.columnconfigure(1, weight=1) 

        ttk.Label(form_alumnos, text="DNI:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.entry_alumno_dni = ttk.Entry(form_alumnos)
        self.entry_alumno_dni.grid(row=0, column=1, padx=5, pady=5, sticky=EW)

        ttk.Label(form_alumnos, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.entry_alumno_nombre = ttk.Entry(form_alumnos)
        self.entry_alumno_nombre.grid(row=1, column=1, padx=5, pady=5, sticky=EW)

        ttk.Label(form_alumnos, text="Apellido:").grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.entry_alumno_apellido = ttk.Entry(form_alumnos)
        self.entry_alumno_apellido.grid(row=2, column=1, padx=5, pady=5, sticky=EW)

        btn_frame_alumnos = ttk.Frame(frame_alumnos_master)
        btn_frame_alumnos.grid(row=3, column=0, sticky=EW, pady=10)
        for i in range(4): btn_frame_alumnos.columnconfigure(i, weight=1)

        self.btn_agregar_alumno = ttk.Button(btn_frame_alumnos, text="Agregar", command=self.agregar_alumno, bootstyle=SUCCESS)
        self.btn_agregar_alumno.grid(row=0, column=0, sticky=EW, padx=5)
        
        self.btn_modificar_alumno = ttk.Button(btn_frame_alumnos, text="Modificar", command=self.modificar_alumno, bootstyle=PRIMARY)
        self.btn_modificar_alumno.grid(row=0, column=1, sticky=EW, padx=5)
        
        self.btn_eliminar_alumno = ttk.Button(btn_frame_alumnos, text="Eliminar", command=self.eliminar_alumno, bootstyle=DANGER)
        self.btn_eliminar_alumno.grid(row=0, column=2, sticky=EW, padx=5)
        
        self.btn_limpiar_alumno = ttk.Button(btn_frame_alumnos, text="Limpiar", command=self.limpiar_campos_alumno, bootstyle=SECONDARY)
        self.btn_limpiar_alumno.grid(row=0, column=3, sticky=EW, padx=5)

        tree_frame_alumnos = ttk.Frame(frame_alumnos_master)
        tree_frame_alumnos.grid(row=2, column=0, sticky=NSEW, pady=10)
        tree_frame_alumnos.columnconfigure(0, weight=1)
        tree_frame_alumnos.rowconfigure(0, weight=1)

        cols_alumnos = ('dni', 'nombre', 'apellido')
        self.tree_alumnos = ttk.Treeview(tree_frame_alumnos, columns=cols_alumnos, show='headings', bootstyle=PRIMARY)
        
        self.tree_alumnos.heading('dni', text='DNI')
        self.tree_alumnos.heading('nombre', text='Nombre')
        self.tree_alumnos.heading('apellido', text='Apellido')
        self.tree_alumnos.column('dni', width=100)
        self.tree_alumnos.column('nombre', width=150)
        self.tree_alumnos.column('apellido', width=150)

        scrollbar_alumnos = ttk.Scrollbar(tree_frame_alumnos, orient=VERTICAL, command=self.tree_alumnos.yview)
        self.tree_alumnos.configure(yscrollcommand=scrollbar_alumnos.set)
        
        self.tree_alumnos.grid(row=0, column=0, sticky=NSEW)
        scrollbar_alumnos.grid(row=0, column=1, sticky=NS)

        self.tree_alumnos.bind('<<TreeviewSelect>>', self.seleccionar_alumno)

        
        # --- Panel Notas ---
        self.frame_notas_master = ttk.Frame(main_paned_window, padding=10)
        self.frame_notas_master.columnconfigure(0, weight=1)
        self.frame_notas_master.rowconfigure(2, weight=1) 
        main_paned_window.add(self.frame_notas_master, weight=1)

        self.lbl_notas_titulo = ttk.Label(self.frame_notas_master, text="Notas (Seleccione un Alumno)", font=('Arial', 16, 'bold'))
        self.lbl_notas_titulo.grid(row=0, column=0, pady=5, sticky=W)

        form_notas = ttk.Frame(self.frame_notas_master)
        form_notas.grid(row=1, column=0, sticky=EW, pady=5)
        form_notas.columnconfigure(1, weight=1)
        
        ttk.Label(form_notas, text="Materia:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.combo_nota_materia = ttk.Combobox(form_notas, values=list(self.materias_map.keys()), state="readonly")
        self.combo_nota_materia.grid(row=0, column=1, padx=5, pady=5, sticky=EW)

        ttk.Label(form_notas, text="Calificación:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.entry_nota_calificacion = ttk.Entry(form_notas)
        self.entry_nota_calificacion.grid(row=1, column=1, padx=5, pady=5, sticky=EW)
        
        ttk.Label(form_notas, text="Año:").grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.combo_nota_anio = ttk.Combobox(form_notas, values=list(self.anios_map.keys()), state="readonly")
        self.combo_nota_anio.grid(row=2, column=1, padx=5, pady=5, sticky=EW)

        btn_frame_notas = ttk.Frame(self.frame_notas_master)
        btn_frame_notas.grid(row=3, column=0, sticky=EW, pady=10)
        for i in range(4): btn_frame_notas.columnconfigure(i, weight=1)

        self.btn_agregar_nota = ttk.Button(btn_frame_notas, text="Agregar", command=self.agregar_nota, bootstyle=SUCCESS)
        self.btn_agregar_nota.grid(row=0, column=0, sticky=EW, padx=5)
        
        self.btn_modificar_nota = ttk.Button(btn_frame_notas, text="Modificar", command=self.modificar_nota, bootstyle=PRIMARY)
        self.btn_modificar_nota.grid(row=0, column=1, sticky=EW, padx=5)
        
        self.btn_eliminar_nota = ttk.Button(btn_frame_notas, text="Eliminar", command=self.eliminar_nota, bootstyle=DANGER)
        self.btn_eliminar_nota.grid(row=0, column=2, sticky=EW, padx=5)
        
        self.btn_limpiar_nota = ttk.Button(btn_frame_notas, text="Limpiar", command=self.limpiar_campos_nota, bootstyle=SECONDARY)
        self.btn_limpiar_nota.grid(row=0, column=3, sticky=EW, padx=5)

        tree_frame_notas = ttk.Frame(self.frame_notas_master)
        tree_frame_notas.grid(row=2, column=0, sticky=NSEW, pady=10)
        tree_frame_notas.columnconfigure(0, weight=1)
        tree_frame_notas.rowconfigure(0, weight=1)

        cols_notas = ('materia', 'anio', 'calificacion', 'estado')
        self.tree_notas = ttk.Treeview(tree_frame_notas, columns=cols_notas, show='headings', bootstyle=PRIMARY)
        
        self.tree_notas.heading('materia', text='Materia')
        self.tree_notas.heading('anio', text='Año')
        self.tree_notas.heading('calificacion', text='Calificación')
        self.tree_notas.heading('estado', text='Estado')
        
        self.tree_notas.column('materia', width=200)
        self.tree_notas.column('anio', width=80)
        self.tree_notas.column('calificacion', width=80, anchor=CENTER)
        self.tree_notas.column('estado', width=100)

        scrollbar_notas = ttk.Scrollbar(tree_frame_notas, orient=VERTICAL, command=self.tree_notas.yview)
        self.tree_notas.configure(yscrollcommand=scrollbar_notas.set)
        
        self.tree_notas.grid(row=0, column=0, sticky=NSEW)
        scrollbar_notas.grid(row=0, column=1, sticky=NS)

        self.tree_notas.bind('<<TreeviewSelect>>', self.seleccionar_nota)

        self.desactivar_panel_notas(True)

    
    # --- Controladores de Eventos: Alumnos ---
    
    def cargar_alumnos(self):
        """
        Refresca la tabla de alumnos con los datos 'activos' de la BD.
        """
        for item in self.tree_alumnos.get_children():
            self.tree_alumnos.delete(item)
        try:
            alumnos = self.alumno_service.obtener_alumnos()
            for alumno in alumnos:
                self.tree_alumnos.insert('', 'end', iid=alumno.id, values=(alumno.dni, alumno.nombre, alumno.apellido))
        except Exception as e:
            self._mostrar_error("Error al Cargar", f"No se pudieron cargar los alumnos: {e}")

    def seleccionar_alumno(self, event):
        """
        Evento: Se dispara al hacer clic en un alumno.
        Carga los datos del alumno en el formulario y refresca el panel de notas.
        """
        try:
            selected_item_id = self.tree_alumnos.focus()
            if not selected_item_id:
                return
            
            item = self.tree_alumnos.item(selected_item_id)
            values = item['values']
            self.alumno_seleccionado = Alumno(
                id=int(selected_item_id),
                dni=values[0],
                nombre=values[1],
                apellido=values[2]
            )
            
            self.entry_alumno_dni.delete(0, END)
            self.entry_alumno_dni.insert(0, self.alumno_seleccionado.dni)
            self.entry_alumno_nombre.delete(0, END)
            self.entry_alumno_nombre.insert(0, self.alumno_seleccionado.nombre)
            self.entry_alumno_apellido.delete(0, END)
            self.entry_alumno_apellido.insert(0, self.alumno_seleccionado.apellido)
            
            self.desactivar_panel_notas(False)
            self.lbl_notas_titulo.config(text=f"Notas de: {self.alumno_seleccionado.nombre} {self.alumno_seleccionado.apellido}")
            self.cargar_notas_por_alumno()
        except Exception as e:
            self._mostrar_error("Error de Selección", f"Error al seleccionar alumno: {e}")
            self.limpiar_campos_alumno()

    def agregar_alumno(self):
        """
        Controlador: Valida los datos del formulario y crea un nuevo alumno.
        """
        dni = self.entry_alumno_dni.get()
        nombre = self.entry_alumno_nombre.get()
        apellido = self.entry_alumno_apellido.get()
        
        if not dni or not nombre or not apellido:
            self._mostrar_error("Datos incompletos", "Todos los campos (DNI, Nombre, Apellido) son obligatorios.")
            return
        try:
            int(dni)
        except ValueError:
            self._mostrar_error("Dato Inválido", "El campo DNI debe ser numérico.")
            return
            
        try:
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
        Controlador: Valida los datos y actualiza el alumno seleccionado.
        """
        if not self.alumno_seleccionado:
            self._mostrar_error("Sin selección", "Por favor, seleccione un alumno de la lista para modificar.")
            return
            
        dni = self.entry_alumno_dni.get()
        nombre = self.entry_alumno_nombre.get()
        apellido = self.entry_alumno_apellido.get()
        
        if not dni or not nombre or not apellido:
            self._mostrar_error("Datos incompletos", "Todos los campos (DNI, Nombre, Apellido) son obligatorios.")
            return
        try:
            int(dni)
        except ValueError:
            self._mostrar_error("Dato Inválido", "El campo DNI debe ser numérico.")
            return
            
        try:
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
        Controlador: Pide confirmación y realiza el borrado lógico del alumno.
        """
        if not self.alumno_seleccionado:
            self._mostrar_error("Sin selección", "Por favor, seleccione un alumno de la lista para eliminar.")
            return
        
        if not messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de que desea eliminar a {self.alumno_seleccionado.nombre} {self.alumno_seleccionado.apellido}?\n\nEl alumno se marcará como inactivo y se ocultará de la lista."):
            return

        try:
            filas_afectadas = self.alumno_service.eliminar_alumno(self.alumno_seleccionado.id)

            if filas_afectadas > 0:
                self._mostrar_info("Éxito", "Alumno eliminado (marcado como inactivo) correctamente.")
                self.cargar_alumnos()
                self.limpiar_campos_alumno()
            else:
                self._mostrar_error("Error en Eliminación", "No se pudo eliminar el alumno.")
        
        except Exception as e:
            self._mostrar_error("Error en Eliminación", f"Error al eliminar el alumno: {e}")

    def limpiar_campos_alumno(self):
        """
        Controlador: Resetea el formulario de alumnos y el estado de la UI.
        """
        self.entry_alumno_dni.delete(0, END)
        self.entry_alumno_nombre.delete(0, END)
        self.entry_alumno_apellido.delete(0, END)
        
        if self.tree_alumnos.selection():
            self.tree_alumnos.selection_remove(self.tree_alumnos.selection())
            
        self.alumno_seleccionado = None
        self.desactivar_panel_notas(True)
        self.lbl_notas_titulo.config(text="Notas (Seleccione un Alumno)")


    # --- Controladores de Eventos: Notas ---

    def cargar_notas_por_alumno(self):
        """
        Refresca la tabla de notas con los datos del alumno seleccionado.
        """
        for item in self.tree_notas.get_children():
            self.tree_notas.delete(item)
        self.cache_notas = {}
        
        if not self.alumno_seleccionado:
            return
            
        try:
            notas = self.nota_service.obtener_notas_por_alumno(self.alumno_seleccionado.id)
            for nota in notas:
                self.tree_notas.insert('', 'end', iid=nota.id_notas, values=(
                    nota.materia,
                    nota.anio,
                    nota.nota_final,
                    nota.estado
                ))
                # Guardar el objeto nota completo en un cache para fácil acceso
                self.cache_notas[nota.id_notas] = nota
        except Exception as e:
            self._mostrar_error("Error al Cargar", f"No se pudieron cargar las notas: {e}")

    def seleccionar_nota(self, event):
        """
        Evento: Se dispara al hacer clic en una nota.
        Carga los datos de la nota en el formulario.
        """
        try:
            selected_item_id = self.tree_notas.focus()
            if not selected_item_id:
                return
                
            self.nota_seleccionada = self.cache_notas.get(int(selected_item_id))
            if not self.nota_seleccionada:
                return
            
            self.entry_nota_calificacion.delete(0, END)
            self.entry_nota_calificacion.insert(0, self.nota_seleccionada.nota_final)
            
            # Traducir los IDs a los nombres para los Combobox
            materia_nombre = self.materias_map_inv.get(self.nota_seleccionada.id_materias)
            anio_nombre = self.anios_map_inv.get(self.nota_seleccionada.id_anios)
            
            self.combo_nota_materia.set(materia_nombre if materia_nombre else "")
            self.combo_nota_anio.set(anio_nombre if anio_nombre else "")

        except Exception as e:
            self._mostrar_error("Error de Selección", f"Error al seleccionar la nota: {e}")
            self.limpiar_campos_nota()

    def agregar_nota(self):
        """
        Controlador: Valida los datos del formulario de nota y los pasa al servicio.
        """
        if not self.alumno_seleccionado:
            self._mostrar_error("Sin Alumno", "Debe seleccionar un alumno para agregarle una nota.")
            return

        try:
            materia_nombre = self.combo_nota_materia.get()
            anio_nombre = self.combo_nota_anio.get()
            calificacion_str = self.entry_nota_calificacion.get()
            
            if not materia_nombre or not anio_nombre or not calificacion_str:
                self._mostrar_error("Datos Incompletos", "Debe seleccionar una Materia, Año y poner una Calificación.")
                return
            
            nota_final = float(calificacion_str)
            id_materia = self.materias_map[materia_nombre]
            id_anio = self.anios_map[anio_nombre]

        except ValueError:
            self._mostrar_error("Dato Inválido", "La calificación debe ser un número (ej: 8.5).")
            return
        except KeyError:
            self._mostrar_error("Dato Inválido", "Asegúrese de seleccionar valores válidos de las listas.")
            return
        
        if not (1 <= nota_final <= 10):
            self._mostrar_error("Rango Inválido", "La calificación debe estar entre 1 y 10.")
            return
        
        try:
            nueva_nota = Nota(
                id_alumnos=self.alumno_seleccionado.id,
                id_materias=id_materia,
                nota_final=nota_final,
                id_anios=id_anio
            )
            
            nuevo_id = self.nota_service.crear_nota(nueva_nota)
            
            if nuevo_id:
                self._mostrar_info("Éxito", f"Nueva nota agregada con ID: {nuevo_id}.")
                self.cargar_notas_por_alumno()
                self.limpiar_campos_nota()
            else:
                self._mostrar_error("Error en Creación", "No se pudo crear la nota. Verifique la consola para más detalles.")
        
        except Exception as e:
            self._mostrar_error("Error en Creación", f"Error al guardar la nota: {e}")

    def modificar_nota(self):
        """
        Controlador: Valida los datos y actualiza la nota seleccionada.
        """
        if not self.nota_seleccionada:
            self._mostrar_error("Sin selección", "Por favor, seleccione una nota de la lista para modificar.")
            return

        try:
            materia_nombre = self.combo_nota_materia.get()
            anio_nombre = self.combo_nota_anio.get()
            calificacion_str = self.entry_nota_calificacion.get()

            if not materia_nombre or not anio_nombre or not calificacion_str:
                self._mostrar_error("Datos Incompletos", "Debe seleccionar una Materia, Año y poner una Calificación.")
                return

            nota_final = float(calificacion_str)
            id_materia = self.materias_map[materia_nombre]
            id_anio = self.anios_map[anio_nombre]
            
        except ValueError:
            self._mostrar_error("Dato Inválido", "La calificación debe ser un número (ej: 8.5).")
            return
        except KeyError:
            self._mostrar_error("Dato Inválido", "Asegúrese de seleccionar valores válidos de las listas.")
            return

        if not (1 <= nota_final <= 10):
            self._mostrar_error("Rango Inválido", "La calificación debe estar entre 1 y 10.")
            return
        
        try:
            nota_actualizada = Nota(
                id_notas=self.nota_seleccionada.id_notas,
                id_alumnos=self.nota_seleccionada.id_alumnos,
                id_materias=id_materia,
                nota_final=nota_final,
                id_anios=id_anio
            )
            
            filas_afectadas = self.nota_service.actualizar_nota(nota_actualizada)
            
            if filas_afectadas > 0:
                self._mostrar_info("Éxito", f"Nota actualizada correctamente.")
                self.cargar_notas_por_alumno()
                self.limpiar_campos_nota()
            else:
                self._mostrar_error("Error en Modificación", "No se pudo actualizar el alumno (o no hubo cambios).")
        
        except Exception as e:
            self._mostrar_error("Error en Modificación", f"Error al actualizar la nota: {e}")

    def eliminar_nota(self):
        """
        Controlador: Pide confirmación y elimina permanentemente la nota seleccionada.
        """
        if not self.nota_seleccionada:
            self._mostrar_error("Sin selección", "Por favor, seleccione una nota de la lista para eliminar.")
            return
            
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
            self.log_error(f"Error al eliminar la nota: {e}")
            self._mostrar_error("Error en Eliminación", f"Error al eliminar la nota: {e}")

    def limpiar_campos_nota(self):
        """
        Controlador: Resetea el formulario de notas.
        """
        self.entry_nota_calificacion.delete(0, END)
        self.combo_nota_materia.set("")
        self.combo_nota_anio.set("")
        
        if self.tree_notas.selection():
            self.tree_notas.selection_remove(self.tree_notas.selection())
        self.nota_seleccionada = None

    # --- Métodos Auxiliares ---

    def desactivar_panel_notas(self, desactivar):
        """
        Activa o desactiva la interacción con todo el panel de notas.
        """
        estado = DISABLED if desactivar else NORMAL 
        
        for child in self.frame_notas_master.winfo_children():
            if child == self.lbl_notas_titulo:
                continue
            
            if isinstance(child, (ttk.Frame, ttk.Panedwindow)):
                for widget in child.winfo_children():
                    try:
                        if 'state' in widget.keys():
                            widget.config(state=estado)
                    except tk.TclError:
                        pass # Algunos widgets (ej: Scrollbar) no tienen 'state'
            else:
                try:
                    if 'state' in child.keys():
                        child.config(state=estado)
                except tk.TclError:
                    pass
                    
        if desactivar:
            self.limpiar_campos_nota()
            for item in self.tree_notas.get_children():
                self.tree_notas.delete(item)

    def _mostrar_error(self, titulo, mensaje):
        """Muestra un popup de error."""
        messagebox.showerror(titulo, mensaje, parent=self.root)

    def _mostrar_info(self, titulo, mensaje):
        """Muestra un popup de información."""
        messagebox.showinfo(titulo, mensaje, parent=self.root)