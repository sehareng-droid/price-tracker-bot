#Project Idea: Real-Time Product Price Tracker
#🎯 Goal:

#Create a bot that automatically scrapes product prices 
#(e.g., laptops, phones, or books) from an online store
#(like Amazon, Daraz, or a demo site), stores them in SQLite, and exports to Excel.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import time

# Step 1: Open browser
driver = webdriver.Chrome()
driver.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops/")

# Step 2: Create an explicit wait (max 10 seconds)
wait = WebDriverWait(driver, 10)
all_products=[]
today = datetime.now().strftime("%Y-%m-%d")


while True:
# Step 3: Wait for product to appear
    products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".thumbnail")))

    
    for q in products:
        text = q.find_element(By.CSS_SELECTOR,"h4 a").get_attribute("title")
        price = q.find_element(By.CSS_SELECTOR,"span[itemprop='price']").text
        description =q.find_element(By.CSS_SELECTOR,"p.description").text
        link = q.find_element(By.CSS_SELECTOR, "h4 a").get_attribute("href")

        all_products.append({"text": text,
                             "price":price,
                             "description":description,
                             "link":link,
                             "date":today})
        
        print(f"Title: {text} | Price: {price} | description: {description} | link:{link} today:{today}")

    try:
        page = driver.find_element(By.CSS_SELECTOR,".next a")
        page.click()
        time.sleep(2)  
    except:
        print("no more pages")
        break
#Convert to DataFrame (panda)
df = pd.DataFrame(all_products, columns=["text", "price", "description","link","date"])


#remove duplicates
df=df.drop_duplicates()


#handle missing data
df["price"]=df["price"].fillna(0)
df["text"]=df["text"].fillna("unknown")
df["description"]=df["description"].fillna("unknown")
df["link"]=df["link"].fillna("unknown")

#change price string to integer
df["price"] = df["price"].str.replace("$", "").astype(float)
import sqlite3

conn = sqlite3.connect("laptops.db")
df.to_sql("products", conn, if_exists="replace", index=False)

df.to_excel("products.xlsx", index=False)

df = pd.read_sql_query("SELECT * FROM products;", conn)
print(df.head())

# total products
df = print(pd.read_sql_query("SELECT count(*) as total_products FROM products;", conn))

#most expensive
df = print(pd.read_sql_query("SELECT text as expensive, price FROM products ORDER BY price DESC LIMIT 1;", conn))

#most cheepest
df = print(pd.read_sql_query("SELECT text as cheepest, price FROM products ORDER BY price ASC LIMIT 1;", conn))

#filters products from price range ($500 to $1000)
df = print(pd.read_sql_query("SELECT text as range, price FROM products WHERE PRICE BETWEEN 500 AND 1000;", conn))

#find all products with hp in title
df = print(pd.read_sql_query("SELECT text as title FROM products WHERE text LIKE '%HP%';", conn))


#Average price
df = print(pd.read_sql_query("SELECT AVG(price) as Average_Price FROM products;", conn))

#expensive laptops
df = print(pd.read_sql_query("SELECT text as expensive, price FROM products ORDER BY price DESC LIMIT 5;", conn))

#cheepest laptops
df = print(pd.read_sql_query("SELECT text as cheepest, price FROM products ORDER BY price ASC LIMIT 5;", conn))

conn.close()





           

driver.quit()