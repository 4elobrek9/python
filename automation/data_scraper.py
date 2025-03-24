import requests
from bs4 import BeautifulSoup
response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")
print("Title:", soup.title.text)