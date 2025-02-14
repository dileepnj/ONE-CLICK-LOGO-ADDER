# styles/theme.py

import tkinter as tk
from tkinter import ttk

def apply_theme(root):
    """
    Applies the red and yellow color theme to the application.
    :param root: The main Tkinter root window.
    """
    # Define the color palette
    BACKGROUND_COLOR = "#FFA500"  # Yellow
    FOREGROUND_COLOR = "#FF0000"  # Red
    BUTTON_COLOR = "#FFD700"      # Gold (for buttons)
    SLIDER_COLOR = "#FF4500"      # OrangeRed (for sliders)

    # Configure the global style
    style = ttk.Style(root)
    
    # General background and foreground colors
    style.configure(".", background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
    
    # Frame styling
    style.configure("TFrame", background=BACKGROUND_COLOR)
    
    # Label styling
    style.configure("TLabel", background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, font=("Arial", 10, "bold"))
    
    # Button styling
    style.configure("TButton", background=BUTTON_COLOR, foreground=FOREGROUND_COLOR, font=("Arial", 10, "bold"))
    style.map("TButton", background=[("active", BUTTON_COLOR), ("pressed", "#FF8C00")])  # Hover effect
    
    # Slider styling
    style.configure("Horizontal.TScale", background=BACKGROUND_COLOR, troughcolor=SLIDER_COLOR, sliderthickness=20)
    style.map("Horizontal.TScale", background=[("active", SLIDER_COLOR)])
    
    # Canvas styling
    style.configure("TCanvas", background=BACKGROUND_COLOR)