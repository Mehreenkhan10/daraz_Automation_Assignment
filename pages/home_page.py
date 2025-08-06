from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.daraz.pk/")

    def search_item(self, item):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(item)
        search_box.submit()