import re
import requests
from bs4 import BeautifulSoup

from utils.constants import useragent
from utils.component.product import Product
from utils.thread_client import CustomThread


class ProductGrabber:
    def __init__(self, url):
        self.url = url

    def get_product_info(self):
        custom_thread_windows = CustomThread(target=get_webpage, args=(self.url, useragent.WINDOWS))
        custom_thread_android = CustomThread(target=get_webpage, args=(self.url, useragent.ANDROID))

        custom_thread_windows.start()
        custom_thread_android.start()

        product_page_windows = custom_thread_windows.join()
        product_page_android = custom_thread_android.join()

        product = Product()
        product.product_url = self.url
        product.product_name = get_product_name(product_page_windows)
        product.actual_price = get_product_price(product_page_windows)
        product.offer_price = get_offer_price(product_page_android)

        if product.offer_price is None:
            product.offer_price = product.actual_price

        product.is_reported = False

        return product


def get_offer_price(webpage_android):
    price = get_offer_price_with_regex(webpage_android)
    if price is None:
        price = get_offer_price_with_class(webpage_android)
        return price
    return price


def get_page_count(url):
    try:
        soup = get_webpage(url, useragent.WINDOWS)

        page_info = soup.find("div", attrs={"class": "_2MImiq"})
        last_index = page_info.span.text.split(" of ")[-1]
        return int(last_index)
    except AttributeError:
        return 1


def get_next_page_url(url, current_page):
    return url + "&page=" + str(current_page)


def get_webpage(url, user_agent=None):
    page = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup


def get_product_price(webpage_windows):
    try:
        price = webpage_windows.find("div", {"class": "_30jeq3 _16Jk6d"}).get_text().strip()[1:].replace(',', '')
        if price:
            return int(price)
        return -1
    except:
        return -1


def get_product_name(webpage_windows):
    product_name = (webpage_windows.find("span", {"class": "B_NuCI"}).get_text().strip())
    return product_name


def get_offer_price_with_class(webpage_android):
    offer_price_classes = (
        "css-901oao r-1wv73ep",
        "css-901oao r-1wv73ep r-1vgyyaa r-1rsjblm",
        "css-901oao r-1wv73ep r-1vgyyaa r-ubezar r-1rsjblm",
        "css-901oao r-1wv73ep r-1w427b9 r-1vgyyaa r-1rsjblm",
    )

    for class_name in offer_price_classes:
        offer_price_list = webpage_android.findAll("div", {"class": class_name})
        if offer_price_list is not None:
            prices = [match.get_text() for match in offer_price_list if match.get_text() is not None]
            prices = [price.strip()[1:].replace(',', '') for price in prices]
            if prices:
                return prices[0]
            return None
    return None


def get_offer_price_with_regex(webpage_android):
    matches = re.findall(
        r'text":"₹[0-9]+,[0-9]+[,]*[0-9]*","textColor":', str(webpage_android)
    )
    prices = [match[8:-14].replace(",", "") for match in matches]
    prices = [int(price) for price in prices if price.isnumeric()]
    if prices:
        return prices[0]
    return None


def get_product_links(url, user_agent=None):
    product_category_sub_page = get_webpage(url, user_agent)
    product_links = re.findall("""http://dl.flipkart.com/dl/.*?(?=")""", str(product_category_sub_page))
    product_links = [links for links in product_links if "pid=" in links]
    return product_links
