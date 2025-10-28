import tkinter as tk
from tkinter import ttk, messagebox
from services.alumno_service import AlumnoService
from services.materia_service import MateriaService
from services.anio_service import AnioService
from services.estado_service import EstadoService
from services.nota_service import NotaService
from models.alumno_model import Alumno
from models.materia_model import Materia
from models.nota_model import Nota


class MainView:
    """
    Vista principal del sistema de gestión de notas
    """
    # Colores profesionales
    COLOR_PRIMARY = "#1E3A5F"      # Azul oscuro profesional
    COLOR_SECONDARY = "#2E5984"    # Azul medio
    COLOR_ACCENT = "#4A7BA7"       # Azul claro
    COLOR_BG = "#F5F6FA"           # Gris muy claro
    COLOR_WHITE = "#FFFFFF"        # Blanco
    COLOR_TEXT = "#2C3E50"         # Texto oscuro
    COLOR_SUCCESS = "#27AE60"      # Verde éxito
    COLOR_DANGER = "#E74C3C"       # Rojo peligro
    COLOR_WARNING = "#F39C12"      # Amarillo advertencia
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Notas - ITEC Nº 3")
        self.root.geometry("1400x800")
        self.root.configure(bg=self.COLOR_BG)
        
        # Servicios
        self.alumno_service = AlumnoService()
        self.materia_service = MateriaService()
        self.anio_service = AnioService()
        self.estado_service = EstadoService()
        self.nota_service = NotaService()
        
        # Variables de estado
        self.alumno_seleccionado = None
        self.nota_seleccionada = None
        
        # Crear interfaz
        self._crear_estilo()
        self._crear_interfaz()
        
        # Cargar datos iniciales
        self.cargar_datos_iniciales()
    
    def _crear_estilo(self):
        """Configura el estilo visual de la aplicación"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar estilo de notebook (pestañas)
        style.configure('TNotebook', background=self.COLOR_BG, borderwidth=0)
        style.configure('TNotebook.Tab', 
                       background=self.COLOR_SECONDARY,
                       foreground=self.COLOR_WHITE,
                       padding=[20, 10],
                       font=('Segoe UI', 10, 'bold'))
        style.map('TNotebook.Tab',
                 background=[('selected', self.COLOR_PRIMARY)],
                 foreground=[('selected', self.COLOR_WHITE)])
        
        # Configurar estilo de frames
        style.configure('Card.TFrame', background=self.COLOR_WHITE, relief='flat')
        
        # Configurar estilo de labels
        style.configure('Title.TLabel', 
                       background=self.COLOR_PRIMARY,
                       foreground=self.COLOR_WHITE,
                       font=('Segoe UI', 14, 'bold'),
                       padding=10)
        
        style.configure('Subtitle.TLabel',
                       background=self.COLOR_WHITE,
                       foreground=self.COLOR_TEXT,
                       font=('Segoe UI', 10, 'bold'))
        
        style.configure('Normal.TLabel',
                       background=self.COLOR_WHITE,
                       foreground=self.COLOR_TEXT,
                       font=('Segoe UI', 9))
    
    def _crear_interfaz(self):
        """Crea la interfaz principal"""
        # Frame principal
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Header
        header = tk.Frame(main_container, bg=self.COLOR_PRIMARY, height=80)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)
        
        title_label = tk.Label(header,
                              text="SISTEMA DE GESTIÓN DE NOTAS",
                              bg=self.COLOR_PRIMARY,
                              fg=self.COLOR_WHITE,
                              font=('Segoe UI', 20, 'bold'))
        title_label.pack(side=tk.LEFT, padx=30, pady=20)
        
        subtitle_label = tk.Label(header,
                                 text="ITEC Nº 3 - Instituto Técnico",
                                 bg=self.COLOR_PRIMARY,
                                 fg=self.COLOR_ACCENT,
                                 font=('Segoe UI', 11))
        subtitle_label.pack(side=tk.LEFT, padx=10)
        
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Crear pestañas
        self._crear_pestaña_alumnos()
        self._crear_pestaña_notas()
        self._crear_pestaña_configuracion()
    
    def _crear_pestaña_alumnos(self):
        """Crea la pestaña de gestión de alumnos"""
        tab_alumnos = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tab_alumnos, text='📚 ALUMNOS')
        
        # Panel izquierdo - Formulario
        left_panel = tk.Frame(tab_alumnos, bg=self.COLOR_WHITE, width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        left_panel.pack_propagate(False)
        
        # Título del formulario
        form_title = tk.Label(left_panel,
                             text="REGISTRO DE ALUMNO",
                             bg=self.COLOR_SECONDARY,
                             fg=self.COLOR_WHITE,
                             font=('Segoe UI', 12, 'bold'),
                             pady=10)
        form_title.pack(fill=tk.X)
        
        # Formulario
        form_frame = tk.Frame(left_panel, bg=self.COLOR_WHITE)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # ID Alumno
        tk.Label(form_frame, text="ID Alumno:", bg=self.COLOR_WHITE, 
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
        self.entry_id_alumno = tk.Entry(form_frame, font=('Segoe UI', 10), width=30)
        self.entry_id_alumno.grid(row=0, column=1, pady=5, padx=5)
        
        # Nombre
        tk.Label(form_frame, text="Nombre:", bg=self.COLOR_WHITE,
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=1, column=0, sticky='w', pady=5)
        self.entry_nombre_alumno = tk.Entry(form_frame, font=('Segoe UI', 10), width=30)
        self.entry_nombre_alumno.grid(row=1, column=1, pady=5, padx=5)
        
        # Apellido
        tk.Label(form_frame, text="Apellido:", bg=self.COLOR_WHITE,
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=2, column=0, sticky='w', pady=5)
        self.entry_apellido_alumno = tk.Entry(form_frame, font=('Segoe UI', 10), width=30)
        self.entry_apellido_alumno.grid(row=2, column=1, pady=5, padx=5)
        
        # DNI
        tk.Label(form_frame, text="DNI:", bg=self.COLOR_WHITE,
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=3, column=0, sticky='w', pady=5)
        self.entry_dni_alumno = tk.Entry(form_frame, font=('Segoe UI', 10), width=30)
        self.entry_dni_alumno.grid(row=3, column=1, pady=5, padx=5)
        
        # Botones
        btn_frame = tk.Frame(form_frame, bg=self.COLOR_WHITE)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        btn_agregar = tk.Button(btn_frame, text="✓ Agregar", 
                               bg=self.COLOR_SUCCESS, fg=self.COLOR_WHITE,
                               font=('Segoe UI', 9, 'bold'), width=12,
                               cursor='hand2', command=self.agregar_alumno)
        btn_agregar.pack(side=tk.LEFT, padx=5)
        
        btn_modificar = tk.Button(btn_frame, text="✎ Modificar",
                                 bg=self.COLOR_WARNING, fg=self.COLOR_WHITE,
                                 font=('Segoe UI', 9, 'bold'), width=12,
                                 cursor='hand2', command=self.modificar_alumno)
        btn_modificar.pack(side=tk.LEFT, padx=5)
        
        btn_eliminar = tk.Button(btn_frame, text="✗ Eliminar",
                                bg=self.COLOR_DANGER, fg=self.COLOR_WHITE,
                                font=('Segoe UI', 9, 'bold'), width=12,
                                cursor='hand2', command=self.eliminar_alumno)
        btn_eliminar.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = tk.Button(btn_frame, text="⟲ Limpiar",
                               bg=self.COLOR_SECONDARY, fg=self.COLOR_WHITE,
                               font=('Segoe UI', 9, 'bold'), width=12,
                               cursor='hand2', command=self.limpiar_campos_alumno)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        # Panel derecho - Lista de alumnos
        right_panel = tk.Frame(tab_alumnos, bg=self.COLOR_WHITE)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título de la tabla
        table_title = tk.Label(right_panel,
                              text="LISTA DE ALUMNOS",
                              bg=self.COLOR_SECONDARY,
                              fg=self.COLOR_WHITE,
                              font=('Segoe UI', 12, 'bold'),
                              pady=10)
        table_title.pack(fill=tk.X)
        
        # Tabla de alumnos
        tree_frame = tk.Frame(right_panel, bg=self.COLOR_WHITE)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollbars
        scroll_y = tk.Scrollbar(tree_frame)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        scroll_x = tk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Treeview
        self.tree_alumnos = ttk.Treeview(tree_frame,
                                        columns=('ID', 'Apellido', 'Nombre', 'DNI'),
                                        show='headings',
                                        yscrollcommand=scroll_y.set,
                                        xscrollcommand=scroll_x.set,
                                        height=20)
        
        scroll_y.config(command=self.tree_alumnos.yview)
        scroll_x.config(command=self.tree_alumnos.xview)
        
        # Configurar columnas
        self.tree_alumnos.heading('ID', text='ID')
        self.tree_alumnos.heading('Apellido', text='Apellido')
        self.tree_alumnos.heading('Nombre', text='Nombre')
        self.tree_alumnos.heading('DNI', text='DNI')
        
        self.tree_alumnos.column('ID', width=80, anchor='center')
        self.tree_alumnos.column('Apellido', width=200)
        self.tree_alumnos.column('Nombre', width=200)
        self.tree_alumnos.column('DNI', width=120, anchor='center')
        
        # Estilos alternados
        self.tree_alumnos.tag_configure('oddrow', background='#F8F9FA')
        self.tree_alumnos.tag_configure('evenrow', background='#FFFFFF')
        
        self.tree_alumnos.pack(fill=tk.BOTH, expand=True)
        self.tree_alumnos.bind('<<TreeviewSelect>>', self.seleccionar_alumno)
    
    def _crear_pestaña_notas(self):
        """Crea la pestaña de gestión de notas"""
        tab_notas = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tab_notas, text='📝 NOTAS')
        
        # Panel superior - Selección de alumno
        top_panel = tk.Frame(tab_notas, bg=self.COLOR_WHITE, height=100)
        top_panel.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        top_panel.pack_propagate(False)
        
        tk.Label(top_panel,
                text="GESTIÓN DE NOTAS POR ALUMNO",
                bg=self.COLOR_SECONDARY,
                fg=self.COLOR_WHITE,
                font=('Segoe UI', 12, 'bold'),
                pady=10).pack(fill=tk.X)
        
        select_frame = tk.Frame(top_panel, bg=self.COLOR_WHITE)
        select_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(select_frame, text="Seleccionar Alumno:", 
                bg=self.COLOR_WHITE, fg=self.COLOR_TEXT,
                font=('Segoe UI', 10, 'bold')).pack(side=tk.LEFT, padx=10)
        
        self.combo_alumnos = ttk.Combobox(select_frame, state='readonly',
                                         font=('Segoe UI', 10), width=40)
        self.combo_alumnos.pack(side=tk.LEFT, padx=10)
        self.combo_alumnos.bind('<<ComboboxSelected>>', self.alumno_combo_changed)
        
        # Panel central - Contenedor principal
        center_container = tk.Frame(tab_notas, bg=self.COLOR_BG)
        center_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel izquierdo - Formulario de notas
        left_panel = tk.Frame(center_container, bg=self.COLOR_WHITE, width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=5)
        left_panel.pack_propagate(False)
        
        tk.Label(left_panel,
                text="REGISTRO DE NOTA",
                bg=self.COLOR_SECONDARY,
                fg=self.COLOR_WHITE,
                font=('Segoe UI', 11, 'bold'),
                pady=10).pack(fill=tk.X)
        
        form_frame = tk.Frame(left_panel, bg=self.COLOR_WHITE)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # ID Nota
        tk.Label(form_frame, text="ID Nota:", bg=self.COLOR_WHITE,
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
        self.entry_id_nota = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.entry_id_nota.grid(row=0, column=1, pady=5)
        
        # Materia
        tk.Label(form_frame, text="Materia:", bg=self.COLOR_WHITE,
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=1, column=0, sticky='w', pady=5)
        self.combo_materias = ttk.Combobox(form_frame, state='readonly',
                                          font=('Segoe UI', 10), width=23)
        self.combo_materias.grid(row=1, column=1, pady=5)
        
        # Nota Final
        tk.Label(form_frame, text="Nota Final:", bg=self.COLOR_WHITE,
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=2, column=0, sticky='w', pady=5)
        self.entry_nota_final = tk.Entry(form_frame, font=('Segoe UI', 10), width=25)
        self.entry_nota_final.grid(row=2, column=1, pady=5)
        
        # Año
        tk.Label(form_frame, text="Año:", bg=self.COLOR_WHITE,
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=3, column=0, sticky='w', pady=5)
        self.combo_anios = ttk.Combobox(form_frame, state='readonly',
                                       font=('Segoe UI', 10), width=23)
        self.combo_anios.grid(row=3, column=1, pady=5)
        
        # Estado
        tk.Label(form_frame, text="Estado:", bg=self.COLOR_WHITE,
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=4, column=0, sticky='w', pady=5)
        self.combo_estados = ttk.Combobox(form_frame, state='readonly',
                                         font=('Segoe UI', 10), width=23)
        self.combo_estados.grid(row=4, column=1, pady=5)
        
        # Botones
        btn_frame = tk.Frame(form_frame, bg=self.COLOR_WHITE)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        tk.Button(btn_frame, text="✓ Agregar",
                 bg=self.COLOR_SUCCESS, fg=self.COLOR_WHITE,
                 font=('Segoe UI', 9, 'bold'), width=10,
                 cursor='hand2', command=self.agregar_nota).pack(pady=3, fill=tk.X)
        
        tk.Button(btn_frame, text="✎ Modificar",
                 bg=self.COLOR_WARNING, fg=self.COLOR_WHITE,
                 font=('Segoe UI', 9, 'bold'), width=10,
                 cursor='hand2', command=self.modificar_nota).pack(pady=3, fill=tk.X)
        
        tk.Button(btn_frame, text="✗ Eliminar",
                 bg=self.COLOR_DANGER, fg=self.COLOR_WHITE,
                 font=('Segoe UI', 9, 'bold'), width=10,
                 cursor='hand2', command=self.eliminar_nota).pack(pady=3, fill=tk.X)
        
        tk.Button(btn_frame, text="⟲ Limpiar",
                 bg=self.COLOR_SECONDARY, fg=self.COLOR_WHITE,
                 font=('Segoe UI', 9, 'bold'), width=10,
                 cursor='hand2', command=self.limpiar_campos_nota).pack(pady=3, fill=tk.X)
        
        # Panel derecho - Lista de notas
        right_panel = tk.Frame(center_container, bg=self.COLOR_WHITE)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(right_panel,
                text="HISTORIAL DE NOTAS",
                bg=self.COLOR_SECONDARY,
                fg=self.COLOR_WHITE,
                font=('Segoe UI', 11, 'bold'),
                pady=10).pack(fill=tk.X)
        
        tree_frame = tk.Frame(right_panel, bg=self.COLOR_WHITE)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scroll_y = tk.Scrollbar(tree_frame)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        scroll_x = tk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.tree_notas = ttk.Treeview(tree_frame,
                                       columns=('ID', 'Materia', 'Nota', 'Año', 'Estado'),
                                       show='headings',
                                       yscrollcommand=scroll_y.set,
                                       xscrollcommand=scroll_x.set,
                                       height=20)
        
        scroll_y.config(command=self.tree_notas.yview)
        scroll_x.config(command=self.tree_notas.xview)
        
        self.tree_notas.heading('ID', text='ID')
        self.tree_notas.heading('Materia', text='Materia')
        self.tree_notas.heading('Nota', text='Nota')
        self.tree_notas.heading('Año', text='Año')
        self.tree_notas.heading('Estado', text='Estado')
        
        self.tree_notas.column('ID', width=60, anchor='center')
        self.tree_notas.column('Materia', width=200)
        self.tree_notas.column('Nota', width=80, anchor='center')
        self.tree_notas.column('Año', width=100, anchor='center')
        self.tree_notas.column('Estado', width=150, anchor='center')
        
        self.tree_notas.tag_configure('oddrow', background='#F8F9FA')
        self.tree_notas.tag_configure('evenrow', background='#FFFFFF')
        
        self.tree_notas.pack(fill=tk.BOTH, expand=True)
        self.tree_notas.bind('<<TreeviewSelect>>', self.seleccionar_nota)
    
    def _crear_pestaña_configuracion(self):
        """Crea la pestaña de configuración"""
        tab_config = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tab_config, text='⚙️ CONFIGURACIÓN')
        
        # Panel de materias
        materias_frame = tk.Frame(tab_config, bg=self.COLOR_WHITE)
        materias_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(materias_frame,
                text="GESTIÓN DE MATERIAS",
                bg=self.COLOR_SECONDARY,
                fg=self.COLOR_WHITE,
                font=('Segoe UI', 12, 'bold'),
                pady=10).pack(fill=tk.X)
        
        # Formulario de materias
        form_frame = tk.Frame(materias_frame, bg=self.COLOR_WHITE)
        form_frame.pack(padx=20, pady=20)
        
        tk.Label(form_frame, text="ID Materia:", bg=self.COLOR_WHITE,
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
        self.entry_id_materia = tk.Entry(form_frame, font=('Segoe UI', 10), width=30)
        self.entry_id_materia.grid(row=0, column=1, pady=5, padx=10)
        
        tk.Label(form_frame, text="Descripción:", bg=self.COLOR_WHITE,
                fg=self.COLOR_TEXT, font=('Segoe UI', 9, 'bold')).grid(row=1, column=0, sticky='w', pady=5)
        self.entry_desc_materia = tk.Entry(form_frame, font=('Segoe UI', 10), width=30)
        self.entry_desc_materia.grid(row=1, column=1, pady=5, padx=10)
        
        tk.Button(form_frame, text="✓ Agregar Materia",
                 bg=self.COLOR_SUCCESS, fg=self.COLOR_WHITE,
                 font=('Segoe UI', 9, 'bold'), width=20,
                 cursor='hand2', command=self.agregar_materia).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Lista de materias
        list_frame = tk.Frame(materias_frame, bg=self.COLOR_WHITE)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        scroll_y = tk.Scrollbar(list_frame)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox_materias = tk.Listbox(list_frame, font=('Segoe UI', 10),
                                          yscrollcommand=scroll_y.set, height=15)
        scroll_y.config(command=self.listbox_materias.yview)
        self.listbox_materias.pack(fill=tk.BOTH, expand=True)
    
    # MÉTODOS DE ALUMNOS
    
    def cargar_alumnos(self):
        """Carga la lista de alumnos en la tabla"""
        # Limpiar tabla
        for item in self.tree_alumnos.get_children():
            self.tree_alumnos.delete(item)
        
        # Cargar alumnos
        alumnos = self.alumno_service.obtener_alumnos()
        for idx, alumno in enumerate(alumnos):
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
            self.tree_alumnos.insert('', tk.END, 
                                    values=(alumno.id_alumnos, alumno.apellido, 
                                           alumno.nombre, alumno.dni),
                                    tags=(tag,))
        
        # Actualizar combo de alumnos en pestaña de notas
        self.cargar_combo_alumnos()
    
    def cargar_combo_alumnos(self):
        """Carga el combo de alumnos en la pestaña de notas"""
        alumnos = self.alumno_service.obtener_alumnos()
        valores = [f"{a.id_alumnos} - {a.apellido}, {a.nombre}" for a in alumnos]
        self.combo_alumnos['values'] = valores
    
    def seleccionar_alumno(self, event):
        """Maneja la selección de un alumno en la tabla"""
        selection = self.tree_alumnos.selection()
        if selection:
            item = self.tree_alumnos.item(selection[0])
            values = item['values']
            
            self.entry_id_alumno.delete(0, tk.END)
            self.entry_id_alumno.insert(0, values[0])
            
            self.entry_apellido_alumno.delete(0, tk.END)
            self.entry_apellido_alumno.insert(0, values[1])
            
            self.entry_nombre_alumno.delete(0, tk.END)
            self.entry_nombre_alumno.insert(0, values[2])
            
            self.entry_dni_alumno.delete(0, tk.END)
            self.entry_dni_alumno.insert(0, values[3])
    
    def agregar_alumno(self):
        """Agrega un nuevo alumno"""
        try:
            id_alumno = int(self.entry_id_alumno.get())
            nombre = self.entry_nombre_alumno.get().strip()
            apellido = self.entry_apellido_alumno.get().strip()
            dni = int(self.entry_dni_alumno.get())
            
            if not nombre or not apellido:
                messagebox.showwarning("Advertencia", "Complete todos los campos")
                return
            
            alumno = Alumno(id_alumnos=id_alumno, nombre=nombre, 
                          apellido=apellido, dni=dni)
            
            if self.alumno_service.crear_alumno(alumno):
                messagebox.showinfo("Éxito", "Alumno agregado correctamente")
                self.cargar_alumnos()
                self.limpiar_campos_alumno()
            else:
                messagebox.showerror("Error", "No se pudo agregar el alumno")
        except ValueError:
            messagebox.showerror("Error", "Verifique los datos ingresados")
    
    def modificar_alumno(self):
        """Modifica un alumno existente"""
        try:
            id_alumno = int(self.entry_id_alumno.get())
            nombre = self.entry_nombre_alumno.get().strip()
            apellido = self.entry_apellido_alumno.get().strip()
            dni = int(self.entry_dni_alumno.get())
            
            if not nombre or not apellido:
                messagebox.showwarning("Advertencia", "Complete todos los campos")
                return
            
            alumno = Alumno(id_alumnos=id_alumno, nombre=nombre,
                          apellido=apellido, dni=dni)
            
            if self.alumno_service.actualizar_alumno(alumno):
                messagebox.showinfo("Éxito", "Alumno modificado correctamente")
                self.cargar_alumnos()
                self.limpiar_campos_alumno()
            else:
                messagebox.showerror("Error", "No se pudo modificar el alumno")
        except ValueError:
            messagebox.showerror("Error", "Verifique los datos ingresados")
    
    def eliminar_alumno(self):
        """Elimina un alumno"""
        try:
            id_alumno = int(self.entry_id_alumno.get())
            
            if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este alumno?"):
                if self.alumno_service.eliminar_alumno(id_alumno):
                    messagebox.showinfo("Éxito", "Alumno eliminado correctamente")
                    self.cargar_alumnos()
                    self.limpiar_campos_alumno()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el alumno")
        except ValueError:
            messagebox.showerror("Error", "Seleccione un alumno válido")
    
    def limpiar_campos_alumno(self):
        """Limpia los campos del formulario de alumno"""
        self.entry_id_alumno.delete(0, tk.END)
        self.entry_nombre_alumno.delete(0, tk.END)
        self.entry_apellido_alumno.delete(0, tk.END)
        self.entry_dni_alumno.delete(0, tk.END)
    
    # MÉTODOS DE NOTAS
    
    def alumno_combo_changed(self, event):
        """Maneja el cambio de selección en el combo de alumnos"""
        selection = self.combo_alumnos.get()
        if selection:
            id_alumno = int(selection.split(' - ')[0])
            self.alumno_seleccionado = id_alumno
            self.cargar_notas_por_alumno()
    
    def cargar_notas_por_alumno(self):
        """Carga las notas del alumno seleccionado"""
        # Limpiar tabla
        for item in self.tree_notas.get_children():
            self.tree_notas.delete(item)
        
        if self.alumno_seleccionado:
            notas = self.nota_service.obtener_notas_por_alumno(self.alumno_seleccionado)
            for idx, nota in enumerate(notas):
                tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
                self.tree_notas.insert('', tk.END,
                                      values=(nota.id_notas, nota.materia,
                                             nota.nota_final, nota.anio, nota.estado),
                                      tags=(tag,))
    
    def seleccionar_nota(self, event):
        """Maneja la selección de una nota en la tabla"""
        selection = self.tree_notas.selection()
        if selection:
            item = self.tree_notas.item(selection[0])
            values = item['values']
            
            self.entry_id_nota.delete(0, tk.END)
            self.entry_id_nota.insert(0, values[0])
            
            # Buscar y seleccionar en los combos
            for materia in self.combo_materias['values']:
                if values[1] in materia:
                    self.combo_materias.set(materia)
                    break
            
            self.entry_nota_final.delete(0, tk.END)
            self.entry_nota_final.insert(0, values[2])
            
            for anio in self.combo_anios['values']:
                if str(values[3]) in anio:
                    self.combo_anios.set(anio)
                    break
            
            for estado in self.combo_estados['values']:
                if values[4] in estado:
                    self.combo_estados.set(estado)
                    break
    
    def agregar_nota(self):
        """Agrega una nueva nota"""
        if not self.alumno_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un alumno primero")
            return
        
        try:
            id_nota = int(self.entry_id_nota.get())
            nota_final = float(self.entry_nota_final.get())
            
            # Obtener IDs de los combos
            materia_sel = self.combo_materias.get()
            anio_sel = self.combo_anios.get()
            estado_sel = self.combo_estados.get()
            
            if not materia_sel or not anio_sel or not estado_sel:
                messagebox.showwarning("Advertencia", "Complete todos los campos")
                return
            
            id_materia = int(materia_sel.split(' - ')[0])
            id_anio = int(anio_sel.split(' - ')[0])
            id_estado = int(estado_sel.split(' - ')[0])
            
            nota = Nota(id_notas=id_nota, id_alumnos=self.alumno_seleccionado,
                       id_materias=id_materia, nota_final=nota_final,
                       id_anios=id_anio, id_estados=id_estado)
            
            if self.nota_service.crear_nota(nota):
                messagebox.showinfo("Éxito", "Nota agregada correctamente")
                self.cargar_notas_por_alumno()
                self.limpiar_campos_nota()
            else:
                messagebox.showerror("Error", "No se pudo agregar la nota")
        except ValueError:
            messagebox.showerror("Error", "Verifique los datos ingresados")
    
    def modificar_nota(self):
        """Modifica una nota existente"""
        try:
            id_nota = int(self.entry_id_nota.get())
            nota_final = float(self.entry_nota_final.get())
            
            materia_sel = self.combo_materias.get()
            anio_sel = self.combo_anios.get()
            estado_sel = self.combo_estados.get()
            
            if not materia_sel or not anio_sel or not estado_sel:
                messagebox.showwarning("Advertencia", "Complete todos los campos")
                return
            
            id_materia = int(materia_sel.split(' - ')[0])
            id_anio = int(anio_sel.split(' - ')[0])
            id_estado = int(estado_sel.split(' - ')[0])
            
            nota = Nota(id_notas=id_nota, id_materias=id_materia,
                       nota_final=nota_final, id_anios=id_anio, id_estados=id_estado)
            
            if self.nota_service.actualizar_nota(nota):
                messagebox.showinfo("Éxito", "Nota modificada correctamente")
                self.cargar_notas_por_alumno()
                self.limpiar_campos_nota()
            else:
                messagebox.showerror("Error", "No se pudo modificar la nota")
        except ValueError:
            messagebox.showerror("Error", "Verifique los datos ingresados")
    
    def eliminar_nota(self):
        """Elimina una nota"""
        try:
            id_nota = int(self.entry_id_nota.get())
            
            if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta nota?"):
                if self.nota_service.eliminar_nota(id_nota):
                    messagebox.showinfo("Éxito", "Nota eliminada correctamente")
                    self.cargar_notas_por_alumno()
                    self.limpiar_campos_nota()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar la nota")
        except ValueError:
            messagebox.showerror("Error", "Seleccione una nota válida")
    
    def limpiar_campos_nota(self):
        """Limpia los campos del formulario de notas"""
        self.entry_id_nota.delete(0, tk.END)
        self.combo_materias.set('')
        self.entry_nota_final.delete(0, tk.END)
        self.combo_anios.set('')
        self.combo_estados.set('')
    
    # MÉTODOS DE CONFIGURACIÓN
    
    def agregar_materia(self):
        """Agrega una nueva materia"""
        try:
            id_materia = int(self.entry_id_materia.get())
            descripcion = self.entry_desc_materia.get().strip()
            
            if not descripcion:
                messagebox.showwarning("Advertencia", "Complete todos los campos")
                return
            
            materia = Materia(id_materias=id_materia, descripcion=descripcion)
            
            if self.materia_service.crear_materia(materia):
                messagebox.showinfo("Éxito", "Materia agregada correctamente")
                self.cargar_materias()
                self.entry_id_materia.delete(0, tk.END)
                self.entry_desc_materia.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "No se pudo agregar la materia")
        except ValueError:
            messagebox.showerror("Error", "Verifique los datos ingresados")
    
    def cargar_materias(self):
        """Carga las materias en el listbox y combo"""
        materias = self.materia_service.obtener_materias()
        
        # Actualizar listbox
        self.listbox_materias.delete(0, tk.END)
        for materia in materias:
            self.listbox_materias.insert(tk.END, f"{materia.id_materias} - {materia.descripcion}")
        
        # Actualizar combo
        valores = [f"{m.id_materias} - {m.descripcion}" for m in materias]
        self.combo_materias['values'] = valores
    
    def cargar_datos_iniciales(self):
        """Carga todos los datos iniciales de la aplicación"""
        self.cargar_alumnos()
        self.cargar_materias()
        
        # Cargar años
        anios = self.anio_service.obtener_anios()
        self.combo_anios['values'] = [f"{a.id_anios} - {a.descripcion}" for a in anios]
        
        # Cargar estados
        estados = self.estado_service.obtener_estados()
        self.combo_estados['values'] = [f"{e.id_estados} - {e.descripcion}" for e in estados]
