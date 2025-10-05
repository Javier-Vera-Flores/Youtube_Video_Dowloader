# -*- coding: utf-8 -*-
import os, sys, subprocess
from PyQt5 import QtWidgets, QtGui
from modelo.lectura_videos import LecturaVideos
from modelo.modelo_descargas import DescargarVideos

class ControladorVista:
    """Controlador que conecta la vista con el modelo"""

    def __init__(self, ui):
        self.ui = ui
        self.modelo = DescargarVideos()
        self.conectar_eventos()

    def conectar_eventos(self):
        # Botones "Guardar en..."
        self.ui.btn_ruta_video.clicked.connect(self.seleccionar_ruta_video)
        self.ui.btn_ruta_varios.clicked.connect(self.seleccionar_ruta_varios)
        self.ui.btn_ruta_playlist.clicked.connect(self.seleccionar_ruta_playlist)

        # Botón "Abrir documento" para varios videos
        self.ui.btn_doc.clicked.connect(self.abrir_documento_txt)

        # Botones descargar
        self.ui.btn_descargar_video.clicked.connect(self.descargar_un_video)
        self.ui.btn_descargar_varios.clicked.connect(self.descargar_varios_videos)
        self.ui.btn_descargar_playlist.clicked.connect(self.descargar_playlist)
        
        #botones para abrir
        self.ui.btn_abrir_video.clicked.connect(self.abrir_video)
        self.ui.btn_abrir_varios.clicked.connect(self.abrir_carpeta_varios)
        self.ui.btn_abrir_playlist.clicked.connect(self.abrir_carpeta_playlist)

    # ---------- Selección de rutas ----------
    def seleccionar_ruta_video(self):
        ruta = QtWidgets.QFileDialog.getExistingDirectory(None, "Seleccionar carpeta para guardar video")
        if ruta:
            self.ui.lbl_guardar_video.setText(f"Guardar en: {ruta}")
            self.ruta_video = ruta

    def seleccionar_ruta_varios(self):
        ruta = QtWidgets.QFileDialog.getExistingDirectory(None, "Seleccionar carpeta para guardar varios videos")
        if ruta:
            self.ui.lbl_guardar_varios.setText(f"Guardar en: {ruta}")
            self.ruta_varios = ruta

    def seleccionar_ruta_playlist(self):
        ruta = QtWidgets.QFileDialog.getExistingDirectory(None, "Seleccionar carpeta para guardar playlist")
        if ruta:
            self.ui.lbl_guardar_playlist.setText(f"Guardar en: {ruta}")
            self.ruta_playlist = ruta

    def abrir_documento_txt(self):
        archivo, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccionar documento con URLs", "", "Archivos TXT (*.txt)")
        if archivo:
            self.ui.lbl_doc.setText(f"Archivo: {archivo}")
            self.archivo_varios = archivo

    # ---------- Actualizaciones de UI ----------
    def actualizar_progreso(self, barra, boton_abrir, valor, mensaje=""):
        barra.setValue(valor)
        if valor >= 100:
            boton_abrir.setEnabled(True)
            boton_abrir.setStyleSheet("background-color: green; color: white;")
        if mensaje:
            print(mensaje)  # O podrías mostrarlo en un QLabel

    # ---------- Descargas ----------
    def descargar_un_video(self):
        url = self.ui.txt_url_video.text().strip()
        ruta = getattr(self, "ruta_video", None)
        if url and ruta:
            #ok = self.modelo.descargar_video(url, ruta)
            archivo = self.modelo.descargar_video(url, ruta)
            #if ok:
            if archivo:
                #guardaremos la ruta completa del archvo
                self.archivo_video = archivo
                self.actualizar_progreso(self.ui.progress_video, self.ui.btn_abrir_video, 100, "Video descargado")
            else:
                self.actualizar_progreso(self.ui.progress_video, self.ui.btn_abrir_video, 0, "Error al descargar")

    def descargar_playlist(self):
        url = self.ui.txt_url_playlist.text().strip()
        ruta = getattr(self, "ruta_playlist", None)
        if url and ruta:
            ok = self.modelo.descargar_playlist(url, ruta)
            if ok:
                self.ruta_playlist_final = ruta #guarcdaremos la ruta de descarga
                self.actualizar_progreso(self.ui.progress_playlist, self.ui.btn_abrir_playlist, 100, "Playlist descargada")
            else:
                self.actualizar_progreso(self.ui.progress_playlist, self.ui.btn_abrir_playlist, 0, "Error al descargar")

    def descargar_varios_videos(self):
        ruta = getattr(self, "ruta_varios", None)
        archivo = getattr(self, "archivo_varios", None)
        if archivo and ruta:
            lectura = LecturaVideos(archivo)
            lista_urls = lectura.obtener_links()
            self.modelo.descargar_varios_videos(lista_urls, ruta)
            #Guardaremos la ruta de la carpeta
            self.ruta_varios_final = ruta
            # Una vez que termine toda la lista, ponemos 100%
            self.actualizar_progreso(self.ui.progress_variosVideos, self.ui.btn_abrir_varios, 100, "Varios videos descargados")
    #metodos para abrir la carpeta
    def abrir_video(self):
        """Abrir el archivo de un solo video con el reproductor por defecto"""
        archivo = getattr(self, "archivo_video", None)
        if archivo and os.path.exists(archivo):
            if sys.platform.startswith("win"):
                os.startfile(archivo)  # Windows
            elif sys.platform.startswith("darwin"):
                subprocess.call(["open", archivo])  # Mac
            else:
                subprocess.call(["xdg-open", archivo])  # Linux

    def abrir_carpeta_varios(self):
        """Abrir la carpeta de varios videos"""
        ruta = getattr(self, "ruta_varios_final", None)
        if ruta and os.path.exists(ruta):
            if sys.platform.startswith("win"):
                os.startfile(ruta)
            elif sys.platform.startswith("darwin"):
                subprocess.call(["open", ruta])
            else:
                subprocess.call(["xdg-open", ruta])

    def abrir_carpeta_playlist(self):
        """Abrir la carpeta de playlist"""
        ruta = getattr(self, "ruta_playlist_final", None)
        if ruta and os.path.exists(ruta):
            if sys.platform.startswith("win"):
                os.startfile(ruta)
            elif sys.platform.startswith("darwin"):
                subprocess.call(["open", ruta])
            else:
                subprocess.call(["xdg-open", ruta])
