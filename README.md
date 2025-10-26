# 🛒 Real-Time Product Price Tracker (Python + Selenium + SQLite + Excel)

## 🎯 Project Goal
A Python-based automation bot that automatically collects **product prices** (like laptops, phones, or books) from online stores and stores them in a **SQLite database** with date tracking for real-time price monitoring.

## ⚙️ Technologies Used
- Python  
- Selenium (for web scraping)  
- Pandas (for data cleaning)  
- SQLite (for local database storage)  
- Excel (for export and reporting)

## 🚀 Key Features
✅ Automated web scraping using Selenium  
✅ Real-time price tracking with date  
✅ Data storage in SQLite  
✅ Export to Excel  
✅ SQL queries for analysis (average, highest, lowest prices)

## 📊 Example SQL Queries
```sql
-- Total products
SELECT COUNT(*) AS total_products FROM products;

-- Most expensive product
SELECT text, price FROM products ORDER BY price DESC LIMIT 1;

-- Cheapest product
SELECT text, price FROM products ORDER BY price ASC LIMIT 1;

-- Filter products in price range $500 - $1000
SELECT text, price FROM products WHERE price BETWEEN 500 AND 1000;

Output Files

laptops.db → SQLite database

products.xlsx → Excel report
