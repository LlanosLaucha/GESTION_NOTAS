from gestion_notas.config.db_config import get_db_connection
from mysql.connector import Error

class CatalogoService:
    """
    Servicio para cargar listas (catálogos) desde la base de datos
    (Materias, Años, Estados).
    """

    def _obtener_catalogo(self, query):
        """
        Método genérico reutilizable para ejecutar consultas de catálogo.
        """
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                return []
            
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        
        except Error as e:
            print(f"Error al obtener catálogo: {e}")
            return []
        
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def obtener_materias(self):
        """Obtiene la lista de todas las materias."""
        query = "SELECT id_materias, descripcion FROM materias"
        return self._obtener_catalogo(query)

    def obtener_anios(self):
        """Obtiene la lista de todos los años."""
        query = "SELECT id_anios, descripcion FROM anios"
        return self._obtener_catalogo(query)

    def obtener_estados(self):
        """Obtiene la lista de todos los estados de nota."""
        query = "SELECT id_estados, descripcion FROM estados"
        return self._obtener_catalogo(query)

    def obtener_mapa_estados(self):
        """
        Devuelve un diccionario para traducir descripciones de estado a IDs.
        Ej: {"Promocionado": 1, "Regular": 2, "Recursante": 3}
        """
        try:
            estados_lista = self.obtener_estados()
            # Convertir la lista de diccionarios en un mapa {descripcion: id}
            return {str(e['descripcion']).strip(): e['id_estados'] for e in estados_lista}
        except Exception as e:
            print(f"Error al crear mapa de estados: {e}")
            return {}