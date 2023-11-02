import time

from pages.forms_page import FormPage
from conftest import driver


class TestRegistrationForm:
    def test_registration_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        data_input = form_page.registration_form()
        data_result = form_page.result_list()
        assert data_input.firstname+' '+data_input.lastname+' '+data_input.email == ' '.join(data_result[:2])