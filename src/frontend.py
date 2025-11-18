import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtCore import Qt
from .ui.orion_v1 import Ui_sheetView
from .backend import TrackerEngine


class FlightTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_sheetView()
        self.ui.setupUi(self)

        self.engine = TrackerEngine()
        self.connections()

        self.ui.graphWidget.hide()

        self.setWindowTitle("Orion")
        self.setFixedSize(800, 600)

    def connections(self):
        self.ui.importButton.clicked.connect(self.import_clicked)
        self.ui.graphView.clicked.connect(self.graph_clicked)
        # self.ui.pushButton_4.clicked.connect(self.sheet_clicked)
        print('connected')

    def import_clicked(self): #import button clicked
        print('import clicked!')
        csv_path = self.engine.addCsv()
        self.ui.csvList.addItem(csv_path)
        self.engine.csvList.append(csv_path)

    def graph_clicked(self): #graph button clicked
        print('Switching to graph view')
        self.build_graph(self.ui.csvList.currentText())
        self.ui.graphWidget.show()


    def build_graph(self, path): #build graph with currently selected path
        current_csv = path

        if not current_csv:
            print("No CSV selected.")
            return

        time_x, accel_y = self.engine.extract(current_csv)

        if time_x is None or accel_y is None:
            print("Extraction failed.")
            return

        self.ui.graphWidget.clear()    
        self.ui.graphWidget.plot(time_x, accel_y)



def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Orion")
    app.setApplicationVersion("1.0")


    window = FlightTrackerApp()
    window.setWindowIcon(QIcon("assets/seds.png"))
    window.show()

    sys.exit(app.exec())
