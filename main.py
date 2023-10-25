import pyflipper_functions

API_KEY = pyflipper_functions.import_api_key("config.json")
BAZAAR_DATA = pyflipper_functions.get_bazaar_data(API_KEY)
BAZAAR_LAST_UPDATED = pyflipper_functions.return_bazaar_datetime(BAZAAR_DATA)
BAZAAR_PRODUCT_INFO = pyflipper_functions.return_bazaar_product_info(BAZAAR_DATA)
BAZAAR_PRODUCTS = []

for product in BAZAAR_PRODUCT_INFO:
    BAZAAR_PRODUCTS.append(pyflipper_functions.BazaarItem(BAZAAR_PRODUCT_INFO[product]["quick_status"]))

print(f"Last updated: {BAZAAR_LAST_UPDATED}")

