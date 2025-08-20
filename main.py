import sys
from PyQt5 import QtWidgets
from vista.vista4 import Ui_MainWindow
from controlador.controlador_vista import ControladorVista

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # cargaremos los estilos desde archivo externo
    try:
        with open("assets/styles.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except Exception as e:
        print(f"No se pudo cargar el archivo de estilos: {e}")

    
    controlador = ControladorVista(ui)

    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()












# # -*- coding: utf-8 -*-
# import sys
# from PyQt5 import QtWidgets
# from vista.vista4 import Ui_MainWindow  # tu archivo generado por pyuic5


# def cargar_estilos(ruta):
#     """Carga un archivo QSS y devuelve su contenido"""
#     try:
#         with open(ruta, "r", encoding="utf-8") as f:
#             return f.read()
#     except FileNotFoundError:
#         print(f"Archivo de estilos no encontrado: {ruta}")
#         return ""


# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)

#     # Cargar estilos desde archivo externo
#     qss = cargar_estilos("assets/styles.qss")
#     app.setStyleSheet(qss)

#     MainWindow.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()



# from controlador.download_controller import DownloadController
# from vista.download_view import DownloadView
# from modelo.download_model import DownloadModel


# def main():
#     model = DownloadModel()
#     view = DownloadView()
#     controller = DownloadController(model, view)

#     view.run()  # Arranca la aplicación

# if __name__ == "__main__":
#     main()










































# # main.py
# from controller import YouTubeController
# from view import YouTubeView
# from model import YouTubeModel

# def main():
#     # Crear modelo, vista y controlador
#     model = YouTubeModel()
#     view = YouTubeView()
#     controller = YouTubeController(model, view)
    
#     # Arrancar la aplicación
#     view.run()

# if __name__ == "__main__":
#     main()




# # main.py
# from Controlador import dowload_controller
# from Vista import dowload_view
# from Modelo import dowload_model

# def main():
#     # Crear modelo, vista y controlador
#     model = dowload_model()
#     view = dowload_view()
#     controller = dowload_controller(model, view)
    
#     # Arrancar la aplicación
#     view.run()

# if __name__ == "__main__":
#     main()








# import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout  # Corrección: QApplication y QVBoxLayout

# def main():
#     app = QApplication(sys.argv)  # Corrección: QApplication (con doble 'p')
#     ventana = QWidget()
#     ventana.setWindowTitle("Mi primera app con PyQt5")  # Corrección de texto
#     ventana.setGeometry(100, 100, 400, 200)

#     layout = QVBoxLayout()  # Corrección: QVBoxLayout (no QBoxLayout)
#     label = QLabel("Hola desde PyQt5")
#     layout.addWidget(label)  # Corrección: addWidget (no addWiget)

#     ventana.setLayout(layout)
#     ventana.show()

#     sys.exit(app.exec_())

# if __name__ == "__main__":  # Corrección: debe ser doble igual (==) y comillas dobles o simples
#     main()