import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenmmheight()

window_width = int(screen_width * 0.7)
window_height = int(screen_height * 0.7)

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)