from utils.component.product import Product


def get_formatted_message(product: Product):
    message = "ProductName: {}\n\nActualPrice: {}\n\nOfferPrice: {}\n\nProductLink: {}\n\n".format(
        product.product_name,
        product.actual_price,
        product.offer_price,
        product.product_url,
    )
    return message
