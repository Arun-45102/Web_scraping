from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver/chromedriver")
driver.get("https://webscraper.io/test-sites/e-commerce/allinone")
final_products = []
click_event = driver.find_element_by_link_text("Computers")
click_event.click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Laptops"))
    )
    element.click()
    soup = BeautifulSoup(driver.page_source, "lxml")
    products = soup.select(".thumbnail")
    print(len(products))
    for product in products:
        if product.find("p", {'data-rating': '1'}):
            get_title = product.select(".title")
            for title in get_title:
                final_products.append(title.text)
finally:
    driver.quit()
print(len(final_products))
print(final_products)
