import pytest
import chromedriver_autoinstaller
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()