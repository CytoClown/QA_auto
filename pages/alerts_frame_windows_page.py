import time

from generator.generator import generated_text
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertWindowPageLocators
from pages.basepage import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        text = self.element_is_present(self.locators.SAMPLE_HEADING).text
        url = self.driver.current_url
        return text, url


    def new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        window_name = self.driver.window_handles[1]
        self.driver.switch_to.window(window_name)
        text = self.element_is_present(self.locators.SAMPLE_HEADING).text
        url = self.driver.current_url
        return text, url

class AlertWindowPage(BasePage):
    locators = AlertWindowPageLocators()
    def button_alert(self):
        self.element_is_visible(self.locators.BUTTON_ALERT).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def button_alert_after_5_seconds(self):
        self.element_is_visible(self.locators.BUTTON_AFTER_5_SECONDS_ALERT).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def confirm_box_alert_ok(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        alert.accept()
        text = self.element_is_present(self.locators.CONFIRM_RESULTS).text
        return text

    def confirm_box_alert_cancel(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        text = self.element_is_present(self.locators.CONFIRM_RESULTS).text
        return text

    def prompt_box_alert(self):
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT).click()
        self.alert_is_present()
        alert = self.driver.switch_to.alert
        text_input = generated_text()
        alert.send_keys(text_input)
        alert.accept()
        text_result = self.element_is_present(self.locators.TEXT_RESULT).text
        return text_input, text_result.split(' ')[2]









