import requests
from bs4 import BeautifulSoup

try:
    url = "https://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page title:", soup.title.string)
except Exception as e:
    print("Something broke during scraping:", e)
