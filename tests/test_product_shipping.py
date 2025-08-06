from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage

def test_free_shipping_check(driver):
    home = HomePage(driver)
    home.load()
    home.search_item("electronics")

    results = SearchResultsPage(driver)
    results.apply_brand_filter()
    try:
        results.set_price_filter("500", "5000")
        results.click_first_product()
        driver.switch_to.window(driver.window_handles[-1])

        product = ProductPage(driver)
        assert product.is_free_shipping(), "Free shipping not available"
    except Exception as e:
        driver.save_screenshot("failed_shipping_check.png")
        raise e