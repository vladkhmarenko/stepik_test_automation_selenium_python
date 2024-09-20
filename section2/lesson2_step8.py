
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

url = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Name')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Surname')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('email@email.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла