import tkinter as tk
from PIL import Image, ImageTk

def set_background(root, image_path, bg_color='lightblue'):
    try:
        image = Image.open(image_path)
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        