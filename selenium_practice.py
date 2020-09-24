from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome("chromedriver/chromedriver")
browser.get("https://www.python.org/")
page = BeautifulSoup(browser.page_source, "html5lib")
links = page.select('a')
for link in links:
    print(link)
browser.close()
