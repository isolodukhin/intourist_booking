from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LoginPageLocators
from pages.locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def scroll_to(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView()", element)

    def login(self, login, password):
        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id=\"mat-input-0\"]")))
        self.browser.find_element(*LoginPageLocators.LOGIN).send_keys(login)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_CONFIRM).click()

