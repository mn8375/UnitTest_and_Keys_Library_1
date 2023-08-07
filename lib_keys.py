import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

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
    CONTEXT_SELECTOR = (By.ID, 'hot-spot')

    #Selector pentru alerte JS
    JS_ALERT_SELECTOR = (By.CSS_SELECTOR, 'button[onclick = "jsAlert()"]')
    MESSAGE_SELECTOR = (By.ID,'result')
    CONFIRM_SELECTOR = (By.CSS_SELECTOR, 'button[onclick = "jsConfirm()"]')
    PROMPT_SELECTOR = (By.CSS_SELECTOR, 'button[onclick = "jsPrompt()"]')

    def setUp(self):  # aceste prime 2 metode se vor implementa la inceperea fiecarui test
        #self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Edge()

        #self.driver.get('https://the-internet.herokuapp.com/login')
        #self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')
        self.driver.get('https://the-internet.herokuapp.com/context_menu')
        # self.driver.maximize_window()
        # time.sleep(2)

    def tearDown(self) -> None:
        # time.sleep(1)
        self.driver.quit()

#Vom trimite un test random in campurile de user si parola, il vom selecta,
    # il vom sterge si apoi vom trimite user si parola corecte folosind libraria Keys

    @unittest.skip
    def test_valid_after_invalid(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys('abcd')
        time.sleep(2)
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.USERNAME)
        time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys('1234')
        time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.PASSWORD,Keys.ENTER)
        time.sleep(2)
        #self.driver.find_element(*self.LOGIN_SLECTOR).click()
        time.sleep(2)

    @unittest.skip
    def test_js_alert(self):
        #CSS_SELECTOR  button[onclick = "jsAlert()"]
        self.driver.find_element(*self.JS_ALERT_SELECTOR).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        #Facem un assert pe elementul Result comparandu-l cu textul
        assert self.driver.find_element(*self.MESSAGE_SELECTOR).text == 'You successfully clicked an alert'

    @unittest.skip
    def test_js_cancel(self):
        self.driver.find_element(*self.CONFIRM_SELECTOR).click()
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()
        time.sleep(2)
        assert self.driver.find_element(*self.MESSAGE_SELECTOR).text == 'You clicked: Cancel'

    @unittest.skip
    def test_js_prompt(self):
        self.driver.find_element(*self.PROMPT_SELECTOR).click()
        time.sleep(2)
        text = 'Asa trebuie sa ruleze pagina'
        self.driver.switch_to.alert.send_keys(text)
        self.driver.switch_to.alert.accept()
        self.assertEqual(self.driver.find_element(*self.MESSAGE_SELECTOR).text, f'You entered: {text}')

    def test_alert_from_contextmenu(self):
        ac = ActionChains(self.driver)
        #Construim selectorul pentru zona in care vom face click dreapta
        element = self.driver.find_element(*self.CONTEXT_SELECTOR)
        time.sleep(2)
        ac.context_click(element).perform()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    



