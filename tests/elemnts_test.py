from conftest import driver
from pages.elements_page import TextBoxPage

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



