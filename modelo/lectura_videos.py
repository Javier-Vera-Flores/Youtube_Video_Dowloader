# -*- coding: utf-8 -*-
class LecturaVideos:
    """Clase para leer un archivo txt con URLs de videos"""

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def obtener_links(self):
        """Devuelve una lista de URLs del archivo"""
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
                # Línea de depuración / confirmación
                print(f"Se leyeron {len(lines)} URL(s):")
                for url in lines:
                    print(f"   - {url}")
            return lines
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return []
