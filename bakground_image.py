import tkinter as tk
from PIL import Image, ImageTk

def set_background(root, image_path, bg_color='lightblue'):
    def resize_and_set_image():
        try:
            # Make sure the window size is updated
            root.update_idletasks()
            # Now we can fetch the correct dimensions
            window_width = root.winfo_width()
            window_height = root.winfo_height()
            
            # Load and resize the image to fit the window
            image = Image.open(image_path)
            image = image.resize((window_width, window_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            label = tk.Label(root, image=photo, bg=bg_color)
            label.image = photo  # Keep a reference
            label.place(x=0, y=0, relwidth=1, relheight=1)
        except IOError:
            print("Image can't be loaded, please check the file path.")

    root.after(100, resize_and_set_image)