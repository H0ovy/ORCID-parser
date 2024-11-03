# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWinodw(object):
    def setupUi(self, MainWinodw):
        if not MainWinodw.objectName():
            MainWinodw.setObjectName(u"MainWinodw")
        MainWinodw.resize(428, 600)
        self.centralwidget = QWidget(MainWinodw)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"ORCIDlogo.png"))

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"font: 12pt \"Arial\";")

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"font: 12pt \"Arial\";")

        self.verticalLayout.addWidget(self.textBrowser)

        MainWinodw.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWinodw)
        self.statusbar.setObjectName(u"statusbar")
        MainWinodw.setStatusBar(self.statusbar)

        self.retranslateUi(MainWinodw)

        QMetaObject.connectSlotsByName(MainWinodw)
    # setupUi

    def retranslateUi(self, MainWinodw):
        MainWinodw.setWindowTitle(QCoreApplication.translate("MainWinodw", u"ORCID parser", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWinodw", u"Enter", None))
    # retranslateUi

