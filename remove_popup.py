import tkinter as tk
from tkinter import messagebox
import requests

class RemovePopup(tk.Frame):
    """ Popup Frame to Remove a Car """

    def __init__(self, parent, close_callback, product):
        """ Constructor """

        self._product = product
        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="ID:").grid(row=1, column=1)
        tk.Label(self, text=product["id"]).grid(row=1, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=7, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=7, column=2)

    def _submit_cb(self):
        """ Submit Remove Vehicle """
        id = str(self._product["id"])

        url = 'http://localhost:5000/product_manager/products/' + id
        response = requests.delete(url)
        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showwarning("Error", "Remove Product Request Failed")