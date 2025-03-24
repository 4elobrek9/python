from bs4 import BeautifulSoup
import requests
response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")
print("Title:", soup.title.text)