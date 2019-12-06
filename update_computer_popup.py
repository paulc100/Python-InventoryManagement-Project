import tkinter as tk
from tkinter import messagebox
import requests

class UpdateComputerPopup(tk.Frame):
    """ Popup Frame to Sell a Vehicle """

    def __init__(self, parent, close_callback, product):
        """ Constructor """

        self._product = product
        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="ID:").grid(row=1, column=1)
        tk.Label(self, text=product["id"]).grid(row=1, column=2)
        tk.Label(self, text="Name:").grid(row=2, column=1)
        tk.Label(self, text=product["name"]).grid(row=2, column=2)
        tk.Label(self, text="Price:").grid(row=3, column=1)
        self._price = tk.Entry(self)
        self._price.grid(row=3, column=2)
        self._price.insert(0, product["price"])
        tk.Label(self, text="Cost:").grid(row=4, column=1)
        tk.Label(self, text=product["cost"]).grid(row=4, column=2)
        tk.Label(self, text="Data Stocked:").grid(row=5, column=1)
        tk.Label(self, text=product["date_stocked"]).grid(row=5, column=2)
        tk.Label(self, text="Date Sold:").grid(row=6, column=1)
        tk.Label(self, text=product["date_sold"]).grid(row=6, column=2)
        tk.Label(self, text="Is Sold:").grid(row=7, column=1)
        tk.Label(self, text=product["is_sold"]).grid(row=7, column=2)
        tk.Label(self, text="Case:").grid(row=8, column=1)
        self._case = tk.Entry(self)
        self._case.grid(row=8, column=2)
        self._case.insert(0, product["case"])
        tk.Label(self, text="Graphics Card:").grid(row=9, column=1)
        tk.Label(self, text=product["graphics_card"]).grid(row=9, column=2)
        tk.Label(self, text="Memory Type:").grid(row=10, column=1)
        tk.Label(self, text=product["memory_type"]).grid(row=10, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=12, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=12, column=2)

    def _submit_cb(self):
        """ Submit Update Computer """
        data = {}
        id = str(self._product["id"])
        data['price'] = int(self._price.get())
        data['case'] = str(self._case.get())

        url = 'http://localhost:5000/product_manager/products/' + id
        response = requests.put(url, json=data)
        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showwarning("Error", "Update Product Request Failed")