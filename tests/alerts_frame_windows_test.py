import time
from conftest import driver
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertWindowPage


class TestAlertsFrameWindowsPage:

    class TestBrowserWindowsPage:
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            result, url = browser_windows_page.new_tab()
            assert result == 'This is a sample page', 'Text is wrong'
            assert url == driver.current_url, 'New tab has not been opened'

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            result, url = browser_windows_page.new_window()
            assert result == 'This is a sample page', 'Text is wrong'
            assert url == driver.current_url, 'New window has not been opened'

    class TestAlertsPage:

        def test_button_alert(self, driver):
            alert_window_page = AlertWindowPage(driver, 'https://demoqa.com/alerts')
            alert_window_page.open()
            result = alert_window_page.button_alert()
            assert result == 'You clicked a button', 'Alert has not been appeared'

        def test_button_alert_after_5_seconds(self, driver):
            alert_window_page = AlertWindowPage(driver, 'https://demoqa.com/alerts')
            alert_window_page.open()
            result = alert_window_page.button_alert_after_5_seconds()
            assert result == 'This alert appeared after 5 seconds', 'Alert has not been appeared after five seconds'

        def test_confirm_box_alert_cancel(self, driver):
            alert_window_page = AlertWindowPage(driver, 'https://demoqa.com/alerts')
            alert_window_page.open()
            result = alert_window_page.confirm_box_alert_cancel()
            assert result == 'You selected Cancel', 'You selected OK'

        def test_confirm_box_alert_ok(self, driver):
            alert_window_page = AlertWindowPage(driver, 'https://demoqa.com/alerts')
            alert_window_page.open()
            result = alert_window_page.confirm_box_alert_ok()
            assert result == 'You selected Ok', 'You selected CANCEL'

        def test_prompt_box_alert(self, driver):
            alert_window_page = AlertWindowPage(driver, 'https://demoqa.com/alerts')
            alert_window_page.open()
            input_text, result = alert_window_page.prompt_box_alert()
            assert input_text == result, 'Result text is not equal to expected'

