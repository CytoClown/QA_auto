import random
import time

import allure

from conftest import driver
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage

@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cut_addr, output_perm_addr = text_box_page.check_filled_form()
            assert full_name == output_name, 'Name does not match'
            assert email == output_email, 'Email does not match'
            assert current_address == output_cut_addr, 'Current does not match'
            assert permanent_address == output_perm_addr, 'Permanent does not match'

    @allure.feature("Check CheckBox")
    class TestCheckBox:
        @allure.title("Check CheckBox")
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

    @allure.feature("Check RadioButton")
    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', 'Yes have not been selected'
            assert output_impressive == 'Impressive', 'Impressive have been selected'
            assert output_no == 'No', 'No have not been selected'
            time.sleep(5)

        @allure.title("Check RadioButton")
        def test_radiobutton(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            output_result = radio_button_page.click_radiobutton_row()
            assert output_result == ['Yes', 'Impressive', 'No'], 'Radiobutton have not been selected'

    @allure.feature("Check WebTable")
    class TestWebTable:
        @allure.title("Check AddPerson")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            person_list = web_table_page.check_new_added_person()
            assert new_person in person_list

        @allure.title("Check SearchPerson")
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0,5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, 'The person was not found in the table'

        @allure.title("Check UpdatePerson")
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, 'The persson card was not changed'

        @allure.title("Check DeletePerson")
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        @allure.title("Check ChangeCountRaw")
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 25, 50, 100], 'The number of rows in the table has not been changed'

    @allure.feature("Check ButtonPage")
    class TestButtonPage:
        @allure.title("Check ClickOnTheButton")
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click', 'Double click button was not pressed'
            assert right == 'You have done a right click', 'Right click button was not pressed'
            assert click == 'You have done a dynamic click', 'Dynamic click button was not pressed'

        @allure.title("Check ButtonsClick")
        def test_buttons_click(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.double_click_on_button()
            right = button_page.right_click_on_button()
            click = button_page.click_on_button()
            assert double == 'You have done a double click', 'Double click button was not pressed'
            assert right == 'You have done a right click', 'Right click button was not pressed'
            assert click == 'You have done a dynamic click', 'Dynamic click button was not pressed'

    @allure.feature("Check LinkPage")
    class TestLinksPage:

        @allure.title("Check CheckLink")
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, 'Invalid response code, this link is incorrect'

        @allure.title("Check LinkRaiseOfStatus")
        def test_link_raise_for_status(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_simple_link()
            assert href_link == current_url, 'Invalid response code, this link is incorrect'

        @allure.title("Check BrokenLink")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, 'Invalid response code'

        @allure.title("Check CreatedLink")
        def test_created_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_created_status_code('https://demoqa.com/created')
            assert response_code == 201, 'Invalid response code'

        @allure.title("Check NoConnectLink")
        def test_no_content_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_no_content_status_code('https://demoqa.com/no-content')
            assert response_code == 204, 'Invalid response code'

        @allure.title("Check NotFoundLink")
        def test_not_found_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_not_found_status_code('https://demoqa.com/invalid-url')
            time.sleep(2)
            assert response_code == 404, 'Invalid response code'

    @allure.feature("Check UploadDownloadPage")
    class TestUploadDownloadPage:
        @allure.title("Check UploadFile")
        def test_upload_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, 'File has not been uploaded'

        @allure.title("Check DownloadFile")
        def test_download_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, 'File has not been downloaded'

    @allure.feature("Check DynamicPropertiesPage")
    class TestDynamicPropertiesPage:

        @allure.title("Check DynamicProperties")
        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            before, after = dynamic_properties_page.check_changed_of_color()
            assert before != after, 'Color has not been changed'

        @allure.title("Check AppearButton")
        def test_check_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            button = dynamic_properties_page.check_appear_button().text
            assert button == 'Visible After 5 Seconds', 'Button is unavailable'

        @allure.title("Check ButtonIsClickable")
        def test_check_button_is_clickable(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            button = dynamic_properties_page.check_button_is_clickable()
            assert button == True, 'Button is not clickable'
