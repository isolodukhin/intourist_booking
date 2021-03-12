from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class BasketPage(BasePage):

    def tariff_checkbox_click(self):
        WebDriverWait(self.browser, 1).until(
            EC.invisibility_of_element_located((By.XPATH, "div[@inlinesvg='assets/loader-plane.svg']")))
        self.browser.find_element(*BasketPageLocators.TARIFF_CHECKBOX).click()

    def scroll(self):
        doc_type = self.browser.find_element(By.XPATH, "//*[text()=\"Не выбрано\"]")
        self.scroll_to(doc_type)

    def data_1_tourist(self):
        self.browser.find_element(*BasketPageLocators.DOCUMENT_TYPE_1).click()
        self.browser.find_element(*BasketPageLocators.ZAGRAN_PASSPORT_1).click()
        self.browser.find_element(*BasketPageLocators.PASSPORT_DATE_1)\
            .send_keys(random.choice(["10.12.2022", "11.12.2022", "01.03.2023", "04.05.2023", "11.07.2025",
                                      "11.08.2023", "17.10.2023", "01.01.2025", "13.02.2022", "19.12.2023",
                                      "01.04.2022", "02.04.2023", "03.04.2023", "04.04.2023", "05.04.2024",
                                      "06.04.2023", "07.04.2023", "08.04.2023"]))
        self.browser.find_element(*BasketPageLocators.LAST_NAME_1).\
            send_keys(random.choice(["Popova", "Petrova", "Pupkina", "Leonova", "Sergeeva", "Loskova", "Trofimova", "Rakova", "Bochkova",
                                     "Minenko", "Suslova", "Medvedeva", "Kuznetsova", "Lebedeva", "Victorova",
                                     "Ptushkina", "Varlamova", "Solodova", "Malkova"]))
        self.browser.find_element(*BasketPageLocators.FIRST_NAME_1)\
            .send_keys(random.choice(["Alena", "Yana", "Anna", "Alina", "Olga", "Irina", "Elena", "Evelina", "Olesya",
                                      "Julia", "Varvara", "Polina", "Lidia", "Maria", "Marina", "Antonina", "Ekaterina",
                                      "Inna", "Victoria", "Vladlena"]))
        self.browser.find_element(*BasketPageLocators.BIRTHDAY_1)\
            .send_keys(random.choice(["10.12.1991", "11.12.1992", "01.03.1993", "04.05.1993", "11.07.1990",
                                      "11.08.1997", "17.10.1993", "21.01.1995", "13.02.1998", "19.12.1993",
                                      "01.03.1989", "01.03.1988", "01.03.1987", "11.03.1986", "01.03.1985",
                                      "01.03.1984", "04.03.1983", "01.03.1982", "01.03.1981"]))
        self.browser.find_element(*BasketPageLocators.PASSPORT_SER_1).send_keys(random.randint(10, 98))
        WebDriverWait(self.browser, 1).until(
            EC.invisibility_of_element_located((By.XPATH, "div[@inlinesvg='assets/loader-plane.svg']")))
        self.browser.find_element(*BasketPageLocators.PASSPORT_NUM_1).send_keys(random.randint(2012030, 9876543))
        self.browser.find_element(*BasketPageLocators.GENDER_BUT_1).click()
        self.browser.find_element(*BasketPageLocators.FEMALE_1).click()
        WebDriverWait(self.browser, 1).until(
            EC.invisibility_of_element_located((By.XPATH, "div[@inlinesvg='assets/loader-plane.svg']")))
        self.browser.find_element(*BasketPageLocators.PHONE_1).send_keys(random.randint(79001020123, 79969802030))

    def data_2_tourist(self):
        self.browser.find_element(*BasketPageLocators.TOURIST2_DOCUMENT_TYPE_1).click()
        self.browser.find_element(*BasketPageLocators.TOURIST2_ZAGRAN_PASSPORT_1).click()
        self.browser.find_element(*BasketPageLocators.TOURIST2_PASSPORT_DATE_1) \
            .send_keys(random.choice(["10.12.2022", "11.12.2022", "01.03.2023", "04.05.2023", "11.07.2025",
                                      "11.08.2023", "17.10.2023", "01.01.2025", "13.02.2022", "19.12.2023",
                                      "01.04.2022", "02.04.2023", "03.04.2023", "04.04.2023", "05.04.2024",
                                      "06.04.2023", "07.04.2023", "08.04.2023"]))
        self.browser.find_element(*BasketPageLocators.TOURIST2_LAST_NAME_1). \
            send_keys(random.choice(["Popova", "Petrova", "Pupkina", "Leonova", "Sergeeva", "Loskova", "Trofimova", "Rakova", "Bochkova",
                                     "Minenko", "Suslova", "Medvedeva", "Kuznetsova", "Lebedeva", "Victorova",
                                     "Ptushkina", "Varlamova", "Solodova", "Malkova"]))
        self.browser.find_element(*BasketPageLocators.TOURIST2_FIRST_NAME_1) \
            .send_keys(random.choice(["Alena", "Yana", "Anna", "Alina", "Olga", "Irina", "Elena", "Evelina", "Olesya",
                                      "Julia", "Varvara", "Polina", "Lidia", "Maria", "Marina", "Antonina", "Ekaterina",
                                      "Inna", "Victoria", "Vladlena"]))
        self.browser.find_element(*BasketPageLocators.TOURIST2_BIRTHDAY_1) \
            .send_keys(random.choice(["10.12.1991", "11.12.1992", "01.03.1993", "04.05.1993", "11.07.1990",
                                      "11.08.1997", "17.10.1993", "21.01.1995", "13.02.1998", "19.12.1993",
                                      "01.03.1989", "01.03.1988", "01.03.1987", "11.03.1986", "01.03.1985",
                                      "01.03.1984", "04.03.1983", "01.03.1982", "01.03.1981"]))
        self.browser.find_element(*BasketPageLocators.TOURIST2_PASSPORT_SER_1).send_keys(random.randint(10, 98))
        WebDriverWait(self.browser, 1).until(
            EC.invisibility_of_element_located((By.XPATH, "div[@inlinesvg='assets/loader-plane.svg']")))
        self.browser.find_element(*BasketPageLocators.TOURIST2_PASSPORT_NUM_1).send_keys(random.randint(2012030, 9876543))
        self.browser.find_element(*BasketPageLocators.TOURIST2_GENDER_BUT_1).click()
        self.browser.find_elements(*BasketPageLocators.TOURIST2_FEMALE_1).pop(1).click()
        WebDriverWait(self.browser, 1).until(
            EC.invisibility_of_element_located((By.XPATH, "div[@inlinesvg='assets/loader-plane.svg']")))

    def booking_and_get_number(self):
        self.browser.find_element(*BasketPageLocators.BOOKING_BTN).click()
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//mat-dialog-container/div[2]/button/span")))
        self.browser.find_element(*BasketPageLocators.TOUR_OK_BUTTON).click()
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//td[1]/table/tbody/tr[4]/td[2]")))
        print(self.browser.find_element(*BasketPageLocators.TOUR_OK_BUTTON).gettext())




