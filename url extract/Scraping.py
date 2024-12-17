import requests
from requests import Session
from bs4 import BeautifulSoup
import json

def get_soup(url: str, headers: dict[str:str], session: Session, page_number: int):
    """
    Simple function to execute get request, parse html and return Beautifulsoup object.

    : param url: str: String containing URL to get.
    : param headers: dict: Dict containing User agent specification for the get request.
    : param session: requests.Session(): Requests Session() object.
    : param page_number: int: Integer representing which page number is being contacted.

    : return: Beautifulsoup object containing parsed html.
    """
    response = session.get(url, headers= headers)

    return BeautifulSoup(response.text, 'html.parser')

def get_url_list(page_number: int,
                  headers: dict[str:str] = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',} ,
                  session: Session = requests.Session()) -> list[str]:
    """
    Function receives a page number from ImmoWeb search results to contact, returns URLs for listings on page.

    : param page_number: int: Page number in search results to scrape.
    : param headers: (optional, dict): Dict containing user agent specifications for get request.
    : param session: (optional, requests.Session()): Requests Session() object to use.

    : returns: list: List of real estate listings from ImmoWeb search.
    """

    url_list = []

    base_url = f'https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={page_number}&orderBy=relevance'

    soup = get_soup(base_url, headers, session, page_number)

    # Extract the listing URLs by finding all <a> elements with the relevant class (adjust class as needed)
    url_list = soup.find_all('a', href='card__title-link ')
    print(url_list)
    # Change this class based on actual HTML structure

    return url_list

dic_page_urls = {}
for page in range(1,334):
    key_name = F"Page {page}"
    page_urls = get_url_list(page)
    dic_page_urls[key_name] = page_urls
    print(dic_page_urls)
    print(F"DONE {page} pages")

urls_list = [url for values in dic_page_urls.values() for url in values]

'''
url_list = []
for values in dic_page_urls.values():
    for value in values:
        print(value)
        url_list.append(value)
print(type(url_list))'''

# Save the URLs to a JSON file
with open("url_list.json", "w") as f:
    json.dump(urls_list, f)