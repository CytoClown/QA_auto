import os
import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file, generated_subject
from locators.forms_page_locators import FormsPageLocators
from pages.basepage import BasePage


class FormPage(BasePage):

    locators = FormsPageLocators()

    def registration_form(self):
        person_info = next(generated_person())
        firstname = person_info.firstname
        lastname = person_info.lastname
        email = person_info.email
        phone = person_info.phone_number
        subjects = generated_subject()
        file_name, path = generated_file()
        address = person_info.current_address
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(phone)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(subjects)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.go_to_element(self.element_is_present(self.locators.HOBBIES))
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(address)
        self.element_is_visible(self.locators.WIDGET).click()
        time.sleep(1)
        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person_info

    def result_list(self):
        elements = self.element_are_present(self.locators.REGISTRATION_RESULT)
        data = []
        for item in elements:
            self.go_to_element(item)
            data.append(item.text)
        return data
