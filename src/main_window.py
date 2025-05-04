# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QSize(640, 480))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addfile = QPushButton(self.centralwidget)
        self.addfile.setObjectName(u"addfile")

        self.verticalLayout.addWidget(self.addfile)

        self.settings = QPushButton(self.centralwidget)
        self.settings.setObjectName(u"settings")

        self.verticalLayout.addWidget(self.settings)

        self.view = QPushButton(self.centralwidget)
        self.view.setObjectName(u"view")

        self.verticalLayout.addWidget(self.view)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addfile.setText(QCoreApplication.translate("MainWindow", u"Add File", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.view.setText(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi
