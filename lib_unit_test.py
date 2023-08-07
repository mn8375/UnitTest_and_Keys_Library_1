import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

print(f'........................ Libraria unit test ....... 10 iuilie 2023......................')


class TestLoghin(unittest.TestCase):
    # vom defini niste constante care sa ajute in crearea testelor
    USERNAME = 'tomsmith'
    PASSWORD = 'SuperSecretPassword!'
    WRONG_PASSWORD = '!QAZ'
    WRONG_USERNAME = 'URUB'
    # vom defini selectorii de care avem nevoie pt crearea testelor care ne vor ajuta sa fie constanti ,
    # vom observa cum o putem face
    USERNAME_SELECTOR = (By.ID, 'username')
    PASSWORD_SELECTOR = (By.ID, 'password')
    LOGIN_SLECTOR = (By.XPATH, '//button')
    EROARE_SELECTOR = (By.ID, 'flash')
    LOGOUT_SELECTOR = (By.CSS_SELECTOR, 'i[class="icon-2x icon-signout"]')

    def setUp(self):  # aceste prime 2 metode se vor implementa la inceperea fiecarui test
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/login')
        # self.driver.maximize_window()
        # time.sleep(2)

    def tearDown(self) -> None:
        # time.sleep(1)
        self.driver.quit()

    def test_verificare_parola_incorecta(self):
        # vrem sa probam accesul cu o parola gresita

        # un exemplu de wait explicit
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'username')))

        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.USERNAME)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.WRONG_PASSWORD)
        self.driver.find_element(*self.LOGIN_SLECTOR).click()
        # time.sleep(2)
        # assert self.driver.find_element(*self.EROARE_SELECTOR).text == 'Your password is invalid!'

        # Tema va recomand sa printam la selector.text() si sa urmarim raspunsul
        #assert self.driver.find_element(*self.EROARE_SELECTOR).get_attribute('class') == 'flash error'
        print(f'folosim selector_text{self.driver.find_element(*self.EROARE_SELECTOR).text}')
        assert (self.driver.find_element(*self.EROARE_SELECTOR).get_attribute('class') == 'flash error')

        # verificare user incorect

    @unittest.skip  # decorator
    def test_verificare_user_incorect(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.WRONG_USERNAME)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.PASSWORD)
        self.driver.find_element(*self.LOGIN_SLECTOR).click()
        # time.sleep(2)
        assert self.driver.find_element(*self.EROARE_SELECTOR).get_attribute('class') == 'flash error'
        # Tema verificati ca cu un username gresit primi eroarea:  'Your username is invalid!'

        # vericam login corect

    def test_login_corect(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.USERNAME)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.PASSWORD)
        self.driver.find_element(*self.LOGIN_SLECTOR).click()
        print(self.driver.find_element(*self.LOGOUT_SELECTOR).get_attribute('class'))
        assert 'icon-signout' in self.driver.find_element(*self.LOGOUT_SELECTOR).get_attribute('class')
        # time.sleep(4)

    # Temma folositi Waituri instructiunile sunt in curs

