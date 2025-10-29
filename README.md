# Sistema de Gestión de Notas Académicas

Proyecto para la materia de Programación Orientada a Objetos. Es una aplicación de escritorio para administrar notas académicas, permitiendo crear, leer, actualizar y eliminar registros (ABM/CRUD).

# Características Principales

1. Gestión de Alumnos: Permite registrar nuevos alumnos (nombre, apellido, DNI), modificar sus datos y eliminarlos del sistema.

2. Gestión de Notas por Alumno: Para cada alumno seleccionado, la aplicación permite añadir, modificar y eliminar sus notas académicas (materia, calificación).

3. Interfaz de Doble Panel: La pantalla principal está dividida en dos secciones para una gestión clara y simultánea de alumnos y sus notas correspondientes.

4. Persistencia de Datos: Toda la información se guarda de forma segura en una base de datos MySQL, garantizando que los datos no se pierdan al cerrar la aplicación.

5. Relación de Datos: Utiliza claves foráneas para vincular de forma segura las notas con cada alumno, y elimina las notas en cascada si un alumno es borrado.

# Tecnologías Utilizadas

1. Lenguaje: Python 3
2. Interfaz Gráfica (GUI): Tkinter
3. Base de Datos: MySQL (Workbench 8.0)
4. Control de Versiones: Git y GitHub
5. Arquitectura: Modelo-Vista-Servicio (una variación de MVC)

# Estructura del Proyecto

```
gestion_notas/
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── alumno_model.py
│   └── nota_model.py
├── services/
│   ├── __init__.py
│   ├── alumno_service.py
│   └── nota_service.py
└── views/
    ├── __init__.py
    └── main_view.py
main.py
```

# Instalación y Ejecución

1. Clonar el repositorio: git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)


2. Navegar al directorio del proyecto: cd nombre-del-repositorio


3. (Recomendado) Crear un entorno virtual:

```
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```


4. Instalar las dependencias (el conector de MySQL): pip install mysql-connector-python


5. Configurar la Base de Datos:
    a. Asegúrate de tener un servidor MySQL en ejecución.
    b. Usando MySQL Workbench o cualquier otro cliente, crea una nueva base de datos. Ejemplo: CREATE DATABASE gestion_notas;
    c. Crea la tabla necesaria para las notas (el script se proveerá más adelante).

6. Ejecutar la aplicación: python main.py


# Equipo de Desarrollo

* **[Llanos Lautaro]** - Lider del proyecto / Tester / Documentador - @LlanosLaucha
* **[Fleck Ian]** - Backend - @ianfleck00
* **[Maidana Nicolas]** - Backend - @NicoMaidanaa
* **[Kocur Malena]** - Frontend - @usuario-github
* **[Fernandez Candela]** - Frontend - @candeelaa14
