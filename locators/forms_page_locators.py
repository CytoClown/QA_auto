import random

from selenium.webdriver.common.by import By


class FormsPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.CSS_SELECTOR, f'label[for="gender-radio-{random.randint(1,3)}"]')
    MOBILE_NUMBER = (By.CSS_SELECTOR, '#userNumber')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, '#dateOfBirthInput')
    SUBJECTS = (By.CSS_SELECTOR, '#subjectsInput')
    HOBBIES = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="hobbies-checkbox-{random.randint(1,3)}"]')
    UPLOAD_FILE = (By.CSS_SELECTOR, '#uploadPicture')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')
    WIDGET = (By.CSS_SELECTOR, 'div:nth-of-type(4) > .group-header > .header-wrapper')
    REGISTRATION_RESULT = (By.XPATH, "//body/div[@role='dialog']/div[@role='document']/div[@class='modal-content']//table//td[2]")





