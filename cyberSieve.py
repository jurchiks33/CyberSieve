import tkinter as tk
from tkinter import ttk
from bakground_image import set_background
from screen_setup import setup_screen
from scraper_logic import scrape_website
import pandas as pd
import requests
from bs4 import BeautifulSoup

root = tk.Tk()

tag_options = ['p', 'div', 'h1', 'span', 'a']
tag_var = tk.StringVar(root)
tag_var.set(tag_options[0])
tag_menu = tk.OptionMenu(root, tag_var, *tag_options)
tag_menu.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

keyword_entry = tk.Entry(root)
keyword_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    # Here will be web scrapping logic.
def start_scrapping():
    url = url_entry.get()
    css_selector = css_selector_entry.get()
    # Clear existing data in the table
    for i in data_table.get_children():
        data_table.delete(i)

    if not url or not css_selector:
        print("URL or CSS selector is missing")
        return

    scraped_data = scrape_website(url, css_selector)
    for text in scraped_data:
        data_table.insert('', 'end', values=(text, '', ''))

def export_to_excel():
    #Here is coming logic for export to excel.
    print(f"Exporting data to Excel")

#Set up GUI elements.
url_entry = tk.Entry(root) #Entry widget for url.
url_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

css_selector_entry = tk.Entry(root)
css_selector_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

scrape_button = tk.Button(root, text="Scrape", command=start_scrapping)
scrape_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

columns = ('column1', 'column2', 'column3')  # Replace with actual column names
data_table = ttk.Treeview(root, show='headings')  
data_table['columns'] = columns  

for col in columns:
    data_table.heading(col, text=col)  
    data_table.column(col, width=100)  

data_table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

export_button = tk.Button(root, text="Export to Excel", command=export_to_excel)
export_button.pack(side=tk.TOP, padx=10, pady=5)

setup_screen(root)

root.title("Web Scraping Tool")

root.after(10, lambda: set_background(root, 'background_image.jpg'))

root.mainloop()
