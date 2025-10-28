"""
Sistema de Gestión de Notas
ITEC Nº 3 - Instituto Técnico
Programación Orientada a Objetos

Aplicación de escritorio para la gestión de alumnos, materias y notas académicas
"""

import tkinter as tk
from views.main_view import MainView


def main():
    """Función principal que inicia la aplicación"""
    root = tk.Tk()
    
    # Configurar icono si existe
    # root.iconbitmap('assets/icon.ico')
    
    # Crear la aplicación
    app = MainView(root)
    
    # Iniciar el bucle de eventos
    root.mainloop()


if __name__ == "__main__":
    main()
