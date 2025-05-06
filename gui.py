import sys
from PySide6 import QtWidgets
from src.main_window import Ui_MainWindow
from src.actions import MainWindowHandlers


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Create UI instance
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.handlers = MainWindowHandlers(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        self._connect_signals()

    def _connect_signals(self):
        #Connect UI elements to their handlers
        self.ui.home_button.clicked.connect(self.handlers.home_button_click)
        self.ui.view_model_button.clicked.connect(self.handlers.view_model_button_click)
        self.ui.settings_button.clicked.connect(self.handlers.settings_button_click)
        self.ui.file_dialog_button.clicked.connect(self.handlers.file_dialog_click)
        #self.actionOpen.triggered.connect(self.handlers.handle_open_action) # actions


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
#------------------------------------------------------------------------------
# https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/
