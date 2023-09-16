import sqlite3

from utils.constants import queries
from utils.component.product import Product
from utils.component.product_category import ProductCategory


class SQliteDbClient:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def save_product(self, product: Product):
        conn = sqlite3.connect(self.connection_string)
        cursor = conn.cursor()

        cursor.execute(queries.INSERT_PRODUCT, product.__dict__)
        conn.commit()

        cursor.close()

    def save_product_category(self, product_category: ProductCategory):
        conn = sqlite3.connect(self.connection_string)
        cursor = conn.cursor()

        cursor.execute(queries.INSERT_PRODUCT_CATEGORY, product_category.__dict__)
        conn.commit()

        cursor.close()

    def get_products(self):
        conn = sqlite3.connect(self.connection_string)
        cursor = conn.cursor()

        products = cursor.execute(queries.SELECT_PRODUCTS).fetchall()

        cursor.close()

        return [Product(*row) for row in products]

    def get_product_categories(self):
        conn = sqlite3.connect(self.connection_string)
        cursor = conn.cursor()

        product_categories = cursor.execute(queries.SELECT_PRODUCT_CATEGORIES).fetchall()

        cursor.close()

        return [ProductCategory(*row) for row in product_categories]

    def get_unreported_products(self):
        conn = sqlite3.connect(self.connection_string)
        cursor = conn.cursor()

        products = cursor.execute(queries.SELECT_UNREPORTED_PRODUCTS).fetchall()

        cursor.close()

        return [Product(*row) for row in products]

    def update_product_price(self, product: Product):
        conn = sqlite3.connect(self.connection_string)
        cursor = conn.cursor()

        cursor.execute(queries.UPDATE_PRODUCT_PRICE, product.__dict__)
        conn.commit()

        cursor.close()

    def update_reported_product(self, product: Product):
        conn = sqlite3.connect(self.connection_string)
        cursor = conn.cursor()

        cursor.execute(queries.UPDATE_REPORTED_PRODUCT, product.__dict__)
        conn.commit()

        cursor.close()
