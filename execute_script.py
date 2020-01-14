from selenium import webdriver
import time
import math

try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/execute_script.html")
        x_val = browser.find_element_by_id("input_value")
        x = x_val.text
        y = math.log(math.fabs(12 * math.sin(int(x))))
        print(y)
        answer = browser.find_element_by_id("answer")
        browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
        answer.send_keys(str(y))
        option1 = browser.find_element_by_id("robotCheckbox")
        option1.click()
        option2 = browser.find_element_by_id("robotsRule")
        option2.click()
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

finally:
    # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

