from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os

from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")


product_links = []
a = 1
for i in range(1,10):
    url = 'https://tiki.vn/laptop/c8095?page=' + str(i)
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.get(url)
    sleep(10)
    #Get Link
    links = browser.find_elements_by_class_name("product-item")
    for link in links:
        z = link.get_attribute("href")
        product_links.append(z)
        a = a+1
    browser.close()
print("\n.....Đã crawl",a - 1,"link..........\n")

textfile = open("tiki.txt", "w")
for element in product_links:
    textfile.write(element + "\n")
textfile.close()