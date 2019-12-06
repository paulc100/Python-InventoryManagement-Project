from abstract_product import AbstractProduct
from datetime import datetime

class ProductStats:
    """ Statistics on Products """
    
    _product_manager = None

    #def __init__(self, total_num_products, num_computers, num_cellphones, avg_computer_cost, avg_cellphone_cost):
    def __init__(self, product_manager):
        self._product_manager = product_manager

    def get_total_num_products(self):
        all_products = self._product_manager.get_all()
        return len(all_products)

    def get_num_computers(self):
        all_computers = self._product_manager.get_all_by_type(AbstractProduct.COMPUTER_TYPE)
        return len(all_computers)

    def get_num_cellphones(self):
        all_cellphones = self._product_manager.get_all_by_type(AbstractProduct.CELLPHONE_TYPE)
        return len(all_cellphones)

    def get_avg_computer_profit(self):
        total_profit = 0
        num_computers = 0
        for comp in self._product_manager.get_all_by_type(AbstractProduct.COMPUTER_TYPE):
            profit = comp.get_price() - comp.get_cost()
            total_profit = total_profit + profit
            num_computers = num_computers + 1
        if num_computers == 0:
            return 0
        avg_profit = total_profit / num_computers
        return avg_profit

    def get_avg_cellphone_profit(self):
        total_profit = 0
        num_cellphones = 0
        for cell in self._product_manager.get_all_by_type(AbstractProduct.CELLPHONE_TYPE):
            profit = cell.get_price() - cell.get_cost()
            total_profit = total_profit + profit
            num_cellphones = num_cellphones + 1
        if num_cellphones == 0:
            return 0
        avg_profit = total_profit / num_cellphones
        return avg_profit

    def get_avg_computer_shelf_time(self):
        total_shelf_time = 0
        num_computers = 0
        for comp in self._product_manager.get_all_by_type(AbstractProduct.COMPUTER_TYPE):
            if self.is_null(comp.get_date_sold()) or self.is_null(comp.get_date_stocked()):
                continue
            date_diff = self.str_to_date(comp.get_date_sold()) - self.str_to_date(comp.get_date_stocked())
            shelf_time = date_diff.days
            total_shelf_time = total_shelf_time + shelf_time
            num_computers = num_computers + 1
        if num_computers == 0:
            return 0
        avg_computer_shelf_time = int(total_shelf_time / num_computers)
        return avg_computer_shelf_time

    def get_avg_cellphone_shelf_time(self):
        total_shelf_time = 0
        num_cellphones = 0
        for cell in self._product_manager.get_all_by_type(AbstractProduct.CELLPHONE_TYPE):
            if self.is_null(cell.get_date_sold()) or self.is_null(cell.get_date_stocked()):
                continue
            date_diff = self.str_to_date(cell.get_date_sold()) - self.str_to_date(cell.get_date_stocked())
            shelf_time = date_diff.days
            total_shelf_time = total_shelf_time + shelf_time
            num_cellphones = num_cellphones + 1
        if num_cellphones == 0:
            return 0
        avg_cellphone_shelf_time = int(total_shelf_time / num_cellphones)
        return avg_cellphone_shelf_time

    def str_to_date(self, date_str):
        date = datetime.strptime(date_str, "%m/%d/%Y")
        return date

    def is_null(self, date):
        if date is None or date.strip() == "":
            return True
        else:
            return False