import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QDialog
from PySide6.QtCore import Qt
from ..ui.orion_v5 import Ui_mainWindow
from ..ui.ui_profile.profile2 import Ui_Dialog
# from ..backend.TrackerEngine import TrackerEngine
# from ..backend.ProfileEngine import ProfileEngine
from ..backend.database import database_init, createDefaultProfile, loadProfileNames, getProfileDescription
# from PySide6.QtGui import QIcon, QStandardItem, QStandardItemModel, QPalette, QColor
from orion.frontend.new_profile_dialog import NewProfileDialog


class ProfileWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.connections()
        self.refreshProfileList()

        self.setWindowTitle("Configuration")
        self.setBaseSize(500, 660)

    def connections(self):
            self.ui.listWidget_2.itemClicked.connect(self.onItemClicked)
            self.ui.newProfileButton_2.clicked.connect(self.newProfileClicked)

    def refreshProfileList(self):
        for i in loadProfileNames():
            self.ui.listWidget_2.addItem(i)

    def onItemClicked(self, item):
        profileName = item.text()
        print("Clicked profile:", profileName)
        self.ui.descriptionBox_2.setPlainText(getProfileDescription(profileName))

    def newProfileClicked(self):
        self.newProfileDialogue = NewProfileDialog()
        self.newProfileDialogue.exec()
        
    # def newProfileClicked():