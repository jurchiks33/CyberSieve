import tkinter as tk
from PIL import Image, ImageTk

def set_background(root, image_path, bg_color='lightblue'):
    try:
        image = Image.open(image_path)
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(root, image=photo, bg=bg_color)
        label.image = photo 
        label.place(relx=0.5, rely=0.5, anchor='center')
    except IOError:
        print("Image cant be loaded, please check the file path.")