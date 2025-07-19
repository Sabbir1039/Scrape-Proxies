# FreeProxy.World Scraper

This repository contains a dataset of HTTPS, highly anonymous proxies scraped from [freeproxy.world](https://www.freeproxy.world).

---

## 🧰 Purpose

This project is intended for **learning and testing purposes** only. It demonstrates:

- Scrapy-based web scraping of proxy lists  
- Proxy data extraction and basic pagination  
- How to store data for later reuse

**Not recommended for production use.** Free proxies are often slow, unreliable, and potentially insecure.

---

## 📦 Files

- `proxies.txt` — Contains lines of `http://<ip>:<port>`, suitable for Scrapy proxy-rotation tools.  
- `scrape_proxies/` — Scrapy project that scrapes the proxy list.  
- `.gitignore` — Ensures local environment files (like `scrape_venv/`) are not committed.

---

## ⚠️ Legal & Ethical Disclaimer

- All scraped data comes from `freeproxy.world`, which provides public proxy lists free of registration.  
- Use of this data is at your own risk.  
  - Free proxies may intercept or manipulate traffic 
- Scraping is permitted for public data, but dev should still respect website terms, robots.txt, and applicable laws.

---

## 🚀 Usage

1. Clone the repo and install dependencies:
    ```bash
    git clone <repo_url>
    cd scrape_proxies
    python3 -m venv ../scrape_venv
    source ../scrape_venv/bin/activate
    pip install -r requirements.txt
    ```
2. Run the Scrapy spider:
    ```bash
    scrapy crawl proxies -o scraped_proxies.json
    ```
3. *proxies.txt* is ready to be used with proxy-rotation middlewares like *scrapy-rotating-proxies*.

## 🎯 For Developers
Use this as a foundation to experiment with:
- Proxy rotation
- Free vs. paid proxy services
- Legality, ethics, and best scraping practices
