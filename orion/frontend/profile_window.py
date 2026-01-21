import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QDialog
from PySide6.QtCore import Qt
from ..ui.orion_v5 import Ui_mainWindow
from ..ui.ui_profile.profile3 import Ui_Dialog
# from ..backend.TrackerEngine import TrackerEngine
# from ..backend.ProfileEngine import ProfileEngine
from ..backend.database import database_init, createDefaultProfile, loadProfileNames, getProfileDescription, deleteProfile
# from PySide6.QtGui import QIcon, QStandardItem, QStandardItemModel, QPalette, QColor
from orion.frontend.new_profile_dialog import NewProfileDialog


class ProfileWindow(QDialog):
    def __init__(self, profileEngine, parent=None):
        super().__init__(parent)

        self.engine = profileEngine
        self.engine.activate()
    

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.connections()
        self.refreshProfileList()

        self.setWindowTitle("Configuration")
        self.setBaseSize(500, 660)

        self.ui.editBox.setDisabled(True)


    def connections(self):
            self.ui.profileList.itemClicked.connect(self.onItemClicked)
            self.ui.newProfileButton.clicked.connect(self.newProfileClicked)
            self.ui.deleteProfileButton.clicked.connect(self.deleteClicked)
            self.ui.editProfileButton.clicked.connect(
                lambda: self.editClicked(self.ui.profileList.selectedItems()[0])
            )

    def refreshProfileList(self):
        self.ui.profileList.clear()
        for i in loadProfileNames():
            self.ui.profileList.addItem(i)

    def onItemClicked(self, item):
        profileName = item.text()
        print("Clicked profile:", profileName)
        self.ui.descriptionBox.setPlainText(getProfileDescription(profileName))

    def newProfileClicked(self):
        self.newProfileDialogue = NewProfileDialog()
        self.newProfileDialogue.exec()
        self.refreshProfileList()
        
    def deleteClicked(self):
        profileName = self.ui.profileList.currentItem().text()
        print("Profile to delete:", profileName)
        deleteProfile(profileName)
        self.refreshProfileList()
        self.ui.descriptionBox.clear()



    def editClicked(self, item):
         print("Editing profile: ", item.text())
         
         

    # def dialogEnd(self, result):
    #     if result == QDialog.Accepted:
    #         self.engine.save_profile()