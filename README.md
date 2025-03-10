# E-Commerce Product Scraper

A powerful web scraping tool to extract product details (name, price, and rating) from popular e-commerce websites like **Amazon**, **eBay**, **Flipkart**, and **Noon**. The tool supports pagination, error handling, and exporting data to CSV, JSON, or Excel formats.

---

## Features

- **Multi-Website Support**: Scrapes products from Amazon, eBay, Flipkart, and Noon.
- **Pagination**: Scrapes multiple pages of search results.
- **Error Handling**: Handles network errors and missing data gracefully.
- **Export Options**: Saves data in CSV, JSON, or Excel format.
- **Proxy Support**: Uses proxies to avoid IP blocking.
- **Dynamic Input**: Users can specify the website, search query, and number of pages via CLI.

---
pip install -r requirements.txt

--- 
how to use ? 
Arguments
--query: Product to search (e.g., "laptops").

--website: Website to scrape (amazon, ebay, flipkart, noon, or all).

--pages: Number of pages to scrape (default: 1).

--format: Output format (csv, json, or excel).

--output: Output file name (without extension).

usage example  : 
python scraper.py --query "laptops" --website all --pages 3 --format csv --output products

---
Requirements :
Python 3.7+
Libraries: requests, beautifulsoup4, pandas, openpyxl


