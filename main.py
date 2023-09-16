# Script to notify the best deals for your customized category of products in flipkart.

import time

from utils.flipkart_client import ProductGrabber
from utils.component.product_category import ProductCategory
from utils.constants import delay, config, useragent
from utils import db_client, message_builder, telegram_client, json_reader, flipkart_client, config_builder

db_client = db_client.SQliteDbClient(config.SQLITE_CONNECTION_STRING)
json_reader = json_reader.JsonReader(config.JSON_PATH)
telegram = telegram_client.TelegramClient()

telegram.sent_message("Flipkart Deal Notifier bot started.")

while True:
    # Read filter config from json file.
    filter_dict = json_reader.read_json_as_dict()
    
    # Insert all product categories into database.
    for category_name in filter_dict.keys():
        product_category = ProductCategory()
        product_category.category_name = category_name
        db_client.save_product_category(product_category)
    product_category_list = db_client.get_product_categories()
    
    # Get all products from db.
    product_list = db_client.get_products()

    # Capture the price of all products and update in db.
    for product_category in product_category_list:
        product_category_filter_url = config_builder.get_url_from_filter(filter_dict.get(product_category.category_name))
        page_count = flipkart_client.get_page_count(product_category_filter_url)

        for page_num in range(1, page_count + 1):
            product_category_page_url = flipkart_client.get_next_page_url(product_category_filter_url, page_num)
            product_links = flipkart_client.get_product_links(product_category_page_url, useragent.WINDOWS)

            for product_url in product_links:
                product_grabber = ProductGrabber(product_url)
                product = product_grabber.get_product_info()
                product.product_category_id = product_category.product_category_id

                if product.actual_price > 0:
                    product_in_db = next((prod for prod in product_list if prod.product_name == product.product_name), None)

                    if product_in_db is None:
                        db_client.save_product(product)
                    else:
                        if product.offer_price < product_in_db.offer_price:
                            db_client.update_product_price(product)
    
    # Get all products from db.
    product_list = db_client.get_products()

    # Sent notification in the telegram for unreported products.
    for product in product_list:
        if not product.is_reported:
            formatted_message = message_builder.get_formatted_message(product)
            telegram.sent_message(formatted_message)
            db_client.update_reported_product(product)
            time.sleep(delay.MESSAGE_INTERVAL_DELAY)

    time.sleep(delay.NEXT_RUN_DELAY)
