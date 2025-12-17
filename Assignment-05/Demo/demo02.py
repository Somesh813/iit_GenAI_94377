from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://duckduckgo.com/")
print("Initial Page Title:",driver.title)
driver.implicitly_wait(5)
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("dkte collage ichalkaranji")
search_box.send_keys(Keys.RETURN)
print("Later page Title:",driver.title)
time.sleep(5)
driver.quit()