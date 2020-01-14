from selenium import webdriver
import time
import unittest

class UniqueSelectors(unittest.TestCase):
    def test_unique_sel(self):
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            firstname = browser.find_element_by_xpath("//input[@class='form-control first' and @required='']")
            firstname.send_keys("Ivan")
            lastname = browser.find_element_by_xpath("//input[@class='form-control second' and @required='']")
            lastname.send_keys("Petrov")
            email = browser.find_element_by_xpath("//input[@class='form-control third' and @required='']")
            email.send_keys("ivan.petrov@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "You have not been registered")

    def test_unique_sel2_fail(self):
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            firstname = browser.find_element_by_xpath("//input[@class='form-control first' and @required='']")
            firstname.send_keys("Ivan")
            lastname = browser.find_element_by_xpath("//input[@class='form-control second' and @required='']")
            lastname.send_keys("Petrov")
            email = browser.find_element_by_xpath("//input[@class='form-control third' and @required='']")
            email.send_keys("ivan.petrov@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "You have not been registered")

if __name__ == "__main__":
    unittest.main()


