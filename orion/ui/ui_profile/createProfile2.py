# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createProfile2.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_createProfileDialog(object):
    def setupUi(self, createProfileDialog):
        if not createProfileDialog.objectName():
            createProfileDialog.setObjectName(u"createProfileDialog")
        createProfileDialog.resize(600, 345)
        createProfileDialog.setMinimumSize(QSize(600, 345))
        createProfileDialog.setMaximumSize(QSize(600, 345))
        self.horizontalLayoutWidget = QWidget(createProfileDialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 300, 581, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(30)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.confirmButton = QPushButton(self.horizontalLayoutWidget)
        self.confirmButton.setObjectName(u"confirmButton")

        self.horizontalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.descriptionInput = QTextEdit(createProfileDialog)
        self.descriptionInput.setObjectName(u"descriptionInput")
        self.descriptionInput.setGeometry(QRect(10, 40, 571, 221))
        self.profileLabel = QLabel(createProfileDialog)
        self.profileLabel.setObjectName(u"profileLabel")
        self.profileLabel.setGeometry(QRect(10, 280, 111, 16))
        self.descriptionLabel = QLabel(createProfileDialog)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(10, 20, 111, 16))

        self.retranslateUi(createProfileDialog)

        QMetaObject.connectSlotsByName(createProfileDialog)
    # setupUi

    def retranslateUi(self, createProfileDialog):
        createProfileDialog.setWindowTitle(QCoreApplication.translate("createProfileDialog", u"Dialog", None))
        self.lineEdit.setText("")
        self.confirmButton.setText(QCoreApplication.translate("createProfileDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("createProfileDialog", u"Cancel", None))
        self.profileLabel.setText(QCoreApplication.translate("createProfileDialog", u"Input Profile Name", None))
        self.descriptionLabel.setText(QCoreApplication.translate("createProfileDialog", u"Profile Description", None))
    # retranslateUi

