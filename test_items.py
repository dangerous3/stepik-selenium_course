import pytest                                                                                                                                                                                                
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_should_have_addtobasket_button(browser):
    browser.get(link)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket")))
    time.sleep(10)
    assert True
