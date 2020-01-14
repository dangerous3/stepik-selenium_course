from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
button = browser.find_element_by_id("book")
button.click()

x_val = browser.find_element_by_id("input_value")
x = x_val.text
y = math.log(math.fabs(12 * math.sin(int(x))))
print(y)
answer = browser.find_element_by_id("answer")
answer.send_keys(str(y))
button1 = browser.find_element_by_id("solve")
button1.click()

