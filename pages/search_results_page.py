from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def apply_brand_filter(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ant-checkbox"))
        )
        brand_checkbox = self.driver.find_elements(By.CLASS_NAME, "ant-checkbox")[0]
        self.driver.execute_script("arguments[0].click();", brand_checkbox)

    def set_price_filter(self, min_price, max_price):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Min']"))
        )
        min_in = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Min']")
        max_in = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Max']")
        min_in.clear()
        min_in.send_keys(min_price)
        max_in.clear()
        max_in.send_keys(max_price)
        self.driver.find_element(By.CSS_SELECTOR, "button.ant-btn-icon-only").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "info--ifj7U"))
        )

    def get_product_count(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "info--ifj7U"))
        )
        return len(self.driver.find_elements(By.CLASS_NAME, "info--ifj7U"))

    def click_first_product(self):
        product = self.driver.find_elements(By.CLASS_NAME, "info--ifj7U")[0]
        product.click()