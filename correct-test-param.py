import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    time.sleep(3)
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)
    textarea =  WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "textarea")))
    #textarea = browser.find_element_by_css_selector("textarea")
    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()
    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    result_test = browser.find_element_by_class_name("smart-hints__hint") 
    assert result_test.text == "Correct!", "Incorrect: Test has not been passed"
    

