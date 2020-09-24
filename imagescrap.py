import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Nilgiris_district")
soup = bs4.BeautifulSoup(result.text, "lxml")

for index,item in enumerate(soup.select(".thumbimage")):
    image = requests.get("https:" + item['src'])
    f = open("D:\Study\pythonProject\images\image_" + str(index) + ".jpg", 'wb')
    f.write(image.content)
    f.close()
    print(str(index) + " completed")

