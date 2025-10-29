# Importamos la librería pathlib, que permite manejar rutas de sistema de archivos
# de una manera moderna y compatible con Windows, Mac y Linux.
from pathlib import Path

def crear_estructura_proyecto():
    """
    Crea la estructura de directorios y archivos inicial para el proyecto de gestión de notas.
    """
    # Lista de directorios que necesitamos. Path() crea un objeto de ruta.
    directorios = [
        Path("gestion_notas/"),
        Path("gestion_notas/models/"),
        Path("gestion_notas/services/"),
        Path("gestion_notas/views/"),
    ]

    # Lista de archivos que necesitamos crear.
    archivos = [
        Path("main.py"),
        Path("gestion_notas/__init__.py"),
        Path("gestion_notas/models/__init__.py"),
        Path("gestion_notas/models/nota_model.py"),
        Path("gestion_notas/services/__init__.py"),
        Path("gestion_notas/services/nota_service.py"),
        Path("gestion_notas/views/__init__.py"),
        Path("gestion_notas/views/main_view.py"),
    ]

    print("Iniciando la creación de la estructura del proyecto...")

    # Creamos cada directorio de la lista.
    for directorio in directorios:
        # Usamos mkdir() para crear el directorio.
        # parents=True: crea los directorios padres si no existen (ej: crea 'gestion_notas' antes que 'models').
        # exist_ok=True: no da error si el directorio ya existe.
        directorio.mkdir(parents=True, exist_ok=True)
        print(f"Directorio creado: {directorio}")

    # Creamos cada archivo de la lista.
    for archivo in archivos:
        # Usamos touch() para crear un archivo vacío.
        # exist_ok=True: no da error si el archivo ya existe.
        archivo.touch(exist_ok=True)
        print(f"Archivo creado: {archivo}")

    print("\n¡Estructura del proyecto creada con éxito!")

if __name__ == "__main__":
    # Esta línea asegura que la función solo se ejecute cuando el script es llamado directamente.
    crear_estructura_proyecto()