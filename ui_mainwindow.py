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

class Ui_ORCID_parser(object):
    def setupUi(self, ORCID_parser):
        if not ORCID_parser.objectName():
            ORCID_parser.setObjectName(u"ORCID_parser")
        ORCID_parser.resize(428, 600)
        self.centralwidget = QWidget(ORCID_parser)
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

        ORCID_parser.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ORCID_parser)
        self.statusbar.setObjectName(u"statusbar")
        ORCID_parser.setStatusBar(self.statusbar)

        self.retranslateUi(ORCID_parser)

        QMetaObject.connectSlotsByName(ORCID_parser)
    # setupUi

    def retranslateUi(self, ORCID_parser):
        ORCID_parser.setWindowTitle(QCoreApplication.translate("ORCID_parser", u"MainWinodw", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("ORCID_parser", u"Enter", None))
    # retranslateUi

