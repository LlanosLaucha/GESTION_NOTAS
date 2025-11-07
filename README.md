# Sistema de Gestión de Notas Académicas

Proyecto para la materia de Programación Orientada a Objetos. Es una aplicación de escritorio para administrar notas académicas, permitiendo crear, leer, actualizar y eliminar registros (ABM/CRUD).

# Características Principales

1. Gestión de Alumnos: Permite registrar nuevos alumnos (nombre, apellido, DNI), modificar sus datos y eliminarlos del sistema.

2. Gestión de Notas por Alumno: Para cada alumno seleccionado, la aplicación permite añadir, modificar y eliminar sus notas académicas (materia, calificación).

3. Soft Delete: Los alumnos no se eliminan físicamente. Se marcan como "inactivos" (activo = 0), preservando la integridad de los datos y permitiendo auditorías.

4. Lógica de Negocio Automatizada: El estado de una nota (Promocionado, Regular, Recursante) se calcula automáticamente en la Capa de Servicio basándose en la calificación.

5. Interfaz Gráfica Moderna: Construida con ttkbootstrap para una estética limpia y profesional.

6. Diseño Responsivo: La ventana y sus componentes se adaptan al tamaño del monitor.

7. Experiencia de Usuario (UX) Mejorada: Uso de listas desplegables (Combobox) cargadas desde la base de datos (Materias, Años), evitando que el usuario memorice IDs.

# Tecnologías Utilizadas

1. Lenguaje: Python (3.11+)
2. Interfaz Gráfica (GUI): ttkbootstrap (basado en tkinter)
3. Base de Datos: MySQL (Workbench 8.0)
4. Control de Versiones: Git y GitHub
5. Arquitectura: Modelo-Servicio-Vista (Model-Service-View)
6. Conector de BD: mysql-connector-python

# Estructura del Proyecto

```
GESTION_NOTAS/
├── .gitignore
├── main.py               <-- (El lanzador de la aplicación)
├── requirements.txt      <-- (Lista de dependencias)
├── schema.sql            <-- (Script de creación de la BD)
├── venv/
└── gestion_notas/        <-- (El paquete principal del proyecto)
    ├── __init__.py
    ├── config/           <-- (Capa de Configuración)
    │   ├── __init__.py
    │   └── db_config.py
    ├── models/           <-- (Capa de Modelos)
    │   ├── __init__.py
    │   ├── alumno_model.py
    │   └── nota_model.py
    ├── services/         <-- (Capa de Servicios - Lógica de Negocio)
    │   ├── __init__.py
    │   ├── alumno_service.py
    │   ├── catalogo_service.py
    │   └── nota_service.py
    └── views/            <-- (Capa de Vista - UI)
        ├── __init__.py
        └── main_view.py

```

# Instalación y Ejecución

## Prerrequisitos

1. Tener Python 3.11 o superior instalado. (Asegúrate de marcar "Add python.exe to PATH" durante la instalación).

2. Tener un servidor MySQL local instalado y en ejecución (Ej: MySQL Workbench).

## Configuración de la Base de Datos

1. Abre tu cliente de MySQL (Workbench).

2. Crea una nueva base de datos (schema) llamada gestion_notas.

3. Abre y ejecuta el archivo schema.sql (incluido en este repositorio). Este script creará todas las tablas (alumnos, notas, materias, anios, estados) y poblará los catálogos necesarios para el primer uso.

##  Clonar el Repositorio

git clone [https://github.com/LlanosLaucha/GESTION_NOTAS.git](https://github.com/LlanosLaucha/GESTION_NOTAS.git)
cd GESTION_NOTAS

## Configurar el Entorno Virtual (Recomendado)

1. Comandos: 

```
En Windows
python -m venv venv

En macOS / Linux
python3 -m venv venv
```

2. Presiona Ctrl+Shift+P para abrir la Paleta de Comandos. 

3. Escribe y selecciona la opción "Python: Select Interpreter" (Python: Seleccionar Intérprete).

4. En la lista que aparece, selecciona el intérprete que está dentro de la carpeta venv que acabas de crear. La ruta será similar a:

```
.\venv\Scripts\python.exe (windows)
./venv/bin/python (macOS/Linux)
```

# Instalar dependencias

1. python -m pip install -r requirements.txt

# Configuración local

1. Abre el archivo: gestion_notas/config/db_config.py.

2. Modifica el diccionario DB_CONFIG con tu usuario y contraseña local de MySQL.

```
DB_CONFIG = {
    'host': 'localhost',
    'user': 'tu_usuario_root',
    'password': 'tu_contraseña', # <-- ¡Modifica esta línea!
    'database': 'gestion_notas'
}
```

# Equipo de Desarrollo

* **[Llanos Lautaro]** - Lider del proyecto / Tester / Documentador - @LlanosLaucha
* **[Maidana Nicolas]** - Backend - @NicoMaidanaa
* **[Kocur Malena]** - Frontend - @usuario-github
* **[Fernandez Candela]** - Frontend - @candeelaa14
