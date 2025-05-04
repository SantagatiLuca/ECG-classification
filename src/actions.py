class MainWindowHandlers:
    def __init__(self, main_window):
        self.main_window = main_window
        self = main_window
    
    def addfile_button_click(self):
        """Example button handler"""
        print("Button Clicked!")
        self.main_window.setWindowTitle("Add File")

    def settings_button_click(self):
        """Example button handler"""
        print("Button Clicked!")
        self.main_window.setWindowTitle("Settings")

    def view_button_click(self):
        """Example button handler"""
        print("Button Clicked!")
        self.main_window.setWindowTitle("View")
    
    def handle_open_action(self):
        """Example menu action handler"""
        print("Open action triggered")
        # Access any UI element through self.ui