import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.basepage import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('AAAAA')
        self.element_is_visible(self.locators.EMAIL).send_keys('aaa@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('ffffffff')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('dddddddd')
        self.element_is_visible(self.locators.SUBMIT).click()
