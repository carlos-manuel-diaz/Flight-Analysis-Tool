import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtCore import Qt
from .ui.orion_v0 import Ui_sheetView
from .backend import TrackerEngine

class FlightTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_sheetView()
        self.ui.setupUi(self)

        self.engine = TrackerEngine()
        self.connections()

        self.setWindowTitle("Orion")
        self.setFixedSize(800, 600)

    def connections(self):
        self.ui.importButton.clicked.connect(self.import_clicked)
        print('connected')

    def import_clicked(self):
        print('import clicked!')
        csv_path = self.engine.getCsv()
        self.ui.csvList.addItem(csv_path)



def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Orion")
    app.setApplicationVersion("1.0")

    window = FlightTrackerApp()   
    window.show()

    sys.exit(app.exec())
