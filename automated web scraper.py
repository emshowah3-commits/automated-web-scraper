# Import core modules 
import requests
from bs4 import BeautifulSoup
import csv
# Extraction script
url = "https://books.toscrape.com/"
response = requests.get(url)

# Get status code to mark down issue
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

# Loops through each book for title and price
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    # Lists each books title and price
    print("\n"f"{title} - {price}")

with open("books.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        writer.writerow([title, price])