from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasePage:
    
    CART_ICON= (By.ID,"menuCart")
    SEARCH_ICON = (By.ID, "menuSearch")
    CART_URL ="https://www.advantageonlineshopping.com/#/shoppingCart"
    
    
    def __init__(self,driver):
        self.driver = driver
        self.wait= WebDriverWait(self.driver,10)
        self.logger = logging.getLogger("Automate_onlineshopping.BasePage")
    
    def get_current_url(self):
        """Returns the current URL of the page."""
        self.logger.debug(f"Getting Current URL : {self.driver.current_url} ")
        return self.driver.current_url
    
    def click_on_cart_icon(self):
        """Clicks the cart icon and waits until the cart page is loaded."""
        cart_icon = self.wait.until(EC.element_to_be_clickable(self.CART_ICON))
        cart_icon.click()
        self.wait.until(EC.url_to_be(self.CART_URL))
        self.logger.info("cart icon clicked") 
        