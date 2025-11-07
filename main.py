import ttkbootstrap as ttk
from gestion_notas.views.main_view import MainView

if __name__ == "__main__":
    root = ttk.Window(themename="litera") 
    app = MainView(root)
    root.mainloop()