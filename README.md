# Sistema de Gestión de Notas Académicas

Proyecto para la materia de Programación Orientada a Objetos. Es una aplicación de escritorio para administrar notas académicas, permitiendo crear, leer, actualizar y eliminar registros (ABM/CRUD).

# Características Principales

1. Alta de Notas: Permite registrar nuevas notas especificando materia, calificación, fecha, etc.
2. Listado de Notas: Muestra todas las notas existentes en una tabla clara y ordenada.
3. Modificación de Notas: Permite editar la información de una nota ya existente.
4. Baja de Notas: Permite eliminar notas del sistema.
5. Interfaz Gráfica Intuitiva: Diseñada para ser fácil de usar.

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
│   └── nota_model.py
├── services/
│   ├── __init__.py
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
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate


4. Instalar las dependencias (el conector de MySQL): pip install mysql-connector-python


5. Configurar la Base de Datos:
    a. Asegúrate de tener un servidor MySQL en ejecución.
    b. Usando MySQL Workbench o cualquier otro cliente, crea una nueva base de datos. Ejemplo: CREATE DATABASE gestion_notas_db;
    c. Crea la tabla necesaria para las notas (el script se proveerá más adelante).

6. Ejecutar la aplicación: python main.py


# Equipo de Desarrollo

* **[Llanos Lautaro]** - Lider del proyecto / Tester / Documentador - @LlanosLaucha
* **[Fleck Ian]** - Backend - @usuario-github
* **[Maidana Nicolas]** - Backend - @usuario-github
* **[Kocur Malena]** - Frontend - @usuario-github
* **[Fernandez Candela]** - Frontend - @usuario-github
