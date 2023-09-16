import pyperclip
import urllib.parse

filter_url = input("Enter filter url: ")
category_name = input("Enter the category name: ")

# Remove all unwanted character from the url.
new_url = urllib.parse.unquote_plus(filter_url)
while new_url != filter_url:
    filter_url = new_url
    new_url = urllib.parse.unquote_plus(new_url)

filter_dic = {}
filters = filter_url.split("&p[]=")[1:]
for group in filters:
    category, value = group.split("=")
    if category in filter_dic.keys():
        filter_dic[category] += ", " + '"' + value + '"'
    else:
        filter_dic[category] = '"' + value + '"'

# Generating the json content.
content = ""
for key, value in filter_dic.items():
    content += "\t\t" + '"&p[]=' + key + '=" : [' + value + "],"

output = """"{}":{{
        "search?q=" : "{}",
        "&as-show=" : "on",
        "&as=" : "off",
        "&sort=" : "price_asc",
        {}
        \t}}""".format(
    category_name.title(), category_name.lower(), content[:-1]
)

pyperclip.copy(output)
print("Json entry has been copied to clipboard")
