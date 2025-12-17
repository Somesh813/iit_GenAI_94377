from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://nilesh-g.github.io/learn-web/HTML/demo08.html")
print("Page Title:",driver.title)
driver.implicitly_wait(5)
list_items=driver.find_elements(By.TAG_NAME,"li")
for item in list_items:
    print("List Item:",item.text)

driver.quit()    