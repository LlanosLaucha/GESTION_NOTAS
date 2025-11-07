import mysql.connector
from mysql.connector import Error

# NOTA: Cambia 'Root2025' por la contraseña que corresponda en cada PC.
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'gestion_notas'
}

def get_db_connection():
    """
    Crea y devuelve una conexión a la base de datos.
    Maneja la excepción si la conexión falla.
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG, use_pure=True)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        # En una app real, podríamos registrar esto en un log.
        # Devolvemos None para que el servicio sepa que la conexión falló.
        return None
