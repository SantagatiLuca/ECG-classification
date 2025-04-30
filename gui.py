from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QDialog
from src.layout_colorwidget import Color
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ECG app")
        self.setMinimumSize(QSize(400,300))

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        button_action = QAction("&Save", self)
        button_action.triggered.connect(self.menu_save_clicked)
        button_action.setCheckable(False)

        button_action2 = QAction("&Open",self)
        button_action2.triggered.connect(self.menu_open_clicked)
        button_action2.setCheckable(False)

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addAction(button_action2)
 

    def menu_save_clicked(self):
        print("Saving file...")

    def menu_open_clicked(self):
        print("Open file: ...")
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All files (*)')
        if file_name:
            print(f'Selected file: {file_name}')

#------------------------------------------------------------------------------
app = QApplication(sys.argv)
window = MainWindow()
window.show()

# Start the event loop.
if __name__ == '__main__':
    app.exec()