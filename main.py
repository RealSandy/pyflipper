import json
import requests
import datetime


def import_api_key(path_to_file):
    f = open(path_to_file, "r")
    data = json.load(f)
    return data['api_key']


def get_bazaar_data(api_key):
    r = requests.get(f"https://api.hypixel.net/skyblock/bazaar?key={api_key}")
    data = r.json()
    return data


def return_bazaar_datetime(data):
    unix = data['lastUpdated']
    return datetime.datetime.fromtimestamp(unix)
