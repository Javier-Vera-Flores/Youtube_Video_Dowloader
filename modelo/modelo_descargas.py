# -*- coding: utf-8 -*-
from pytubefix import YouTube, Playlist  # Ajusta import según pytubefix real
import os

class DescargarVideos:
    """Clase que implementa la lógica de descarga"""

    def __init__(self):
        pass

    def descargar_video(self, url, ruta_guardado, callback=None):
        """Descarga un solo video"""
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            #stream.download(output_path=ruta_guardado)
            archivo = stream.download(output_path=ruta_guardado)
            if callback:
                callback(f"Video descargado: {yt.title}")
            #return True
            return archivo
        except Exception as e:
            if callback:
                callback(f"Error: {e}")
            #return False
            return None

    def descargar_playlist(self, url, ruta_guardado, callback=None):
        """Descarga todos los videos de una playlist"""
        try:
            pl = Playlist(url)
            for video in pl.videos:
                video.streams.get_highest_resolution().download(output_path=ruta_guardado)
                if callback:
                    callback(f"Descargando: {video.title}")
            if callback:
                callback("Playlist descargada correctamente")
            return True
        except Exception as e:
            if callback:
                callback(f"Error: {e}")
            return False

    def descargar_varios_videos(self, lista_urls, ruta_guardado, callback=None):
        """Descarga varios videos desde una lista de URLs"""
        for url in lista_urls:
            self.descargar_video(url, ruta_guardado, callback)
