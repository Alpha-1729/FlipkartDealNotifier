SELECT_PRODUCTS = "SELECT * FROM Product;"

SELECT_PRODUCT_CATEGORIES = "SELECT * FROM ProductCategory;"

SELECT_UNREPORTED_PRODUCTS = "SELECT * FROM Product WHERE is_reported = 0;"

INSERT_PRODUCT = "INSERT INTO Product(product_name, product_url, product_category_id, actual_price, offer_price, is_reported) VALUES (:product_name, :product_url, :product_category_id,  :actual_price, :offer_price, :is_reported);"

INSERT_PRODUCT_CATEGORY = "INSERT OR IGNORE INTO ProductCategory(category_name) VALUES (:category_name);"

UPDATE_REPORTED_PRODUCT = "UPDATE Product SET is_reported = 1 WHERE product_name = :product_name;"

UPDATE_PRODUCT_PRICE = "UPDATE Product SET actual_price = :actual_price, offer_price = :offer_price, is_reported = 0 WHERE product_name = :product_name;"
