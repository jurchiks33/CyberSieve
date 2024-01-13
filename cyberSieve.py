import tkinter as tk
from tkinter import ttk
from bakground_image import set_background
from screen_setup import setup_screen
import pandas as pd
import requests
from bs4 import BeautifulSoup

root = tk.Tk()

    # Here will be web scrapping logic.
def start_scrapping():
    url = url_entry.get()
    #Check if the URL is empty
    if not url:
        print({"No URL provided."})
        return
    try:
        #Fetch content from URL.
        response = requests.get(url)
        response.raise_for_status()

        #Parse the content with BeautifulSoup.
        soup = BeautifulSoup(response.text, 'html.parser')
        

    print(f"Scrapping {url}")

def export_to_excel():
    #Here is coming logic for export to excel.
    print(f"Exporting data to Excel")

#Set up GUI elements.
url_entry = tk.Entry(root) #Entry widget for url.
url_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

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
