import tkinter as tk
from tkinter import messagebox
from tkinter import IntVar
import requests
from abstract_product import AbstractProduct
from add_computer_popup import AddComputerPopup
from add_cellphone_popup import AddCellphonePopup
from remove_popup import RemovePopup
from update_cellphone_popup import UpdateCellphonePopup
from update_computer_popup import UpdateComputerPopup
import json

class MainAppController(tk.Frame):
    """ Main Application for GUI """

    _selected_type = None

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Product Stats").grid(row=1, column=2)
        self._stats_listbox = tk.Listbox(self, height=8, width=160)
        self._stats_listbox.grid(row=2, column=1, columnspan=5)

        tk.Label(self, text="Products").grid(row=3, column=2)
        self._product_listbox = tk.Listbox(self, height=12, width=160)
        self._product_listbox.grid(row=4, column=1, columnspan=5)

        self._selection = IntVar()
        tk.Radiobutton(self, text="Computer", variable=self._selection, value=1, command=self._select_type).grid(row=5, column=1)
        tk.Radiobutton(self, text="Cellphone", variable=self._selection, value=2, command=self._select_type).grid(row=6, column=1)

        tk.Button(self, text="Add Product", command=self._add_product).grid(row=5, column=2)
        #tk.Button(self, text="Add Computer", command=self._add_computer).grid(row=5, column=1)
        #tk.Button(self, text="Add Cellphone", command=self._add_cellphone).grid(row=5, column=2)
        tk.Button(self, text="Update Product", command=self._update_product).grid(row=5, column=3)
        tk.Button(self, text="Remove Product", command=self._remove_product).grid(row=5, column=4)
        tk.Button(self, text="Quit", command=self._quit_callback).grid(row=6, column=2)

        self._update_products_list()
        self._get_product_stats()

    def _select_type(self):
        select = int(self._selection.get())
        if select == 1:
            self._selected_type = AbstractProduct.COMPUTER_TYPE
        elif select == 2:
            self._selected_type = AbstractProduct.CELLPHONE_TYPE
        self._update_products_list()

    def _add_product(self):
        if self._selected_type == AbstractProduct.COMPUTER_TYPE:
            self._add_computer()
        elif self._selected_type == AbstractProduct.CELLPHONE_TYPE:
            self._add_cellphone()

    def _add_computer(self):
        """ Add Car Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddComputerPopup(self._popup_win, self._close_computer_cb)

    def _close_computer_cb(self):
        """ Close Add Car Popup """
        self._popup_win.destroy()
        self._update_products_list()
        self._get_product_stats()

    def _add_cellphone(self):
        """ Add Truck Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddCellphonePopup(self._popup_win, self._close_cellphone_cb)

    def _close_cellphone_cb(self):
        """ Close Add Truck Popup """
        self._popup_win.destroy()
        self._update_products_list()
        self._get_product_stats()

    def _update_product(self):
        """ Sell Vehicle Popup """

        product = self._select_product()
        if len(product) == 0:
            return

        if product["is_sold"] != "" and int(product["is_sold"]) == 1:
            messagebox.showwarning("Error", "Please select an item that isn't sold")
            return

        self._popup_win = tk.Toplevel()
        if product["type"] == AbstractProduct.COMPUTER_TYPE:
            self._popup = UpdateComputerPopup(self._popup_win, self._close_update_cb, product)
        elif product["type"] == AbstractProduct.CELLPHONE_TYPE:
            self._popup = UpdateCellphonePopup(self._popup_win, self._close_update_cb, product)

    def _remove_product(self):
        """ Remove Product Popup """
        product = self._select_product()
        if len(product) == 0:
            return

        if product["is_sold"] != "" and int(product["is_sold"]) == 1:
            messagebox.showwarning("Error", "Please select an item that isn't sold")
            return

        self._popup_win = tk.Toplevel()
        self._popup = RemovePopup(self._popup_win, self._close_update_cb, product)

    def _close_update_cb(self):
        """ Close Update Vehicle Popup """
        self._popup_win.destroy()
        self._update_products_list()
        self._get_product_stats()

    def _quit_callback(self):
        """ Quit """
        self.quit()

    def _update_products_list(self):
        """ Update the List of Vehicle Descriptions """
        lines = []

        if self._selected_type == AbstractProduct.COMPUTER_TYPE or self._selected_type is None:
            url = 'http://localhost:5000/product_manager/products/all/Computer'
            response = requests.get(url)
            computers = response.json()
            lines.append("Computers")
            for computer in computers:
                lines.append(computer)
            lines.append("")

        if self._selected_type == AbstractProduct.CELLPHONE_TYPE or self._selected_type is None:
            url = 'http://localhost:5000/product_manager/products/all/Cellphone'
            response = requests.get(url)
            cellphones = response.json()
            lines.append("Cellphones")
            for cellphone in cellphones:
                lines.append(cellphone)

        self._product_listbox.delete(0, tk.END)
        for line in lines:
            self._product_listbox.insert(tk.END, line)

    def _get_product_stats(self):
        response = requests.get('http://localhost:5000/product_manager/products/stats')
        if response.status_code == 200:
            data = response.json()
            num_products = data['num_products']
            num_computers = data['num_computers']
            num_cellphones = data['num_cellphones']
            avg_computer_profit = data['avg_computer_profit']
            avg_cellphone_profit = data['avg_cellphone_profit']
            avg_computer_shelf_time = data['avg_computer_shelf_time']
            avg_cellphone_shelf_time = data['avg_cellphone_shelf_time']
            total_products = int(num_computers) + int(num_cellphones)
            total_profit = int(avg_computer_profit) + int(avg_cellphone_profit)

            self._stats_listbox.delete(0, tk.END)
            self._stats_listbox.insert(tk.END, "Product Statistics")
            self._stats_listbox.insert(tk.END, "")
            self._stats_listbox.insert(tk.END, "Number of products: " + str(num_products))
            self._stats_listbox.insert(tk.END, "Number of computers: " + str(num_computers))
            self._stats_listbox.insert(tk.END, "Number of cellphones: " + str(num_cellphones))
            self._stats_listbox.insert(tk.END, "Average computer profit: " + str(avg_computer_profit))
            self._stats_listbox.insert(tk.END, "Average cellphone profit: " + str(avg_cellphone_profit))
            self._stats_listbox.insert(tk.END, "Average computer shelf time: " + str(avg_computer_shelf_time))
            self._stats_listbox.insert(tk.END, "Average cellphone shelf time: " + str(avg_cellphone_shelf_time))
            self._stats_listbox.insert(tk.END, "Total profit: " + str(total_profit))
            self._stats_listbox.insert(tk.END, "Total products: " + str(total_products))

    def _select_product(self):
        product  = {}
        if (len(self._product_listbox.curselection()) == 0):
            messagebox.showwarning("Error", "Please select an item to remove")
            return product

        index = self._product_listbox.curselection()[0]
        product = self._product_listbox.get(index)
        product = product.replace("'", "\"")
        product = json.loads(product)
        return product

if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()