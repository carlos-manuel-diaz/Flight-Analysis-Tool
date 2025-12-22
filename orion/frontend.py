import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget
from PySide6.QtCore import Qt
from .ui.orion_v3 import Ui_mainWindow
from .backend import TrackerEngine
from PySide6.QtGui import QIcon, QStandardItem, QStandardItemModel

class FlightTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.engine = TrackerEngine()
        self.connections()

        self.ui.stackedWidget.setCurrentIndex(0)

        self.setWindowTitle("Orion")
        self.setBaseSize(800, 600)

    def connections(self):
        self.ui.importButton.clicked.connect(self.import_clicked)
        self.ui.graphButton.clicked.connect(self.graph_clicked)
        self.ui.sheetButton.clicked.connect(self.sheet_clicked)
        print('connected')

    def import_clicked(self): #import button clicked
        print('import clicked!')
        csv_path = self.engine.addCsv()
        self.ui.csvList.addItem(csv_path)
        self.engine.csvList.append(csv_path)

    def graph_clicked(self): #graph button clicked
        print('Switching to graph view')       

        if self.display_graph(self.ui.csvList.currentText()) == -1:
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.ui.stackedWidget.setCurrentIndex(1)
    


    def sheet_clicked(self): #sheet button clicked
        print('Switching to sheet view')

        if self.display_sheet(self.ui.csvList.currentText()) == -1:
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.ui.stackedWidget.setCurrentIndex(2)


    def display_graph(self, path): #display graph with currently selected path
        current_csv = path
        if not current_csv:
            print("No CSV selected.")
            return -1
        time_x, accel_y = self.engine.extract(current_csv)
        if time_x is None or accel_y is None:
            print("Extraction failed.")
            return
        self.ui.graphWidget.clear()    
        self.ui.graphWidget.plot(time_x, accel_y)

    def display_sheet(self, path): #display sheet with currently selected path
        current_csv = path
        if not current_csv:
            print("No CSV selected.")
            return -1
        
        model = QStandardItemModel()
        self.ui.sheetWidget.setModel(model)
        self.ui.sheetWidget.horizontalHeader().setStretchLastSection(True)

        with open(current_csv, "r", newline="", encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            for i, row in enumerate(reader):
                if i == 0:
                    model.setHorizontalHeaderLabels(
                        [col.strip().strip('"') for col in row]
                    )
                else:
                    items = [QStandardItem(field.strip()) for field in row]
                    model.appendRow(items)
     
        
        



def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Orion")
    app.setApplicationVersion("1.0")


    window = FlightTrackerApp()
    window.setWindowIcon(QIcon("assets/seds.png"))
    window.show()

    sys.exit(app.exec())

