import tkinter as tk
from bakground_image import set_background
import pandas as pd

def start_scrapping():
    url = url_entry.get()
    # Here will be web scrapping logic.
    print(f"Scrapping {url}")

def export_to_excel():
    #Here is coming logic for export to excel.
    print(f"Exporting data to Excel")

#Set up GUI elements.
url_entry = tk.Entry(root) #Entry widget for url.
url_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

scrape_button = tk.Button(root, text="Scrape", command=start_scrapping)
scrape_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width * 0.7)
window_height = int(screen_height * 0.7)

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.title("Web Scraping Tool")

root.after(10, lambda: set_background(root, 'background_image.jpg'))

root.mainloop()
