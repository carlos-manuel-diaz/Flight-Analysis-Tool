import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QDialog, QMessageBox
from PySide6.QtCore import Qt
from ..ui.orion_v5 import Ui_mainWindow
from ..ui.ui_profile.createProfile2 import Ui_createProfileDialog
from ..backend.TrackerEngine import TrackerEngine
from ..backend.ProfileEngine import ProfileEngine
from ..backend.database import database_init, createDefaultProfile, loadProfileNames, getProfileDescription, createProfile
from PySide6.QtGui import QIcon, QStandardItem, QStandardItemModel, QPalette, QColor


class NewProfileDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_createProfileDialog()
        self.ui.setupUi(self)

        self.connections()
        # self.refreshProfileList()

        self.setWindowTitle("New Profile")
        self.setBaseSize(600, 345)

    def connections(self):
            self.ui.cancelButton.clicked.connect(self.cancelClicked)
            self.ui.confirmButton.clicked.connect(self.confirmClicked)    

    def cancelClicked(self):
         self.accept()

    def confirmClicked(self):
         newProfileName = self.ui.lineEdit.text() 
         newProfileDescription = self.ui.descriptionInput.toPlainText()
         
         if newProfileName in loadProfileNames():
              warning = QMessageBox.warning(
                None,
                "Warning",
                "A profile with this name already exists.",
                QMessageBox.StandardButton.Cancel
            )
              return
         else:
             createProfile(newProfileName, newProfileDescription)

         self.accept()
    