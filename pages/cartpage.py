from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
import logging

class CartPage(BasePage):
    
    CART_ICON = (By.ID,"menuCart")
    CART_ITEMS=(By.XPATH,"//label[contains(@class, 'productName')]")
    CART_ITEM_ROWS = (By.XPATH, "//tbody//tr[@class='ng-scope']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.wait =WebDriverWait(driver,10)
        self.logger = logging.getLogger("Automate_onlineshopping.CartPage")
        

    def is_on_shopping_cart_page(self):
        
        current_url =self.get_current_url()
        self.click_on_cart_icon()
        cart_page = self.get_current_url()
        assert cart_page == BasePage.CART_URL , f"Redirecting to Cart failed: expected URL{BasePage.CART_URL} but got {cart_page}"
        self.logger.info("Redirected to cart page")
    
    def get_cart_item(self):
        self.logger.info("Retrieving all cart item names.")
        Item_names_in_cart = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEMS))
        return [element.text for element in Item_names_in_cart]   
    '''
    def get_cart_items_with_quantity(self):
        self.logger.info(f"Getting quantity for items in cart.")
        item_rows = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM_ROWS))
        
        cart_items = []
       
        for row in item_rows:
           cart_item_names = row.find_element(By.XPATH,".//label[contains(@class, 'productName')]")
           item_names = cart_item_names.text.strip()
           self.logger.info(f"total items in cart are: {len(item_names)}") 
           print(row.get_attribute("outerHTML")) 
           cart_item_quantity = row.find_element(By.XPATH,".//td[contains(@class, 'quantityMobile')]/label[@class='ng-binding']")
           #cart_item_quantity =row.find_element(By.XPATH,".//td/a/label[contains(text(), 'QTY:')]")
           item_quantity = cart_item_quantity.text.strip()
           cart_items.append((item_names,item_quantity))
    
        return cart_items    
        '''
    def get_cart_items_with_quantity(self):
        self.logger.info("Getting quantity for items in cart.")
        item_rows = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM_ROWS))
        self.logger.info(f"Number of item rows found: {len(item_rows)}")
        
        cart_items = []
        
        for index, row in enumerate(item_rows):
            html = row.get_attribute("outerHTML")
            print(f"Row {index} outerHTML:\n{html}\n")
            
            # Try to find the product name label
            try:
                cart_item_names = row.find_element(By.XPATH, ".//label[contains(@class, 'productName')]")
                item_names = cart_item_names.text.strip()
            except Exception as e:
                print(f"Could not find productName label in row {index}: {e}")
                continue
            
            # Try to find quantity label
            try:
                cart_item_quantity = row.find_element(By.XPATH, ".//td[contains(@class, 'quantityMobile')]/label[@class='ng-binding']")
                item_quantity = cart_item_quantity.text.strip()
            except Exception as e:
                print(f"Could not find quantity label in row {index}: {e}")
                item_quantity = "N/A"
            
            cart_items.append((item_names, item_quantity))
        
        return cart_items    