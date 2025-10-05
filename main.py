import sys
from PyQt5 import QtWidgets
from vista.vista4 import Ui_MainWindow
from controlador.controlador_vista import ControladorVista
from modelo.rutas import resource_path 

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # cargaremos los estilos desde archivo externo
    try:
        with open(resource_path("assets/styles.qss"), "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except Exception as e:
        print(f"No se pudo cargar el archivo de estilos: {e}")

    
    controlador = ControladorVista(ui)

    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()