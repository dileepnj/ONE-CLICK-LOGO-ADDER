# main.py

import tkinter as tk
from ui.main_window import MainWindow

if __name__ == "__main__":
    # Initialize the main application window
    root = tk.Tk()
    
    # Set the title of the application
    root.title("One-Click Logo Adder")
    
    # Set the window size (optional)
    root.geometry("1000x600")  # Width x Height
    
    # Prevent resizing (optional)
    root.resizable(False, False)
    
    # Initialize the MainWindow class
    app = MainWindow(root)
    
    # Start the Tkinter event loop
    root.mainloop()