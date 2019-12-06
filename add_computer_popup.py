import tkinter as tk
from tkinter import messagebox
import requests
from abstract_product import AbstractProduct

class AddComputerPopup(tk.Frame):
    """ Popup Frame to Add a Car """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="Name:").grid(row=1, column=1)
        self._name = tk.Entry(self)
        self._name.grid(row=1, column=2)
        tk.Label(self, text="Price:").grid(row=2, column=1)
        self._price = tk.Entry(self)
        self._price.grid(row=2, column=2)
        tk.Label(self, text="Cost:").grid(row=3, column=1)
        self._cost = tk.Entry(self)
        self._cost.grid(row=3, column=2)
        tk.Label(self, text="Data Stocked:").grid(row=4, column=1)
        self._date_stocked = tk.Entry(self)
        self._date_stocked.grid(row=4, column=2)
        tk.Label(self, text="Date Sold:").grid(row=6, column=1)
        self._date_sold = tk.Entry(self)
        self._date_sold.grid(row=6, column=2)
        tk.Label(self, text="Is Sold:").grid(row=5, column=1)
        self._is_sold = tk.Entry(self)
        self._is_sold.grid(row=5, column=2)
        tk.Label(self, text="Graphics Card:").grid(row=7, column=1)
        self._graphics_card = tk.Entry(self)
        self._graphics_card.grid(row=7, column=2)
        tk.Label(self, text="Case:").grid(row=8, column=1)
        self._case = tk.Entry(self)
        self._case.grid(row=8, column=2)
        tk.Label(self, text="Memory Type:").grid(row=9, column=1)
        self._memory_type = tk.Entry(self)
        self._memory_type.grid(row=9, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=11, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=11, column=2)

    def _submit_cb(self):
        """ Submit the Add Computer """
        data = {}
        data['name'] = str(self._name.get())
        data['price'] = int(self._price.get())
        data['cost'] = int(self._cost.get())
        data['date_stocked'] = str(self._date_stocked.get())
        data['date_sold'] = str(self._date_sold.get())
        data['is_sold'] = int(self._is_sold.get())
        data['graphics_card'] = str(self._graphics_card.get())
        data['case'] = str(self._case.get())
        data['memory_type'] = str(self._memory_type.get())
        data['type'] = AbstractProduct.COMPUTER_TYPE

        url = 'http://localhost:5000/product_manager/products'
        response = requests.post(url, json=data)
        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showwarning("Error", "Add Product Request Failed")