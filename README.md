# 🔰 Flipkart Deal Notifier
- Flipkart Deal Notifier is a Python script that sends notification to the user whenever there is a decrease in the price of a product on Flipkart. It parses the product's webpage using BeautifulSoup library, compares the current price with the previously recorded price, and notifies the user accordingly. The user can run the script on their local machine or deploy it on a cloud service like AWS Lambda. The project is open-source and contributions are welcome.
- It helps to notify the best deals for your customized category of products in flipkart.

#### ➡ Prerequisites
- [DB Browser for SQLite](https://sqlitebrowser.org/)
- [Python 3.9.0](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)
- [URL Decoder/Encoder](https://meyerweb.com/eric/tools/dencoder/)

#### ➡ Configurations
- Open `utils/constants/config.py` and update the full file-path of the `sqlite db` and `json` file.
- Open `db/products.db` using `Db Browser for SQLite` and run the `scripts/create_table.sql` script against the db.
- Add `TELEGRAM_BOT_KEY` and `TELEGRAM_CHAT_ID` in the environment variables.
- How to add entry in `config/config.json`.
    - Search for a product in flipkart.
    - Apply all the required filter.
    - Copy the url from the browser.
    - Run `tools/url_to_json_converter.py`.
    - Json entry will be copied to clipboard.
    - Open `config/config.json` and paste the json content from the clipboard at the end of the json file.

#### ➡ Usage
```bash
python main.py
```

#### ➡ Disclaimer
- This repository is provided as-is without any warranty or guarantee of reliability, suitability or accuracy of its contents. The author is not responsible for any damage or negative consequences arising from the use or distribution of the information herein. Users assume full responsibility for any actions taken based on the materials provided in this repository. The author reserves the right to modify or remove any content from the repository without notice. By accessing or using this repository, users agree to indemnify and hold harmless the author from any claims or liabilities arising from their use.
