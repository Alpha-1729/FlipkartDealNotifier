import string


class Product:
    product_id: int
    product_name: string
    product_url: string
    product_category_id: int
    actual_price: float
    offer_price: float
    is_reported: bool

    def __init__(
            self,
            product_id=None,
            product_name=None,
            product_url=None,
            product_category_id=None,
            actual_price=None,
            offer_price=None,
            is_reported=None,
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.product_url = product_url
        self.product_category_id = product_category_id
        self.actual_price = actual_price
        self.offer_price = offer_price
        self.is_reported = is_reported
