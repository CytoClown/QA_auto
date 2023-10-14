import time

from conftest import driver
from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cut_addr, output_perm_addr = text_box_page.check_filled_form()
            assert full_name == output_name, 'Name does not match'
            assert email == output_email, 'Email does not match'
            assert current_address == output_cut_addr, 'Current does not match'
            assert permanent_address == output_perm_addr, 'Permanent does not match'

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            # input_checkbox_new = []
            # output_result_new = []
            # for i in input_checkbox:
            #    a = i.replace(' ', '')
            #    a = a.replace('.doc', '')
            #    input_checkbox_new.append(a.lower())
            # for i in output_result:
            #    output_result_new.append(i.lower())
            # time.sleep(3)
            # print(input_checkbox_new)
            # print(output_result_new)
            # assert output_result_new == input_checkbox_new
            assert input_checkbox == output_result, 'checkboxes have not been selected'


