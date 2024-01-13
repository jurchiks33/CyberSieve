import tkinter as tk
from PIL import Image, ImageTk

def set_background(root, image_path, bg_color='lightblue'):
    # Keep a reference to the label and photo in the function's scope
    label = tk.Label(root, bg=bg_color)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.photo = None

    def resize_image(event):
        nonlocal label  # Use the label defined in the outer scope
        # Resize the image to match the new window size
        new_image = Image.open(image_path).resize((event.width, event.height), Image.Resampling.LANCZOS)
        label.photo = ImageTk.PhotoImage(new_image)
        label.config(image=label.photo)

    # Bind the resize_image function to the window's resize event
    root.bind('<Configure>', resize_image)

    # Lower the background image label to ensure it doesn't cover other widgets
    label.lower()