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
            label.image = photo 
            label.place(relx=0.5, rely=0.5, anchor='center')
        except IOError:
            print("Image cant be loaded, please check the file path.")