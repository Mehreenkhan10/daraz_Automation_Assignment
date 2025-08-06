from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def is_free_shipping(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "delivery-fee"))
            )
            shipping_info = self.driver.find_element(By.CLASS_NAME, "delivery-fee").text
            return "free" in shipping_info.lower()
        except:
            return False