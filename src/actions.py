import pandas as pd
import numpy as np
from PySide6.QtWidgets import QFileDialog, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT


class MainWindowHandlers:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = main_window.ui
        self.current_data = None  # To store loaded ECG data

    def home_button_click(self):
        print("Button Clicked!")
        self.ui.stackedWidget.setCurrentIndex(0)  # First page
        self.ui.center_title.setText("Home")

    def view_model_button_click(self):
        print("Button Clicked!")
        self.ui.stackedWidget.setCurrentIndex(1)  # Second page
        self.ui.center_title.setText("View Model")

    def settings_button_click(self):
        print("Button Clicked!")
        self.ui.stackedWidget.setCurrentIndex(2)  # Third page
        self.ui.center_title.setText("Settings")

    def file_dialog_click(self):
        """Handle file dialog and plot the selected ECG"""
        file_path, _ = QFileDialog.getOpenFileName(
            parent=self.main_window,
            caption="Open ECG File",
            dir="",
            filter="CSV Files (*.csv);;All Files (*)"
        )
        
        if file_path:
            self._process_file(file_path)  # This should call _plot_ecg internally
    
    def _process_file(self, file_path):
        """Load CSV and plot the ECG"""
        try:
            # Load the single-line CSV
            self.current_data = pd.read_csv(file_path, header=None)
            
            # Verify the shape (188 columns with last being label)
            if self.current_data.shape[1] != 188:
                raise ValueError("File must have exactly 188 columns")
                
            # Update UI
            self.ui.file_location_label.setText(f"Loaded: {file_path}")
            
            # Create the plot
            self._plot_ecg()  # Make sure this method exists
            
        except Exception as e:
            self.ui.file_location_label.setText(f"Error: {str(e)}")
    
    def _plot_ecg(self):
        """Plot the ECG data in the designated frame"""
        # Clear previous plot if exists
        if hasattr(self, 'canvas'):
            # Proper way to clear layout
            layout = self.ui.plot_frame.layout()
            if layout:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
        
        # Create matplotlib figure
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        # Extract values and label
        values = self.current_data.iloc[0, :-1].values
        label = "Normal" if self.current_data.iloc[0, -1] == 0 else "Abnormal"
        
        # Plot the ECG
        ax.plot(values, label=f'ECG (Label: {label})')
        ax.set_title('ECG Signal')
        ax.set_xlabel('Time steps')
        ax.set_ylabel('Amplitude')
        ax.legend()
        ax.grid(True)
        
        # Create canvas and add to frame
        self.canvas = FigureCanvasQTAgg(fig)
        
        # Ensure plot_frame has a layout
        if not self.ui.plot_frame.layout():
            self.ui.plot_frame.setLayout(QVBoxLayout())
        
        # Add navigation toolbar
        self.toolbar = NavigationToolbar2QT(self.canvas, self.ui.plot_frame)
        
        # Add widgets to frame
        self.ui.plot_frame.layout().addWidget(self.toolbar)
        self.ui.plot_frame.layout().addWidget(self.canvas)
        
        self.canvas.draw()