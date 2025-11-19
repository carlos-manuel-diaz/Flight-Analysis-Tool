# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orion_v2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QWidget(mainWindow)
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

        self.sheetView_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.sheetView_2.setObjectName(u"sheetView_2")

        self.viewButtons.addWidget(self.sheetView_2)

        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setGeometry(QRect(9, 60, 771, 481))
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(15, 51, 761, 501))
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.csvList.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Select Data", None))
        self.importButton.setText(QCoreApplication.translate("mainWindow", u"Import", None))
        self.graphView.setText(QCoreApplication.translate("mainWindow", u"Graph View", None))
        self.sheetView_2.setText(QCoreApplication.translate("mainWindow", u"Sheet View", None))
    # retranslateUi

