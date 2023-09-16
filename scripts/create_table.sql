-- Open the sql lite db using sql-db-browser.
-- Run the below script to create all tables.

DROP TABLE IF EXISTS ProductCategory;
DROP TABLE IF EXISTS Product;

CREATE TABLE 'ProductCategory'
(
	'product_category_id'	INTEGER NOT NULL UNIQUE,
	'category_name' TEXT NOT NULL,
	PRIMARY KEY('product_category_id' AUTOINCREMENT),
	UNIQUE(category_name)
);

CREATE TABLE 'Product' 
(
	'product_id'	INTEGER NOT NULL UNIQUE,
	'product_name'	TEXT,
	'product_url'	TEXT,
	'product_category_id'	INTEGER NOT NULL,
	'actual_price'	REAL,
	'offer_price'	REAL,
	'is_reported'	INTEGER DEFAULT 0,
	PRIMARY KEY('product_id' AUTOINCREMENT)
);