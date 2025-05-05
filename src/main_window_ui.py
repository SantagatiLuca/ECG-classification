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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(867, 582)
        MainWindow.setMinimumSize(QSize(640, 480))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menu = QFrame(self.centralwidget)
        self.Menu.setObjectName(u"Menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Menu.sizePolicy().hasHeightForWidth())
        self.Menu.setSizePolicy(sizePolicy)
        self.Menu.setMinimumSize(QSize(130, 0))
        self.Menu.setMaximumSize(QSize(200, 16777215))
        self.Menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.Menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.frame = QFrame(self.Menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 40))
        self.frame.setMaximumSize(QSize(200, 100))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.Menu)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(100, 0))
        self.frame_2.setMaximumSize(QSize(200, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(200, 0))
        self.radioButton.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(200, 0))
        self.radioButton_2.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.frame_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(200, 0))
        self.radioButton_3.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_2.addWidget(self.radioButton_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.Menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 40))
        self.frame_3.setMaximumSize(QSize(200, 100))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.Menu)

        self.Center = QFrame(self.centralwidget)
        self.Center.setObjectName(u"Center")
        self.Center.setFrameShape(QFrame.Shape.StyledPanel)
        self.Center.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Center)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.Center)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 80))
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.center_title = QLabel(self.frame_4)
        self.center_title.setObjectName(u"center_title")
        self.center_title.setMinimumSize(QSize(0, 60))
        self.center_title.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.center_title.setFont(font)

        self.verticalLayout_5.addWidget(self.center_title)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.Center)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.hlabel = QLabel(self.frame_5)
        self.hlabel.setObjectName(u"hlabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hlabel.sizePolicy().hasHeightForWidth())
        self.hlabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.hlabel)

        self.file_dialog_button = QPushButton(self.frame_5)
        self.file_dialog_button.setObjectName(u"file_dialog_button")
        sizePolicy1.setHeightForWidth(self.file_dialog_button.sizePolicy().hasHeightForWidth())
        self.file_dialog_button.setSizePolicy(sizePolicy1)
        self.file_dialog_button.setMaximumSize(QSize(120, 30))
        self.file_dialog_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.file_dialog_button.setIcon(icon)
        self.file_dialog_button.setFlat(False)

        self.verticalLayout_6.addWidget(self.file_dialog_button)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.Center)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"New File", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"View Model", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.center_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">Default</span></p></body></html>", None))
        self.hlabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.file_dialog_button.setText(QCoreApplication.translate("MainWindow", u"Add File", None))
    # retranslateUi

