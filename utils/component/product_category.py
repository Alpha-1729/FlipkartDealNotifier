import string


class ProductCategory:
    product_category_id: int
    category_name: string

    def __init__(
            self,
            product_category_id=None,
            category_name=None
    ):
        self.product_category_id = product_category_id
        self.category_name = category_name
