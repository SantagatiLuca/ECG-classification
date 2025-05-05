from PySide6.QtWidgets import QFileDialog

class MainWindowHandlers:
    def __init__(self, main_window):
        self.main_window = main_window  # Store reference to main window
        self.ui = main_window.ui  # Access to all UI elements
    
    def addfile_button_click(self):
        print("Button Clicked!")
        self.ui.center_title.setText("Adding file...")

    def settings_button_click(self):
        print("Button Clicked!")
        self.ui.center_title.setText("Settings")

    def view_button_click(self):
        print("Button Clicked!")
        self.ui.center_title.setText("View Model")
    
    def file_dialog_click(self):
        print("Adding file...")
        """Open a file dialog and process the selected file"""
        # Get the main window as parent for the dialog
        parent = self.main_window
        
        # Open file dialog and get the selected file path
        file_path, _ = QFileDialog.getOpenFileName(
            parent=parent,
            caption="Open File",
            dir="",  # Start in current directory
            filter="All Files (*)"
        )
        
        if file_path:  # Only proceed if a file was selected
            print("Data loaded correctly.")
            self._process_file(file_path)

    def _process_file(self,file_path):

        # Update the label with file information
        self.ui.hlabel.setText(f"File location: {file_path}")
        # Force immediate UI update (important for long operations)
        self.main_window.repaint()

    
    def handle_open_action(self):
        """Example menu action handler"""
        print("Open action triggered")
        # Access any UI element through self.ui 