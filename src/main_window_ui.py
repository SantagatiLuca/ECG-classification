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
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(973, 691)
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
        self.Menu.setMaximumSize(QSize(240, 16777215))
        self.Menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.Menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 40))
        self.frame.setMaximumSize(QSize(1000, 100))
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
        self.frame_2.setMaximumSize(QSize(1000, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.home_button = QPushButton(self.frame_2)
        self.home_button.setObjectName(u"home_button")

        self.verticalLayout_2.addWidget(self.home_button)

        self.view_model_button = QPushButton(self.frame_2)
        self.view_model_button.setObjectName(u"view_model_button")

        self.verticalLayout_2.addWidget(self.view_model_button)

        self.settings_button = QPushButton(self.frame_2)
        self.settings_button.setObjectName(u"settings_button")

        self.verticalLayout_2.addWidget(self.settings_button)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.Menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 40))
        self.frame_3.setMaximumSize(QSize(1000, 100))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.github_link_label = QLabel(self.frame_3)
        self.github_link_label.setObjectName(u"github_link_label")
        font = QFont()
        font.setUnderline(True)
        self.github_link_label.setFont(font)
        self.github_link_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.github_link_label.setOpenExternalLinks(False)

        self.horizontalLayout_6.addWidget(self.github_link_label)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.Menu)

        self.Center = QFrame(self.centralwidget)
        self.Center.setObjectName(u"Center")
        self.Center.setFrameShape(QFrame.Shape.StyledPanel)
        self.Center.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Center)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.Center)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 80))
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.center_title = QLabel(self.frame_4)
        self.center_title.setObjectName(u"center_title")
        self.center_title.setMinimumSize(QSize(0, 60))
        self.center_title.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(True)
        self.center_title.setFont(font1)

        self.verticalLayout_5.addWidget(self.center_title)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.Center)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.plot_frame = QFrame(self.frame_6)
        self.plot_frame.setObjectName(u"plot_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plot_frame.sizePolicy().hasHeightForWidth())
        self.plot_frame.setSizePolicy(sizePolicy1)
        self.plot_frame.setMinimumSize(QSize(0, 300))
        font2 = QFont()
        font2.setUnderline(True)
        font2.setStrikeOut(False)
        self.plot_frame.setFont(font2)
        self.plot_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.plot_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_9.addWidget(self.plot_frame)

        self.label_frame = QFrame(self.frame_6)
        self.label_frame.setObjectName(u"label_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_frame.sizePolicy().hasHeightForWidth())
        self.label_frame.setSizePolicy(sizePolicy2)
        self.label_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.label_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.real_label = QLabel(self.label_frame)
        self.real_label.setObjectName(u"real_label")

        self.horizontalLayout_4.addWidget(self.real_label)

        self.predicted_label = QLabel(self.label_frame)
        self.predicted_label.setObjectName(u"predicted_label")

        self.horizontalLayout_4.addWidget(self.predicted_label)


        self.verticalLayout_9.addWidget(self.label_frame)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.file_location_label = QLabel(self.frame_7)
        self.file_location_label.setObjectName(u"file_location_label")

        self.horizontalLayout_5.addWidget(self.file_location_label)

        self.file_dialog_button = QPushButton(self.frame_7)
        self.file_dialog_button.setObjectName(u"file_dialog_button")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.file_dialog_button.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.file_dialog_button)


        self.verticalLayout_9.addWidget(self.frame_7)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_3 = QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.model_label = QLabel(self.page_3)
        self.model_label.setObjectName(u"model_label")

        self.horizontalLayout_3.addWidget(self.model_label)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.Center)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.view_model_button.setText(QCoreApplication.translate("MainWindow", u"View Model", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.github_link_label.setToolTip(QCoreApplication.translate("MainWindow", u"Check out the project", None))
#endif // QT_CONFIG(tooltip)
        self.github_link_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#1a5fb4;\">github.com</span></p></body></html>", None))
        self.center_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">Home</span></p></body></html>", None))
        self.real_label.setText("")
        self.predicted_label.setText("")
        self.file_location_label.setText(QCoreApplication.translate("MainWindow", u"Select a file:", None))
        self.file_dialog_button.setText(QCoreApplication.translate("MainWindow", u"Add File", None))
        self.model_label.setText(QCoreApplication.translate("MainWindow", u"PlaceHolder", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

