from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN = (By.XPATH, "//input[@id=\"mat-input-0\"]")
    PASSWORD = (By.XPATH, "//input[@id=\"mat-input-1\"]")
    BTN_CONFIRM = (By.XPATH, "//button/span[text()='Войти']")


class BasketPageLocators:
    TARIFF_CHECKBOX = (By.XPATH, '//mat-checkbox[@id="mat-checkbox-2"]')

    DOCUMENT_TYPE_1 = (By.XPATH, "//*[text()=\"Не выбрано\"]")
    ZAGRAN_PASSPORT_1 = (By.XPATH, "//span[text()=' Загран паспорт РФ ']")
    PASSPORT_SER_1 = (By.XPATH, "//input[@formcontrolname='personalDocumentSeries']")
    PASSPORT_NUM_1 = (By.XPATH, "//input[@formcontrolname='personalDocumentNumber']")
    PASSPORT_DATE_1 = (By.XPATH, "//input[@formcontrolname='personalDocumentValidTill']")
    LAST_NAME_1 = (By.XPATH, "//input[@formcontrolname='lastName']")
    FIRST_NAME_1 = (By.XPATH, "//input[@formcontrolname='firstName']")
    BIRTHDAY_1 = (By.XPATH, "//input[@formcontrolname='birthDate']")
    GENDER_BUT_1 = (By.XPATH, "//*[@formcontrolname='genderType']")
    FEMALE_1 = (By.XPATH, "//span[text()='Ж']")
    PHONE_1 = (By.XPATH, "//input[@formcontrolname='phoneNumber']")

    TOURIST2_DOCUMENT_TYPE_1 = (By.XPATH, "//div[@class ='tourist-form tourist-form-1 ng-untouched ng-pristine ng-invalid ng-star-inserted']//*[text()=\"Не выбрано\"]")
    TOURIST2_ZAGRAN_PASSPORT_1 = (By.XPATH, "//span[text()=' Загран паспорт РФ ']")
    TOURIST2_PASSPORT_SER_1 = (By.XPATH, "//div[@class ='tourist-form tourist-form-1 ng-invalid ng-star-inserted ng-touched ng-dirty']//input[@formcontrolname='personalDocumentSeries']")
    TOURIST2_PASSPORT_NUM_1 = (By.XPATH, "//div[@class ='tourist-form tourist-form-1 ng-invalid ng-star-inserted ng-touched ng-dirty']//input[@formcontrolname='personalDocumentNumber']")
    TOURIST2_PASSPORT_DATE_1 = (By.XPATH, "//div[@class ='tourist-form tourist-form-1 ng-invalid ng-star-inserted ng-touched ng-dirty']//input[@formcontrolname='personalDocumentValidTill']")
    TOURIST2_LAST_NAME_1 = (By.XPATH, "//div[@class ='tourist-form tourist-form-1 ng-invalid ng-star-inserted ng-touched ng-dirty']//input[@formcontrolname='lastName']")
    TOURIST2_FIRST_NAME_1 = (By.XPATH, "//div[@class ='tourist-form tourist-form-1 ng-invalid ng-star-inserted ng-touched ng-dirty']//input[@formcontrolname='firstName']")
    TOURIST2_BIRTHDAY_1 = (By.XPATH, "//div[@class ='tourist-form tourist-form-1 ng-invalid ng-star-inserted ng-touched ng-dirty']//input[@formcontrolname='birthDate']")
    TOURIST2_GENDER_BUT_1 = (By.XPATH, "//div[@class ='tourist-form tourist-form-1 ng-invalid ng-star-inserted ng-touched ng-dirty']//*[@formcontrolname='genderType']")
    TOURIST2_FEMALE_1 = (By.XPATH, "//span[text()='Ж']")

    BOOKING_BTN = (By.XPATH, "//*[text()=' Забронировать ']")
    TOUR_OK_BUTTON = (By.XPATH, "//mat-dialog-container/div[2]/button/span")
    TOUR_NUMBER = (By.XPATH, "//td[1]/table/tbody/tr[4]/td[2]")






