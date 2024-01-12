import tkinter as tk
from PIL import Image, ImageTk

def set_background(root, image_path, bg_color='lightblue'):
    # Load the image
    original_image = Image.open(image_path)
    original_photo = ImageTk.PhotoImage(original_image)  # Keep a reference to avoid garbage collection

    # Create a label and place it to cover the entire window
    label = tk.Label(root, bg=bg_color)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    def resize_image(event):
        # Resize the image to match the new window size
        new_image = original_image.resize((event.width, event.height), Image.Resampling.LANCZOS)
        new_photo = ImageTk.PhotoImage(new_image)

        # Set the resized image
        label.config(image=new_photo)
        label.image = new_photo  

    # Initially set the image
    label.config(image=original_photo)
    label.image = original_photo

    # Bind the resize_image function to the window's resize event
    root.bind('<Configure>', resize_image)