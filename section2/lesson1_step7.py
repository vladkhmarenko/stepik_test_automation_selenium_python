from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

url = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element(By.CSS_SELECTOR, 'img').get_attribute('valuex')
    y = calc(x)
    
    answer_element = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_element.send_keys(y)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    robot_checkbox.click()

    robot_radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robot_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button')
    submit_button.click()

finally:
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла