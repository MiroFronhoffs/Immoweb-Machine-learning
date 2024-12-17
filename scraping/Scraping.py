import requests
import re
from bs4 import BeautifulSoup
import json

url = "https://www.immoweb.be/en/classified/house/for-sale/borgerhout/2140/20359920"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",}

req = requests.get(url, headers=headers)

print(req.status_code)

content = req.content
soup = BeautifulSoup(content, 'html.parser')

with open("html.txt", "w", encoding="utf-8") as f:
    f.write(str(soup))

variables = soup.find("script", {"class": "list-item"})

print(variables)
