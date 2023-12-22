# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainTKPSiP.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 210)
        MainWindow.setMaximumSize(QSize(500, 210))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Formulario = QGroupBox(self.centralwidget)
        self.Formulario.setObjectName(u"Formulario")
        self.Formulario.setGeometry(QRect(10, 10, 481, 161))
        self.SelectLabelsDir = QPushButton(self.Formulario)
        self.SelectLabelsDir.setObjectName(u"SelectLabelsDir")
        self.SelectLabelsDir.setGeometry(QRect(20, 20, 161, 32))
        self.labelsDir = QLineEdit(self.Formulario)
        self.labelsDir.setObjectName(u"labelsDir")
        self.labelsDir.setGeometry(QRect(20, 50, 441, 21))
        self.CambiarLabel = QLabel(self.Formulario)
        self.CambiarLabel.setObjectName(u"CambiarLabel")
        self.CambiarLabel.setGeometry(QRect(20, 85, 58, 16))
        self.porLabel = QLabel(self.Formulario)
        self.porLabel.setObjectName(u"porLabel")
        self.porLabel.setGeometry(QRect(280, 86, 31, 16))
        self.cambiarButton = QPushButton(self.Formulario)
        self.cambiarButton.setObjectName(u"cambiarButton")
        self.cambiarButton.setEnabled(False)
        self.cambiarButton.setGeometry(QRect(20, 120, 441, 32))
        self.OrigenComboBox = QComboBox(self.Formulario)
        self.OrigenComboBox.setObjectName(u"OrigenComboBox")
        self.OrigenComboBox.setEnabled(False)
        self.OrigenComboBox.setGeometry(QRect(80, 80, 161, 32))
        self.OrigenComboBox.setEditable(False)
        self.DestinoComboBox = QComboBox(self.Formulario)
        self.DestinoComboBox.setObjectName(u"DestinoComboBox")
        self.DestinoComboBox.setEnabled(False)
        self.DestinoComboBox.setGeometry(QRect(310, 80, 161, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sustituci\u00f3n de clases en etiquetas", None))
        self.Formulario.setTitle(QCoreApplication.translate("MainWindow", u"Cambio de clase en labels", None))
        self.SelectLabelsDir.setText(QCoreApplication.translate("MainWindow", u"Directorio de etiquetas", None))
        self.labelsDir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleccione directorio de etiquetas", None))
        self.CambiarLabel.setText(QCoreApplication.translate("MainWindow", u"Cambiar", None))
        self.porLabel.setText(QCoreApplication.translate("MainWindow", u"Por", None))
        self.cambiarButton.setText(QCoreApplication.translate("MainWindow", u"Cambiar clases", None))
    # retranslateUi

