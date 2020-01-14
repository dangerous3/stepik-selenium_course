from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try:
		browser = webdriver.Chrome()
		browser.get("http://suninjuly.github.io/selects2.html")
		num1 = browser.find_element_by_id("num1")
		num2 = browser.find_element_by_id("num2")
		a = int(num1.text)
		b = int(num2.text)
		sum = a + b
		select = Select(browser.find_element_by_tag_name("select"))
		select.select_by_value(str(sum))
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()
