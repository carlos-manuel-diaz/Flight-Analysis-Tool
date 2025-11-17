# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orion_v0.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_sheetView(object):
    def setupUi(self, sheetView):
        if not sheetView.objectName():
            sheetView.setObjectName(u"sheetView")
        sheetView.resize(800, 600)
        self.centralwidget = QWidget(sheetView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 10, 801, 31))
        self.importHeader = QHBoxLayout(self.horizontalLayoutWidget)
        self.importHeader.setObjectName(u"importHeader")
        self.importHeader.setContentsMargins(0, 0, 0, 0)
        self.csvList = QComboBox(self.horizontalLayoutWidget)
        self.csvList.setObjectName(u"csvList")
        self.csvList.setEditable(True)

        self.importHeader.addWidget(self.csvList)

        self.importButton = QPushButton(self.horizontalLayoutWidget)
        self.importButton.setObjectName(u"importButton")
        

        self.importHeader.addWidget(self.importButton)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 559, 801, 41))
        self.viewButtons = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.viewButtons.setObjectName(u"viewButtons")
        self.viewButtons.setContentsMargins(0, 0, 0, 0)
        self.graphView = QPushButton(self.horizontalLayoutWidget_2)
        self.graphView.setObjectName(u"graphView")

        self.viewButtons.addWidget(self.graphView)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.viewButtons.addWidget(self.pushButton_4)

        sheetView.setCentralWidget(self.centralwidget)

        self.retranslateUi(sheetView)

        QMetaObject.connectSlotsByName(sheetView)
    # setupUi

    def retranslateUi(self, sheetView):
        sheetView.setWindowTitle(QCoreApplication.translate("sheetView", u"MainWindow", None))
        self.csvList.setPlaceholderText(QCoreApplication.translate("sheetView", u"Select Data", None))
        self.importButton.setText(QCoreApplication.translate("sheetView", u"Import", None))
        self.graphView.setText(QCoreApplication.translate("sheetView", u"Graph View", None))
        self.pushButton_4.setText(QCoreApplication.translate("sheetView", u"Sheet View", None))
    # retranslateUi

