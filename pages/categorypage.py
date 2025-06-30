from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
import logging

class Category(BasePage):
    
    CATEGORIES = ["SPEAKERS", "TABLETS","LAPTOPS","MICE","HEADPHONES"]

    SPEAKERS_LINK = (By.ID,"speakersTxt") 
    #TABLET_LINK = (By.ID,"tabletsTxt")
    TABLET_LINK =(By.XPATH,"//span[text()='TABLETS']")
    LAPTOPS_LINK = (By.ID,"laptopsTxt")
    MICE_LINK= (By.ID,"miceTxt")
    HEADPHONES_LINK=(By.ID,"headphonesTxt")
    SPEAKERS_HEADING =(By.XPATH,"//h3[contains(text(), 'SPEAKERS')]")
    TABLET_HEADING =(By.XPATH,"//h3[contains(text() , 'TABLETS')]")
    LAPTOPS_HEADING =(By.XPATH,"//h3[contains(text() , 'LAPTOPS')]")
    MICE_HEADING = (By.XPATH,"//h3[contains(text() , 'MICE')]")
    HEADPHONES_HEADING = (By.XPATH,"//h3[contains(text() , 'HEADPHONES')]")
    
    ADD_TO_CART = (By.XPATH,"//button[@name='save_to_cart']")
    
    
    
    def __init__(self, driver):
        super().__init__(driver)
        self.wait =WebDriverWait(driver,10)
    
    def select_category(self,category_name):
        self.logger.info(f"Selecting category '{category_name}' and waiting for heading")
        if category_name =="SPEAKERS":
           element = self.wait.until(EC.element_to_be_clickable(self.SPEAKERS_LINK)) 
           heading= self.SPEAKERS_HEADING
        elif category_name =="TABLETS":
            element = self.wait.until(EC.element_to_be_clickable(self.TABLET_LINK))
            heading = self.TABLET_HEADING
        elif category_name == "LAPTOPS":
            element = self.wait.until(EC.element_to_be_clickable(self.LAPTOPS_LINK))
            heading = self.LAPTOPS_HEADING
        elif category_name == "MICE":
            element = self.wait.until(EC.element_to_be_clickable(self.MICE_LINK))
            heading = self.MICE_HEADING
        elif category_name == "HEADPHONES":
            element = self.wait.until(EC.element_to_be_clickable(self.HEADPHONES_LINK))
            heading = self.HEADPHONES_HEADING        
        else:
            raise ValueError(f"Category {category_name} not supported")  
        
        self.driver.execute_script("arguments[0].click();", element)
        element.click()                   
        page_title =self.wait.until(EC.visibility_of_element_located(heading))
        title= page_title.text
        return title
    
    def add_items_to_cart(self ,category_name,item_name):
        item_category = self.select_category(category_name)
        ITEM_LOCATOR =(By.XPATH,f"//a[text()='{item_name}']")
        item_element =self.wait.until(EC.element_to_be_clickable(ITEM_LOCATOR))
        item_element.click()  
        self.logger.info(f"{item_name}added to cart")