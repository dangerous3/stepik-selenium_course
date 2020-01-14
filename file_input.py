from selenium import webdriver
import os
import time

try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/file_input.html")
        firstname = browser.find_element_by_name("firstname")
        firstname.send_keys("Ivan")
        lastname = browser.find_element_by_name("lastname")
        lastname.send_keys("Petrov")
        email = browser.find_element_by_name("email")
        email.send_keys("Ivan.Petrov@mail.ru")
        upload_file = browser.find_element_by_id("file")
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test.txt')
        upload_file.send_keys(file_path)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

finally:
    # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

