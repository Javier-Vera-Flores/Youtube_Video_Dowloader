from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class DownloadView:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle("Descargador de YouTube")
        self.layout = QVBoxLayout()

        # Campos de entrada y botón
        self.input_url = QLineEdit()
        self.input_url.setPlaceholderText("Ingresa la URL del video")
        self.boton = QPushButton("Descargar")

        # Añadir widgets al layout
        self.layout.addWidget(self.input_url)
        self.layout.addWidget(self.boton)
        self.window.setLayout(self.layout)

    def run(self):
        self.window.show()
        self.app.exec_()


# # view.py
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

# class YouTubeView:
#     def __init__(self):
#         self.app = QApplication([])
#         self.window = QWidget()
#         self.window.setWindowTitle("Descargador de YouTube")
#         self.layout = QVBoxLayout()
#         self.input_url = QLineEdit()
#         self.boton = QPushButton("Descargar")
#         self.layout.addWidget(self.input_url)
#         self.layout.addWidget(self.boton)
#         self.window.setLayout(self.layout)

#     def run(self):
#         self.window.show()
#         self.app.exec_()
