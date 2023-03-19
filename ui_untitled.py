# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(333, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.chooseFile = QPushButton(self.centralwidget)
        self.chooseFile.setObjectName(u"chooseFile")
        self.chooseFile.setGeometry(QRect(10, 510, 81, 25))
        self.display = QLabel(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(10, 10, 321, 481))
        self.fileName = QLineEdit(self.centralwidget)
        self.fileName.setObjectName(u"fileName")
        self.fileName.setGeometry(QRect(10, 540, 151, 25))
        self.startConvert = QPushButton(self.centralwidget)
        self.startConvert.setObjectName(u"startConvert")
        self.startConvert.setGeometry(QRect(230, 510, 81, 25))
        self.saveRoute = QPushButton(self.centralwidget)
        self.saveRoute.setObjectName(u"saveRoute")
        self.saveRoute.setGeometry(QRect(100, 510, 71, 25))
        self.fileName_1 = QLineEdit(self.centralwidget)
        self.fileName_1.setObjectName(u"fileName_1")
        self.fileName_1.setGeometry(QRect(170, 540, 151, 25))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.chooseFile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.display.setText("")
        self.startConvert.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.saveRoute.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84", None))
    # retranslateUi

