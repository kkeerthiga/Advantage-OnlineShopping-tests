from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
import logging
import time


class LoginPage(BasePage):
    """Page object for the login functionality of Advantage Online Shopping."""
    
    USERMENU= (By.ID, "menuUser")
    USERNAME_ELEMENT = (By.XPATH, "//input[@name='username']")
    PASSWORD_ELEMENT = (By.XPATH,"//input[@name='password']")
    SIGN_IN_BUTTON_ELEMENT = (By.ID,"sign_in_btn")
    #LOGGED_IN_USER = (By.XPATH,"//span[contains(text(),'Tester')]")
    LOGGED_IN_USER=(By.XPATH,"//*[@id='menuUserLink']/span")
    LOADER = (By.CSS_SELECTOR, "div.loader")
    SIGN_OUT_ELEMENT = (By.XPATH,"//label[contains(@class, 'option roboto-medium ng-scope') and contains(text(), 'Sign out')]")
    
    def __init__(self,driver):
        super().__init__(driver)
        self.wait =WebDriverWait(driver,10)
        self.logger = logging.getLogger("Automate_onlineshopping.Loginpage")
        
    def click_usermenu(self):
        """Click the user menu icon to open the login popup."""
        usermenu= self.wait.until(EC.element_to_be_clickable(self.USERMENU))
        usermenu.click()
    
        
    def enter_username(self,username):
        """Enter the given username."""
        username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_ELEMENT))
        username_field.send_keys(username)
    
    def enter_password(self,password):
        """Enter the given password."""
        password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_ELEMENT))
        password_field.send_keys(password)    
    
    def click_Sign_in_button(self):
        """Click the sign-in button to log in."""
        #self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        sign_in_button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON_ELEMENT))
        sign_in_button.click()       
        
    def login(self, username, password):
        """Perform full login using username and password."""
        self.click_usermenu()
        self.enter_username(username)    
        self.enter_password(password)
        self.click_Sign_in_button()
        
    def is_user_logged_in(self):
         """Return the text of the logged-in user's name (if visible)."""
         userProfile_element= self.wait.until(EC.visibility_of_element_located(self.LOGGED_IN_USER))
         time.sleep(3)
         text = userProfile_element.text.strip()
         self.logger.info(f"Logged in user text: '{text}'")
         return text
         
    def log_out(self):
        """Click sign-out from the user menu."""
        self.click_usermenu()
        signout_link = self.wait.until(EC.element_to_be_clickable(self.SIGN_OUT_ELEMENT))
        signout_link.click()
               