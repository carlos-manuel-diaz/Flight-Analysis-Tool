import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtCore import Qt
from .ui.orion_v0 import Ui_MainWindow

class FlightTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Orion")
        self.setFixedSize(800, 600)

def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Orion")
    app.setApplicationVersion("1.0")

    window = FlightTrackerApp()   
    window.show()

    sys.exit(app.exec())
