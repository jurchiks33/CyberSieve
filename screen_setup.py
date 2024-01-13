import tkinter as tk

def setup_screen(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = int(screen_width * 0.7)
    window_height = int(screen_height * 0.7)

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')