from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

url = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Vlad")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Khmarenko")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Vileyka")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Belarus")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

finally:
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла