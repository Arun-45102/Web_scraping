import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Nilgiris_district")
soup = bs4.BeautifulSoup(result.text, "lxml")

for item in soup.select(".mw-headline"):
    print(item.getText())
