# Sistema de Gestión de Notas - ITEC Nº 3

Sistema de gestión académica desarrollado en Python con interfaz gráfica Tkinter para administrar alumnos, materias y notas.

## 📋 Características

- ✅ Gestión completa de alumnos (CRUD)
- ✅ Gestión de materias
- ✅ Registro de notas por alumno
- ✅ Consulta de historial académico
- ✅ Interfaz gráfica profesional e intuitiva
- ✅ Arquitectura MVC (Modelo-Vista-Controlador)
- ✅ Base de datos MySQL
- ✅ Diseño con colores corporativos profesionales

## 🚀 Tecnologías

- **Python 3.x**
- **Tkinter** (Interfaz gráfica)
- **MySQL** (Base de datos)
- **mysql-connector-python** (Conector de base de datos)

## 📦 Instalación

### Requisitos previos

- Python 3.7 o superior
- MySQL Server 8.0 o superior
- MySQL Workbench (opcional, para administración de base de datos)

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/LlanosLaucha/GESTION_NOTAS.git
   cd GESTION_NOTAS
   ```

2. **Crear entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**

   a. Crear la base de datos en MySQL:
   ```bash
   mysql -u root -p < database/script_creacion.sql
   ```

   b. Cargar datos de prueba (opcional):
   ```bash
   mysql -u root -p gestion_notas < database/datos_prueba.sql
   ```

   c. Configurar credenciales en `config/db_config.py`:
   ```python
   DB_CONFIG = {
       'host': 'localhost',
       'user': 'root',
       'password': 'Root2025',  # Cambiar por tu contraseña
       'database': 'gestion_notas'
   }
   ```

5. **Ejecutar la aplicación**
   ```bash
   python main.py
   ```

## 📂 Estructura del Proyecto

```
GESTION_NOTAS/
│
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Documentación
├── .gitignore             # Archivos ignorados por Git
│
├── config/                # Configuración
│   ├── __init__.py
│   └── db_config.py       # Configuración de base de datos
│
├── models/                # Modelos de datos (POO)
│   ├── __init__.py
│   ├── alumno_model.py    # Clase Alumno
│   ├── materia_model.py   # Clase Materia
│   ├── anio_model.py      # Clase Año
│   ├── estado_model.py    # Clase Estado
│   └── nota_model.py      # Clase Nota
│
├── services/              # Lógica de negocio y acceso a datos
│   ├── __init__.py
│   ├── alumno_service.py  # CRUD de alumnos
│   ├── materia_service.py # CRUD de materias
│   ├── anio_service.py    # Operaciones con años
│   ├── estado_service.py  # Operaciones con estados
│   └── nota_service.py    # CRUD de notas
│
├── views/                 # Interfaz gráfica
│   ├── __init__.py
│   └── main_view.py       # Vista principal
│
└── database/              # Scripts de base de datos
    ├── script_creacion.sql    # Creación de tablas
    └── datos_prueba.sql       # Datos de ejemplo
```

## 💾 Base de Datos

### Tablas

- **alumnos**: Información de estudiantes
- **materias**: Catálogo de materias
- **anios**: Años académicos
- **estados**: Estados de notas (Aprobado, Desaprobado, etc.)
- **notas**: Registro de calificaciones

### Diagrama ER

```
alumnos (1) ----< (N) notas (N) >---- (1) materias
                        ↓
                    (1) anios
                        ↓
                    (1) estados
```

## 🎨 Interfaz

La aplicación cuenta con tres pestañas principales:

1. **📚 ALUMNOS**: Gestión completa de estudiantes
   - Registro de nuevos alumnos
   - Modificación de datos
   - Eliminación lógica
   - Visualización en tabla ordenada

2. **📝 NOTAS**: Gestión de calificaciones
   - Asignación de notas por alumno y materia
   - Consulta de historial académico
   - Modificación y eliminación de registros

3. **⚙️ CONFIGURACIÓN**: Gestión de catálogos
   - Administración de materias
   - Visualización de configuraciones

### Colores Corporativos

- Azul Oscuro Principal: `#1E3A5F`
- Azul Medio: `#2E5984`
- Azul Claro: `#4A7BA7`
- Fondo: `#F5F6FA`
- Texto: `#2C3E50`

## 🔧 Uso

### Agregar un Alumno

1. Ir a la pestaña "ALUMNOS"
2. Completar el formulario con los datos del alumno
3. Hacer clic en "Agregar"

### Registrar una Nota

1. Ir a la pestaña "NOTAS"
2. Seleccionar un alumno del desplegable
3. Completar el formulario de nota
4. Hacer clic en "Agregar"

### Modificar Registros

1. Seleccionar el registro de la tabla
2. Modificar los datos en el formulario
3. Hacer clic en "Modificar"

## 👥 Autor

**Proyecto Final - Programación Orientada a Objetos**
- ITEC Nº 3 - Instituto Técnico
- Prof. Medina, Juan Agustín

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📞 Contacto

Para preguntas o sugerencias:
- GitHub: [@LlanosLaucha](https://github.com/LlanosLaucha)
- Repositorio: https://github.com/LlanosLaucha/GESTION_NOTAS

## ✨ Características Destacadas

- **Arquitectura POO**: Código modular y mantenible
- **Patrón MVC**: Separación clara de responsabilidades
- **Validaciones**: Control de datos de entrada
- **Manejo de errores**: Mensajes informativos al usuario
- **Interfaz profesional**: Diseño intuitivo y moderno
- **Base de datos relacional**: Integridad referencial
- **Eliminación lógica**: Preservación del historial

---
Desarrollado con ❤️ para ITEC Nº 3
