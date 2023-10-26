# import json
import requests
import datetime


class BazaarItem:
    def __init__(self, product_data, items_data):
        self.ITEMS_DATA = items_data
        self.product_data = product_data

        self.item_id = self.product_data['productId']
        self.name = self.get_name_from_id()

        self.sell_order_price = self.product_data['buyPrice']
        self.buy_order_price = self.product_data['sellPrice']

        self.display_sell_order_price = add_commas_to_number(int(self.sell_order_price * 100) / 100)
        self.display_buy_order_price = add_commas_to_number(int(self.buy_order_price * 100) / 100)

        self.buy_volume = add_commas_to_number(self.product_data['buyVolume'])
        self.sell_volume = add_commas_to_number(self.product_data['sellVolume'])

        self.profit = self.calculate_profit()
        self.margin = self.calculate_margin()

        self.display_profit = add_commas_to_number(int(self.profit * 100) / 100)
        self.display_margin = int(self.margin * 100) / 100

        # print(self.item_id, self.name)
        # print(self.product_data, "\n", self.margin, self.buy_volume, self.sell_volume)
        # print(self)

    def calculate_margin(self):
        if int(self.buy_order_price == 0 or self.sell_order_price == 0):
            margin = 0
        else:
            margin = (self.profit * 100) / self.sell_order_price
        return margin

    def calculate_profit(self):
        if int(self.buy_order_price == 0 or self.sell_order_price == 0):
            profit = 0
        else:
            profit = self.sell_order_price - self.buy_order_price
        return profit

    def get_name_from_id(self):
        if self.item_id.startswith("ENCHANTMENT"):
            name = self.item_id
            name = name.lower()
            name = name.replace("_", " ")
            name = name.replace("enchantment ", "")
            name += " Book"
            name = name.title()
            name = name.replace("Bane Of Arthropods", "Bane of Arthropods")
            return name
        for material in self.ITEMS_DATA['items']:
            if material['id'] == self.item_id:
                return material['name']

    def __str__(self):
        string = f"""{self.name}: 
    Buy Order Price: {self.display_buy_order_price} coins
    Buy Volume: {self.buy_volume}
    Sell Order Price: {self.display_sell_order_price} coins
    Sell Volume: {self.sell_volume}
    Profit per Item: {self.display_profit} coins
    Profit Margin: {self.display_margin}%
"""
        return string


def get_bazaar_data():
    r = requests.get("https://api.hypixel.net/skyblock/bazaar")
    data = r.json()
    if not data['success']:
        raise Exception("Sorry, but the API request failed. Try again later.")
    return data


def return_bazaar_datetime(data):
    unix = data['lastUpdated'] / 1000  # Divide by 1000 to convert to seconds (milliseconds by default)
    unix = int(unix)  # Round to nearest whole second
    return datetime.datetime.fromtimestamp(unix)


def return_bazaar_product_info(data):
    info = data['products']
    return info


def get_items_data():
    r = requests.get("https://api.hypixel.net/resources/skyblock/items")
    data = r.json()
    if not data['success']:
        raise Exception("Sorry, but the API request failed. Try again later.")
    return data


def add_commas_to_number(number):
    return remove_trailing_zeroes(format(number, ",f"))


def remove_trailing_zeroes(string):
    return string.rstrip("0").rstrip(".")
