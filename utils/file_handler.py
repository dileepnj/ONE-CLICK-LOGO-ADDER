# utils/file_handler.py

import tkinter as tk
from tkinter import filedialog

class FileHandler:
    @staticmethod
    def select_logo_file():
        """
        Opens a file dialog to select a logo file.
        :return: Path to the selected logo file, or None if canceled.
        """
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(
            title="Select Logo File",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All Files", "*.*")]
        )
        root.destroy()  # Destroy the hidden root window
        return file_path if file_path else None

    @staticmethod
    def select_image_folder():
        """
        Opens a folder dialog to select an image folder.
        :return: Path to the selected folder, or None if canceled.
        """
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        folder_path = filedialog.askdirectory(
            title="Select Image Folder"
        )
        root.destroy()  # Destroy the hidden root window
        return folder_path if folder_path else None