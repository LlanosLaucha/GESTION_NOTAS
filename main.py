import tkinter as tk
from gestion_notas.views.main_view import MainView

if __name__ == "__main__":
    # Crea la ventana principal de la aplicación.
    root = tk.Tk()
    
    # Crea una instancia de nuestra clase MainView, que construye toda la interfaz
    # y contiene la lógica de la aplicación.
    app = MainView(root)
    
    # Inicia el bucle de eventos de Tkinter para que la ventana aparezca y sea interactiva.
    root.mainloop()