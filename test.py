import requests
from bs4 import BeautifulSoup

def get_price_ardes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Use CSS selectors or XPath to extract the price element
        price_element = soup.select_one('#price-tag')  # Adjust this selector
        if price_element:
            price = float(price_element.text.replace('лв', '').replace(',', '.'))
            return price
    return None

def get_price_lowPrice(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Use CSS selectors or XPath to extract the price element
        price_element = soup.select_one('span[itemprop="price"]')
        if price_element:
            price = float(price_element.text.replace('лв', '').replace(',', '.'))
            return price
    return None

product_urls = {
    "Ardes": "https://ardes.bg/product/samsung-galaxy-s23-8gb-128gb-green-sm-s911bzgdeue-310480?utm_source=pazaruvaj.com&utm_medium=%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D0%B8",
    "LowPrice": "https://lowprice.bg/bg/telefoni/samsung-s23-5g-128gb-green",
}

prices = {}

for site, url in product_urls.items():
    if site == "Ardes":
        price = get_price_ardes(url)
    else:
        price = get_price_lowPrice(url)
    if price is not None:
        prices[site] = price
    else:
        prices[site] = float('inf')

if prices["Ardes"] < prices["LowPrice"]:
    cheaper_site = "Ardes"
    cheaper_price = prices["Ardes"]
else:
    cheaper_site = "LowPrice"
    cheaper_price = prices["LowPrice"]

print(f"The site with the lower price is {cheaper_site} with a price of {cheaper_price:.2f} лв.")

for price in prices:
    print(prices[price])
