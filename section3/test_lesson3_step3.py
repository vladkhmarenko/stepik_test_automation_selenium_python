from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_page1():
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
    email = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
    first_name.send_keys('Name')
    last_name.send_keys('Surname')
    email.send_keys('mail@gmail.com')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    
    assert welcome_text == "Congratulations! You have successfully registered!", f"Expected 'Congratulations! You have successfully registered!', got {welcome_text}"

    time.sleep(5)
    browser.quit()

        
def test_page2():
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
    email = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
    first_name.send_keys('Name')
    last_name.send_keys('Surname')
    email.send_keys('mail@gmail.com')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    
    assert welcome_text == "Congratulations! You have successfully registered!", f"Expected 'Congratulations! You have successfully registered!', got {welcome_text}"

    time.sleep(5)
    browser.quit()
        