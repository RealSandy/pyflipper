import json
import requests
import datetime


class BazaarItem:
    def __init__(self, product_data):
        self.product_data = product_data
        self.item_id = self.product_data['productId']
        self.margin = self.calculate_margin()
        self.buy_volume = self.product_data['buyVolume']
        self.sell_volume = self.product_data['sellVolume']
        print(self.product_data, "\n", self.margin, self.buy_volume, self.sell_volume)

    def calculate_margin(self):
        sell_order_price = self.product_data["buyPrice"]
        buy_order_price = self.product_data["sellPrice"]
        if int(buy_order_price == 0 or sell_order_price == 0):
            margin = 0
        else:
            profit = sell_order_price - buy_order_price
            margin = (profit * 100) / sell_order_price
        return margin


def import_api_key(path_to_file):
    f = open(path_to_file, "r")
    data = json.load(f)
    return data['api_key']


def get_bazaar_data(api_key):
    r = requests.get(f"https://api.hypixel.net/skyblock/bazaar?key={api_key}")
    data = r.json()
    if not data['success']:
        raise Exception("Sorry, but the API request failed")
    return data


def return_bazaar_datetime(data):
    unix = data['lastUpdated'] / 1000  # Divide by 1000 to convert to seconds (milliseconds by default)
    unix = int(unix)  # Round to nearest whole second
    return datetime.datetime.fromtimestamp(unix)


def return_bazaar_product_info(data):
    info = data['products']
    return info
