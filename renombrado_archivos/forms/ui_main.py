# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainkWUeeC.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 320)
        MainWindow.setMaximumSize(QSize(500, 320))
        MainWindow.setBaseSize(QSize(500, 320))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.otrosDatos = QGroupBox(self.centralwidget)
        self.otrosDatos.setObjectName(u"otrosDatos")
        self.otrosDatos.setGeometry(QRect(10, 160, 471, 111))
        self.prefixLabel = QLabel(self.otrosDatos)
        self.prefixLabel.setObjectName(u"prefixLabel")
        self.prefixLabel.setGeometry(QRect(10, 30, 58, 16))
        self.prefixName = QLineEdit(self.otrosDatos)
        self.prefixName.setObjectName(u"prefixName")
        self.prefixName.setGeometry(QRect(60, 30, 161, 21))
        self.maxDigitsLabel = QLabel(self.otrosDatos)
        self.maxDigitsLabel.setObjectName(u"maxDigitsLabel")
        self.maxDigitsLabel.setGeometry(QRect(250, 30, 141, 16))
        self.DigitsSpin = QSpinBox(self.otrosDatos)
        self.DigitsSpin.setObjectName(u"DigitsSpin")
        self.DigitsSpin.setGeometry(QRect(410, 30, 51, 22))
        self.DigitsSpin.setLayoutDirection(Qt.LeftToRight)
        self.DigitsSpin.setAutoFillBackground(False)
        self.DigitsSpin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.DigitsSpin.setMinimum(1)
        self.Renombrar = QPushButton(self.otrosDatos)
        self.Renombrar.setObjectName(u"Renombrar")
        self.Renombrar.setEnabled(False)
        self.Renombrar.setGeometry(QRect(10, 70, 451, 32))
        self.GrupoDeFicheros = QGroupBox(self.centralwidget)
        self.GrupoDeFicheros.setObjectName(u"GrupoDeFicheros")
        self.GrupoDeFicheros.setGeometry(QRect(10, 10, 471, 141))
        self.ImagesDirTextLine = QLineEdit(self.GrupoDeFicheros)
        self.ImagesDirTextLine.setObjectName(u"ImagesDirTextLine")
        self.ImagesDirTextLine.setEnabled(False)
        self.ImagesDirTextLine.setGeometry(QRect(10, 50, 451, 20))
        self.ImagesDirSelect = QPushButton(self.GrupoDeFicheros)
        self.ImagesDirSelect.setObjectName(u"ImagesDirSelect")
        self.ImagesDirSelect.setGeometry(QRect(10, 20, 81, 32))
        self.LabesDirTextLine = QLineEdit(self.GrupoDeFicheros)
        self.LabesDirTextLine.setObjectName(u"LabesDirTextLine")
        self.LabesDirTextLine.setEnabled(False)
        self.LabesDirTextLine.setGeometry(QRect(10, 110, 451, 21))
        self.LabelsDirSelect = QPushButton(self.GrupoDeFicheros)
        self.LabelsDirSelect.setObjectName(u"LabelsDirSelect")
        self.LabelsDirSelect.setGeometry(QRect(10, 80, 81, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Renombrado de im\u00e1genes y etiquetas", None))
        self.otrosDatos.setTitle(QCoreApplication.translate("MainWindow", u"Otros Datos", None))
        self.prefixLabel.setText(QCoreApplication.translate("MainWindow", u"Prefijo", None))
        self.prefixName.setInputMask("")
        self.prefixName.setText("")
        self.prefixName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prefijo", None))
        self.maxDigitsLabel.setText(QCoreApplication.translate("MainWindow", u"M\u00e1x. d\u00edgitos en nombre", None))
        self.Renombrar.setText(QCoreApplication.translate("MainWindow", u"Renombrar", None))
        self.GrupoDeFicheros.setTitle(QCoreApplication.translate("MainWindow", u"Selecci\u00f3n de rutas", None))
        self.ImagesDirTextLine.setInputMask("")
        self.ImagesDirTextLine.setText(QCoreApplication.translate("MainWindow", u"Im\u00e1genes", None))
        self.ImagesDirSelect.setText(QCoreApplication.translate("MainWindow", u"Im\u00e1genes", None))
        self.LabesDirTextLine.setText(QCoreApplication.translate("MainWindow", u"Etiquetas", None))
        self.LabelsDirSelect.setText(QCoreApplication.translate("MainWindow", u"Etiquetas", None))
    # retranslateUi

