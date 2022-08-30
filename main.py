from lib2to3.pgen2 import driver
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://www.dios.se/bostader/sundsvall/"

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('./chromedriver') 
driver.get(URL)

# this is just to ensure that the page is loaded
time.sleep(5) 

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

apartment_list = soup.find_all("li", class_="objectsearchlisting__item")
print(apartment_list)