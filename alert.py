from selenium import webdriver
import time
import math

try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/alert_accept.html")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        alert = browser.switch_to.alert
        alert.accept()
        input_value = browser.find_element_by_id("input_value")
        x = int(input_value.text)
        y = math.log(math.fabs(12*math.sin(x)))
        answer = browser.find_element_by_id("answer")
        answer.send_keys(str(y))
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

finally:
    # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

