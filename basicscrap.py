import requests
import bs4

result = requests.get("http://www.example.com")
soup = bs4.BeautifulSoup(result.text, "lxml")
get_title = soup.select('title')[0].getText()
print(get_title)
for item in soup.select('p'):
    print(item.getText())
