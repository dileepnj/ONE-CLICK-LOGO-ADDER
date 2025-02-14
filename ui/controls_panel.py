# ui/controls_panel.py

import tkinter as tk
from tkinter import ttk
from utils.file_handler import FileHandler  # For file uploads and folder selection
from utils.image_processor import ImageProcessor  # For applying the logo to images

class ControlsPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Initialize default logo parameters
        self.logo_params = {
            "width": 100,
            "height": 100,
            "opacity": 100,
            "x": 0,
            "y": 0
        }
        
        # Logo file path and image folder path
        self.logo_file_path = None
        self.image_folder_path = None
        
        # Create UI elements
        self.create_ui_elements()

    def create_ui_elements(self):
        # Title Label
        title_label = ttk.Label(self, text="Logo Parameters", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        
        # Logo Width Slider
        ttk.Label(self, text="Width").pack()
        self.width_slider = ttk.Scale(self, from_=50, to=500, orient=tk.HORIZONTAL, command=self.update_width)
        self.width_slider.set(self.logo_params["width"])
        self.width_slider.pack(fill=tk.X, padx=10)
        
        # Logo Height Slider
        ttk.Label(self, text="Height").pack()
        self.height_slider = ttk.Scale(self, from_=50, to=500, orient=tk.HORIZONTAL, command=self.update_height)
        self.height_slider.set(self.logo_params["height"])
        self.height_slider.pack(fill=tk.X, padx=10)
        
        # Opacity Slider
        ttk.Label(self, text="Opacity").pack()
        self.opacity_slider = ttk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.update_opacity)
        self.opacity_slider.set(self.logo_params["opacity"])
        self.opacity_slider.pack(fill=tk.X, padx=10)
        
        # Horizontal Position Slider
        ttk.Label(self, text="Horizontal Position").pack()
        self.x_slider = ttk.Scale(self, from_=0, to=800, orient=tk.HORIZONTAL, command=self.update_x_position)
        self.x_slider.set(self.logo_params["x"])
        self.x_slider.pack(fill=tk.X, padx=10)
        
        # Vertical Position Slider
        ttk.Label(self, text="Vertical Position").pack()
        self.y_slider = ttk.Scale(self, from_=0, to=600, orient=tk.HORIZONTAL, command=self.update_y_position)
        self.y_slider.set(self.logo_params["y"])
        self.y_slider.pack(fill=tk.X, padx=10)
        
        # Upload Logo Button
        self.upload_logo_button = ttk.Button(self, text="Upload Logo", command=self.upload_logo)
        self.upload_logo_button.pack(pady=10)
        
        # Select Image Folder Button
        self.select_folder_button = ttk.Button(self, text="Select Image Folder", command=self.select_image_folder)
        self.select_folder_button.pack(pady=10)
        
        # Add Logo Button
        self.add_logo_button = ttk.Button(self, text="Add Logo to Images", command=self.add_logo_to_images)
        self.add_logo_button.pack(pady=20)

    def update_width(self, value):
        self.logo_params["width"] = int(float(value))

    def update_height(self, value):
        self.logo_params["height"] = int(float(value))

    def update_opacity(self, value):
        self.logo_params["opacity"] = int(float(value))

    def update_x_position(self, value):
        self.logo_params["x"] = int(float(value))

    def update_y_position(self, value):
        self.logo_params["y"] = int(float(value))

    def upload_logo(self):
        # Open file dialog to select a logo file
        self.logo_file_path = FileHandler.select_logo_file()
        if self.logo_file_path:
            print(f"Logo uploaded: {self.logo_file_path}")

    def select_image_folder(self):
        # Open folder dialog to select an image folder
        self.image_folder_path = FileHandler.select_image_folder()
        if self.image_folder_path:
            print(f"Image folder selected: {self.image_folder_path}")

    def add_logo_to_images(self):
        if not self.logo_file_path or not self.image_folder_path:
            print("Please upload a logo and select an image folder first.")
            return
        
        # Process images and add logo
        try:
            ImageProcessor.add_logo_to_images(
                logo_path=self.logo_file_path,
                image_folder=self.image_folder_path,
                params=self.logo_params
            )
            print("Logo added to all images successfully!")
        except Exception as e:
            print(f"Error adding logo: {e}")