# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orion_v3.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableView, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.importHeader = QHBoxLayout()
        self.importHeader.setObjectName(u"importHeader")
        self.csvList = QComboBox(self.centralwidget)
        self.csvList.setObjectName(u"csvList")
        self.csvList.setEditable(True)

        self.importHeader.addWidget(self.csvList)

        self.importButton = QPushButton(self.centralwidget)
        self.importButton.setObjectName(u"importButton")

        self.importHeader.addWidget(self.importButton)


        self.verticalLayout_4.addLayout(self.importHeader)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.empty_page = QWidget()
        self.empty_page.setObjectName(u"empty_page")
        self.stackedWidget.addWidget(self.empty_page)
        self.graph_page = QWidget()
        self.graph_page.setObjectName(u"graph_page")
        self.gridLayout_3 = QGridLayout(self.graph_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.graphWidget = PlotWidget(self.graph_page)
        self.graphWidget.setObjectName(u"graphWidget")
        self.verticalLayout_7 = QVBoxLayout(self.graphWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.gridLayout_3.addWidget(self.graphWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.graph_page)
        self.sheet_page = QWidget()
        self.sheet_page.setObjectName(u"sheet_page")
        self.verticalLayout_3 = QVBoxLayout(self.sheet_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sheetWidget = QTableView(self.sheet_page)
        self.sheetWidget.setObjectName(u"sheetWidget")

        self.verticalLayout_2.addWidget(self.sheetWidget)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.sheet_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.viewButtons = QHBoxLayout()
        self.viewButtons.setObjectName(u"viewButtons")
        self.graphButton = QPushButton(self.centralwidget)
        self.graphButton.setObjectName(u"graphButton")

        self.viewButtons.addWidget(self.graphButton)

        self.sheetButton = QPushButton(self.centralwidget)
        self.sheetButton.setObjectName(u"sheetButton")

        self.viewButtons.addWidget(self.sheetButton)


        self.verticalLayout_4.addLayout(self.viewButtons)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.csvList.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Select Data", None))
        self.importButton.setText(QCoreApplication.translate("mainWindow", u"Import", None))
        self.graphButton.setText(QCoreApplication.translate("mainWindow", u"Graph View", None))
        self.sheetButton.setText(QCoreApplication.translate("mainWindow", u"Sheet View", None))
    # retranslateUi

