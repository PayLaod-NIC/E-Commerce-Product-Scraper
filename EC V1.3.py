import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import argparse
import time
import random

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# User agents and proxies to avoid blocking
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
]

PROXIES = [
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080",
    "http://proxy3.example.com:8080",
]

# Function to get a random user agent
def get_random_user_agent():
    return random.choice(USER_AGENTS)

# Function to get a random proxy
def get_random_proxy():
    return random.choice(PXIES)

# Function to scrape Amazon products
def scrape_amazon(search_query, pages=1):
    base_url = "https://www.amazon.com"
    products = []
    
    for page in range(1, pages + 1):
        logging.info(f"Scraping Amazon page {page}...")
        url = f"{base_url}/s?k={search_query}&page={page}"
        headers = {"User-Agent": get_random_user_agent()}
        proxy = {"http": get_random_proxy(), "https": get_random_proxy()}
        
        try:
            response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            
            for item in soup.find_all("div", class_="s-result-item"):
                try:
                    name = item.find("span", class_="a-text-normal").text.strip()
                    price = item.find("span", class_="a-price-whole").text.strip()
                    rating = item.find("span", class_="a-icon-alt").text.strip()
                    products.append({
                        "Website": "Amazon",
                        "Name": name,
                        "Price": price,
                        "Rating": rating
                    })
                except AttributeError:
                    continue
        except requests.exceptions.RequestException as e:
            logging.error(f"Error scraping Amazon: {e}")
        
        time.sleep(2)  # Delay to avoid blocking
    
    return products

# Function to scrape eBay products
def scrape_ebay(search_query, pages=1):
    base_url = "https://www.ebay.com"
    products = []
    
    for page in range(1, pages + 1):
        logging.info(f"Scraping eBay page {page}...")
        url = f"{base_url}/sch/i.html?_nkw={search_query}&_pgn={page}"
        headers = {"User-Agent": get_random_user_agent()}
        proxy = {"http": get_random_proxy(), "https": get_random_proxy()}
        
        try:
            response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            
            for item in soup.find_all("div", class_="s-item__info"):
                try:
                    name = item.find("h3", class_="s-item__title").text.strip()
                    price = item.find("span", class_="s-item__price").text.strip()
                    rating = item.find("span", class_="s-item__etrs-text").text.strip() if item.find("span", class_="s-item__etrs-text") else "N/A"
                    products.append({
                        "Website": "eBay",
                        "Name": name,
                        "Price": price,
                        "Rating": rating
                    })
                except AttributeError:
                    continue
        except requests.exceptions.RequestException as e:
            logging.error(f"Error scraping eBay: {e}")
        
        time.sleep(2)  # Delay to avoid blocking
    
    return products

# Function to scrape Flipkart products
def scrape_flipkart(search_query, pages=1):
    base_url = "https://www.flipkart.com"
    products = []
    
    for page in range(1, pages + 1):
        logging.info(f"Scraping Flipkart page {page}...")
        url = f"{base_url}/search?q={search_query}&page={page}"
        headers = {"User-Agent": get_random_user_agent()}
        proxy = {"http": get_random_proxy(), "https": get_random_proxy()}
        
        try:
            response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            
            for item in soup.find_all("div", class_="_1AtVbE"):
                try:
                    name = item.find("div", class_="_4rR01T").text.strip()
                    price = item.find("div", class_="_30jeq3").text.strip()
                    rating = item.find("div", class_="_3LWZlK").text.strip() if item.find("div", class_="_3LWZlK") else "N/A"
                    products.append({
                        "Website": "Flipkart",
                        "Name": name,
                        "Price": price,
                        "Rating": rating
                    })
                except AttributeError:
                    continue
        except requests.exceptions.RequestException as e:
            logging.error(f"Error scraping Flipkart: {e}")
        
        time.sleep(2)  # Delay to avoid blocking
    
    return products

# Function to scrape Noon products
def scrape_noon(search_query, pages=1):
    base_url = "https://www.noon.com"
    products = []
    
    for page in range(1, pages + 1):
        logging.info(f"Scraping Noon page {page}...")
        url = f"{base_url}/uae-en/search?q={search_query}&page={page}"
        headers = {"User-Agent": get_random_user_agent()}
        proxy = {"http": get_random_proxy(), "https": get_random_proxy()}
        
        try:
            response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            
            for item in soup.find_all("div", class_="productContainer"):
                try:
                    name = item.find("div", class_="name").text.strip()
                    price = item.find("span", class_="currency").text.strip() + item.find("span", class_="value").text.strip()
                    rating = item.find("span", class_="rating").text.strip() if item.find("span", class_="rating") else "N/A"
                    products.append({
                        "Website": "Noon",
                        "Name": name,
                        "Price": price,
                        "Rating": rating
                    })
                except AttributeError:
                    continue
        except requests.exceptions.RequestException as e:
            logging.error(f"Error scraping Noon: {e}")
        
        time.sleep(2)  # Delay to avoid blocking
    
    return products

# Function to save data to CSV, JSON, or Excel
def save_data(data, filename="products", format="csv"):
    df = pd.DataFrame(data)
    
    if format == "csv":
        df.to_csv(f"{filename}.csv", index=False)
        logging.info(f"Data saved to {filename}.csv")
    elif format == "json":
        df.to_json(f"{filename}.json", orient="records", lines=True)
        logging.info(f"Data saved to {filename}.json")
    elif format == "excel":
        df.to_excel(f"{filename}.xlsx", index=False)
        logging.info(f"Data saved to {filename}.xlsx")
    else:
        logging.error("Invalid format. Supported formats: csv, json, excel")

# Main function
def main():
    parser = argparse.ArgumentParser(description="E-Commerce Product Scraper")
    parser.add_argument("--query", required=True, help="Product search query")
    parser.add_argument("--website", choices=["amazon", "ebay", "flipkart", "noon", "all"], default="all", help="Website to scrape")
    parser.add_argument("--pages", type=int, default=1, help="Number of pages to scrape")
    parser.add_argument("--format", choices=["csv", "json", "excel"], default="csv", help="Output file format")
    parser.add_argument("--output", default="products", help="Output file name (without extension)")
    args = parser.parse_args()
    
    products = []
    
    if args.website == "amazon" or args.website == "all":
        products.extend(scrape_amazon(args.query, args.pages))
    if args.website == "ebay" or args.website == "all":
        products.extend(scrape_ebay(args.query, args.pages))
    if args.website == "flipkart" or args.website == "all":
        products.extend(scrape_flipkart(args.query, args.pages))
    if args.website == "noon" or args.website == "all":
        products.extend(scrape_noon(args.query, args.pages))
    
    if products:
        save_data(products, args.output, args.format)
    else:
        logging.warning("No products found.")

if __name__ == "__main__":
    main()