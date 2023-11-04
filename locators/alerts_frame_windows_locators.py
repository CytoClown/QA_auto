from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, '#tabButton')
    NEW_WINDOW = (By.CSS_SELECTOR, '#windowButton')
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, '#messageWindowButton')
    SAMPLE_HEADING = (By.CSS_SELECTOR, '#sampleHeading')

class AlertWindowPageLocators:
    BUTTON_ALERT = (By.CSS_SELECTOR, '#alertButton')
    BUTTON_AFTER_5_SECONDS_ALERT = (By.CSS_SELECTOR, '#timerAlertButton')
    CONFIRM_BOX_ALERT = (By.CSS_SELECTOR, '#confirmButton')
    PROMPT_BOX_ALERT = (By.CSS_SELECTOR, '#promtButton')
    CONFIRM_RESULTS = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    TEXT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')
