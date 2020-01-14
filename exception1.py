from selenium import webdriver
import time
import math

try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/cats.html")
        button = browser.find_element_by_id("button")
finally:
    # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

