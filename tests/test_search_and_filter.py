from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def test_search_filter_product_count(driver):
    home = HomePage(driver)
    home.load()
    home.search_item("electronics")

    results = SearchResultsPage(driver)
    results.apply_brand_filter()
    try:
        results.set_price_filter("500", "5000")
        count = results.get_product_count()
        assert count > 0, "No products found in results"
    except Exception as e:
        driver.save_screenshot("failed_search_filter.png")
        raise e