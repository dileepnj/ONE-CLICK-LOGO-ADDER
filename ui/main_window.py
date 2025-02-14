# ui/main_window.py

import tkinter as tk
from tkinter import ttk
from styles.theme import apply_theme  # Import the theme for styling
from ui.controls_panel import ControlsPanel  # Import the controls panel
from ui.preview_panel import PreviewPanel  # Import the preview panel

class MainWindow:
    def __init__(self, root):
        self.root = root
        
        # Apply the red and yellow color theme
        apply_theme(self.root)
        
        # Create the main frame for the application
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create the controls panel (left side)
        self.controls_panel = ControlsPanel(self.main_frame)
        self.controls_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # Create the preview panel (right side)
        self.preview_panel = PreviewPanel(self.main_frame)
        self.preview_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)