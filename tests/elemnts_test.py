import time
from pages.basepage import BasePage
from conftest import driver
from pages.elements_page import TextBoxPage

# def test(driver):
#     page = BasePage(driver, 'https://demoqa.com/text-box')
#     page.open()
#     time.sleep(3)

class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            time.sleep(5)


