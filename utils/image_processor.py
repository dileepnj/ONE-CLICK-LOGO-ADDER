# utils/image_processor.py

import os
from PIL import Image

class ImageProcessor:
    @staticmethod
    def add_logo_to_images(logo_path, image_folder, params):
        """
        Adds the logo to all images in the specified folder.
        :param logo_path: Path to the logo file.
        :param image_folder: Path to the folder containing images.
        :param params: Dictionary containing logo parameters (width, height, opacity, x, y).
        """
        try:
            # Load the logo image
            logo = Image.open(logo_path).convert("RGBA")
            
            # Resize the logo based on width and height parameters
            logo_resized = logo.resize((params["width"], params["height"]), Image.ANTIALIAS)
            
            # Adjust opacity
            logo_with_opacity = Image.new("RGBA", logo_resized.size)
            logo_with_opacity.paste(logo_resized, (0, 0), logo_resized)
            alpha = int((params["opacity"] / 100) * 255)
            logo_with_opacity.putalpha(alpha)
            
            # Process each image in the folder
            for filename in os.listdir(image_folder):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_path = os.path.join(image_folder, filename)
                    
                    # Open the image
                    try:
                        image = Image.open(image_path).convert("RGBA")
                    except Exception as e:
                        print(f"Error opening image {filename}: {e}")
                        continue
                    
                    # Paste the logo onto the image at the specified position
                    image.paste(logo_with_opacity, (params["x"], params["y"]), logo_with_opacity)
                    
                    # Save the modified image
                    output_path = os.path.join(image_folder, f"modified_{filename}")
                    image.save(output_path, format="PNG")
                    print(f"Logo added to {filename} and saved as modified_{filename}")
            
            print("All images processed successfully!")
        
        except Exception as e:
            print(f"Error processing images: {e}")