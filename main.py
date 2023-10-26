import pyflipper_functions

ITEMS_DATA = pyflipper_functions.get_items_data()
BAZAAR_DATA = pyflipper_functions.get_bazaar_data()
BAZAAR_LAST_UPDATED = pyflipper_functions.return_bazaar_datetime(BAZAAR_DATA)
BAZAAR_PRODUCT_INFO = pyflipper_functions.return_bazaar_product_info(BAZAAR_DATA)
BAZAAR_PRODUCTS = []

for product in BAZAAR_PRODUCT_INFO:
    BAZAAR_PRODUCTS.append(pyflipper_functions.BazaarItem(BAZAAR_PRODUCT_INFO[product]["quick_status"], ITEMS_DATA))

viable_flips = list(filter(lambda x: x.margin <= 56, BAZAAR_PRODUCTS))
viable_flips.sort(key=lambda x: x.margin, reverse=False)

for i in range(len(viable_flips)):
    print(f"#{len(viable_flips) - i} {viable_flips[i]}")

print(f"Last updated: {BAZAAR_LAST_UPDATED}")
