import tkinter as tk
from tkinter import ttk
from bakground_image import set_background
from screen_setup import setup_screen
from scraper_logic import scrape_website
import pandas as pd
import requests
from bs4 import BeautifulSoup

def on_entry_click(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, tk.END)
        entry.config(fg='black')

def on_focusout(event, entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.config(fg='grey')

root = tk.Tk()

tag_options = ['p', 'div', 'h1', 'span', 'a']

tag_var = tk.StringVar(root)
tag_var.set(tag_options[0])

#Dropdown for tag selection
tag_menu = tk.OptionMenu(root, tag_var, *tag_options)
tag_menu.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

#Entry with placeholder for URL
default_url_text = 'Enter URL here...'
url_entry = tk.Entry(root, fg='grey')
url_entry.insert(0, default_url_text)
url_entry.bind('<FocusIn>', lambda event: on_entry_click(event, url_entry, default_url_text))
url_entry.bind('<FocusOut>', lambda event: on_focusout(event, url_entry, default_url_text))
url_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

#Entry with placeholder for CSS selector.
default_css_selector_text = 'Enter CSS selector...'
css_selector_entry = tk.Entry(root, fg='grey')
css_selector_entry.insert(0, default_css_selector_text)
css_selector_entry.bind('<FocusIn>', lambda event: on_entry_click(event, css_selector_entry, default_css_selector_text))
css_selector_entry.bind('<FocusOut>', lambda event: on_focusout(event, css_selector_entry, default_css_selector_text))
css_selector_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

keyword_entry = tk.Entry(root)
keyword_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    # Here will be web scrapping logic.
def start_scrapping():
    url = url_entry.get().strip()
    selected_tag = tag_var.get().strip()
    css_selector = css_selector_entry.get().strip()
    keyword = keyword_entry.get().strip()

    if url == default_url_text:  # Check if default text is present
            print("Please enter a URL.")
            return
    if css_selector == default_css_selector_text:  # Reset CSS selector if default text is present
            css_selector = ''

    # Clear existing data in the table
    for i in data_table.get_children():
        data_table.delete(i)

    if not url:
        print("No URL provided.")
        return

    if not css_selector and not selected_tag:
        print("tag or CSS selector is required")
        return

    scraped_data = scrape_website(url, tag=selected_tag if selected_tag else None, 
                                  keyword=keyword if keyword else None,
                                  css_selector=css_selector if css_selector else None)
    for text in scraped_data:
        if text:
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
