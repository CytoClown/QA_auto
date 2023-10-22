import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# service=ChromeService(ChromeDriverManager().install())
# --start-maximized
# chrome_options.add_argument('--window-size=1500, 900')
# options = ChromeOptions()
# options.add_argument("--start-maximized")
# driver = ChromeDriver(options)