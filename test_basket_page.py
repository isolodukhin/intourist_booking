from pages.basket_page import BasketPage
import time
from selenium.common.exceptions import NoSuchElementException


def test_basket_page_booking(browser):
    link = ""
    page = BasketPage(browser)
    page.open(link)
    page.login("", "")
    try:
        page.tariff_checkbox_click()
    except NoSuchElementException:
        pass
    page.scroll()
    page.data_1_tourist()
    try:
        page.data_2_tourist()
    except NoSuchElementException:
        pass
#    page.booking_and_get_number()
    time.sleep(200)



