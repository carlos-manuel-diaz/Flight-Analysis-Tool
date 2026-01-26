# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile3.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPlainTextEdit,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 700)
        Dialog.setMinimumSize(QSize(500, 700))
        Dialog.setMaximumSize(QSize(500, 700))
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 481, 681))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.horizontalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.profileTab = QWidget()
        self.profileTab.setObjectName(u"profileTab")
        self.profileBox = QGroupBox(self.profileTab)
        self.profileBox.setObjectName(u"profileBox")
        self.profileBox.setGeometry(QRect(10, 10, 451, 331))
        self.horizontalLayoutWidget_3 = QWidget(self.profileBox)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(33, 290, 391, 26))
        self.profileButtons = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.profileButtons.setObjectName(u"profileButtons")
        self.profileButtons.setContentsMargins(0, 0, 0, 0)
        self.newProfileButton = QPushButton(self.horizontalLayoutWidget_3)
        self.newProfileButton.setObjectName(u"newProfileButton")

        self.profileButtons.addWidget(self.newProfileButton)

        self.editProfileButton = QPushButton(self.horizontalLayoutWidget_3)
        self.editProfileButton.setObjectName(u"editProfileButton")

        self.profileButtons.addWidget(self.editProfileButton)

        self.copyProfileButton = QPushButton(self.horizontalLayoutWidget_3)
        self.copyProfileButton.setObjectName(u"copyProfileButton")

        self.profileButtons.addWidget(self.copyProfileButton)

        self.deleteProfileButton = QPushButton(self.horizontalLayoutWidget_3)
        self.deleteProfileButton.setObjectName(u"deleteProfileButton")

        self.profileButtons.addWidget(self.deleteProfileButton)

        self.descriptionBox = QPlainTextEdit(self.profileBox)
        self.descriptionBox.setObjectName(u"descriptionBox")
        self.descriptionBox.setGeometry(QRect(10, 170, 431, 101))
        self.descriptionBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.descriptionBox.setReadOnly(True)
        self.profileList = QListWidget(self.profileBox)
        self.profileList.setObjectName(u"profileList")
        self.profileList.setGeometry(QRect(20, 20, 411, 141))
        self.editBox = QGroupBox(self.profileTab)
        self.editBox.setObjectName(u"editBox")
        self.editBox.setGeometry(QRect(10, 350, 451, 291))
        self.label = QLabel(self.editBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 91, 31))
        self.verticalLayoutWidget_2 = QWidget(self.editBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 150, 201, 91))
        self.editXButtons = QVBoxLayout(self.verticalLayoutWidget_2)
        self.editXButtons.setObjectName(u"editXButtons")
        self.editXButtons.setContentsMargins(0, 0, 0, 0)
        self.newAttribute = QPushButton(self.verticalLayoutWidget_2)
        self.newAttribute.setObjectName(u"newAttribute")

        self.editXButtons.addWidget(self.newAttribute)

        self.deleteAttribute = QPushButton(self.verticalLayoutWidget_2)
        self.deleteAttribute.setObjectName(u"deleteAttribute")

        self.editXButtons.addWidget(self.deleteAttribute)

        self.attributeList = QListWidget(self.editBox)
        self.attributeList.setObjectName(u"attributeList")
        self.attributeList.setGeometry(QRect(30, 50, 191, 91))
        self.attributeList_2 = QListWidget(self.editBox)
        self.attributeList_2.setObjectName(u"attributeList_2")
        self.attributeList_2.setGeometry(QRect(230, 50, 191, 91))
        self.label_2 = QLabel(self.editBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 20, 91, 31))
        self.verticalLayoutWidget_3 = QWidget(self.editBox)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(230, 150, 201, 91))
        self.editYButtons_2 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.editYButtons_2.setObjectName(u"editYButtons_2")
        self.editYButtons_2.setContentsMargins(0, 0, 0, 0)
        self.newAttribute_2 = QPushButton(self.verticalLayoutWidget_3)
        self.newAttribute_2.setObjectName(u"newAttribute_2")

        self.editYButtons_2.addWidget(self.newAttribute_2)

        self.deleteAttribute_2 = QPushButton(self.verticalLayoutWidget_3)
        self.deleteAttribute_2.setObjectName(u"deleteAttribute_2")

        self.editYButtons_2.addWidget(self.deleteAttribute_2)

        self.horizontalLayoutWidget_2 = QWidget(self.editBox)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(80, 250, 291, 31))
        self.formButtons = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.formButtons.setObjectName(u"formButtons")
        self.formButtons.setContentsMargins(0, 0, 0, 0)
        self.confirmButton = QPushButton(self.horizontalLayoutWidget_2)
        self.confirmButton.setObjectName(u"confirmButton")

        self.formButtons.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(self.horizontalLayoutWidget_2)
        self.cancelButton.setObjectName(u"cancelButton")

        self.formButtons.addWidget(self.cancelButton)

        self.tabWidget.addTab(self.profileTab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.profileBox.setTitle(QCoreApplication.translate("Dialog", u"Profiles", None))
        self.newProfileButton.setText(QCoreApplication.translate("Dialog", u"New Profile", None))
        self.editProfileButton.setText(QCoreApplication.translate("Dialog", u"Edit Profile", None))
        self.copyProfileButton.setText(QCoreApplication.translate("Dialog", u"Copy Profile", None))
        self.deleteProfileButton.setText(QCoreApplication.translate("Dialog", u"Delete Profile", None))
        self.descriptionBox.setPlainText("")
        self.editBox.setTitle(QCoreApplication.translate("Dialog", u"Default Profile ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Key X Attributes", None))
        self.newAttribute.setText(QCoreApplication.translate("Dialog", u"New Attribute", None))
        self.deleteAttribute.setText(QCoreApplication.translate("Dialog", u"Delete Attribute", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Key Y Attributes", None))
        self.newAttribute_2.setText(QCoreApplication.translate("Dialog", u"New Attribute", None))
        self.deleteAttribute_2.setText(QCoreApplication.translate("Dialog", u"Delete Attribute", None))
        self.confirmButton.setText(QCoreApplication.translate("Dialog", u"Confirm Edits", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel Edits", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profileTab), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"Tab 2", None))
    # retranslateUi

