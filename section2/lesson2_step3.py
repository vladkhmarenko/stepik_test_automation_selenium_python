from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x1 = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    x2 = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    sum = str(x1 + x2)

    browser.find_element(By.CSS_SELECTOR, 'select#dropdown').click()
    browser.find_element(By.CSS_SELECTOR, f'option[value="{sum}"]').click()
    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла