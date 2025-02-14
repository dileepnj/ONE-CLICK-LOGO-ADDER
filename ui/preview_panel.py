# ui/preview_panel.py

import tkinter as tk
from PIL import Image, ImageTk, ImageOps

class PreviewPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Load the dummy image
        self.dummy_image_path = "assets/dummy_image.png"
        self.dummy_image = Image.open(self.dummy_image_path).convert("RGBA")
        self.logo_image = None  # Placeholder for the uploaded logo
        
        # Create a canvas to display the preview
        self.canvas_width = 800
        self.canvas_height = 600
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Display the initial dummy image
        self.display_dummy_image()

    def display_dummy_image(self):
        """Displays the dummy image on the canvas."""
        self.photo = ImageTk.PhotoImage(self.dummy_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def update_preview(self, logo_params):
        """
        Updates the preview with the logo applied to the dummy image.
        :param logo_params: A dictionary containing logo parameters (width, height, opacity, x, y).
        """
        if not self.logo_image:
            return  # Do nothing if no logo is uploaded
        
        # Resize the logo based on width and height parameters
        logo_resized = self.logo_image.resize(
            (logo_params["width"], logo_params["height"]), Image.ANTIALIAS
        )
        
        # Adjust opacity
        logo_with_opacity = Image.new("RGBA", logo_resized.size)
        logo_with_opacity.paste(logo_resized, (0, 0), logo_resized)
        alpha = int((logo_params["opacity"] / 100) * 255)
        logo_with_opacity.putalpha(alpha)
        
        # Create a copy of the dummy image to overlay the logo
        preview_image = self.dummy_image.copy()
        preview_image.paste(logo_with_opacity, (logo_params["x"], logo_params["y"]), logo_with_opacity)
        
        # Update the canvas with the new preview image
        self.photo = ImageTk.PhotoImage(preview_image)
        self.canvas.delete("all")  # Clear the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def set_logo_image(self, logo_path):
        """
        Sets the uploaded logo image.
        :param logo_path: Path to the uploaded logo file.
        """
        try:
            self.logo_image = Image.open(logo_path).convert("RGBA")
            print(f"Logo loaded for preview: {logo_path}")
        except Exception as e:
            print(f"Error loading logo for preview: {e}")