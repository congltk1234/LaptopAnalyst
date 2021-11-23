from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.chrome.options import Options

# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
product_links = []
a = 1
# Crawl sản phẩm trong 20 trang đầu tiên
for i in range(1,20):
    url = 'https://www.lazada.vn/laptop/?page=' + str(i)
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.get(url)
    #Get Link
    sleep(30)  # Nghỉ 30s để tránh bị chặn API 
    links = browser.find_elements_by_xpath('//*[@class="RfADt"]/a')  # Vị trí chứa đường dẫn sản phẩm
    for link in links:
        z = link.get_attribute("href")   # Lấy đường dẫn và thêm vào list
        product_links.append(z)
        a = a+1
    browser.close()
print("\n.....Đã crawl",a - 1,"link..........\n")

# Lưu lại đường dẫn các sản phẩm sau khi crawl được
textfile = open("data/lazada_link.txt", "w")
for element in product_links:
    textfile.write(element + "\n")
textfile.close()