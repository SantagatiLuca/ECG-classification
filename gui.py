import sys
from PySide6 import QtWidgets
from src.main_window import Ui_MainWindow
from src.actions import MainWindowHandlers


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # load the UI
        self.setupUi(self)
        # handlers (for events, actions etc.)
        self.handlers = MainWindowHandlers(self)
        self._connect_signals()

    def _connect_signals(self):
        #Connect UI elements to their handlers
        self.settings.clicked.connect(self.handlers.settings_button_click)
        self.addfile.clicked.connect(self.handlers.addfile_button_click)
        self.view.clicked.connect(self.handlers.view_button_click)
        #self.actionOpen.triggered.connect(self.handlers.handle_open_action) # actions


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()


# Start the event loop.
if __name__ == '__main__':
    app.exec()
    
#------------------------------------------------------------------------------
# https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/
