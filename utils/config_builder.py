def get_url_from_filter(product_filter):
    url = r"https://www.flipkart.com/"

    for key, value in product_filter.items():
        if type(value) == type(list()):
            for item in value:
                url += key + item
        else:
            url += key + value
    return url
