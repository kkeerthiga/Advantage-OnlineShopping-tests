import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import logging

from conftest import LOGIN_URL
from pages.loginpage import LoginPage
from pages.categorypage import Category
from pages.cartpage import CartPage

USERNAME= "Tester"
PASSWORD = "Test@123"

test_logger= logging.getLogger("Test_AdvantageDemo")

def test_AdvantageDemo_login(browser: WebDriver | WebDriver):
    
    loginpage= LoginPage(browser)
    loginpage.login(USERNAME,PASSWORD)
    test_logger.info("Logged in Successfully")
    logged_in_user = loginpage.is_user_logged_in()
    assert logged_in_user == USERNAME,f"Login Failed : Expected :{USERNAME} but got {logged_in_user}" 
    
    loginpage.log_out()
    test_logger.info("Logged out successfully")
    assert browser.current_url == LOGIN_URL,f"Logout Test Failed: Expected url {LOGIN_URL} but got {browser.current_url} "  


@pytest.mark.parametrize("category_name",["SPEAKERS", "TABLETS","LAPTOPS","MICE","HEADPHONES"])  
def test_category_selection(browser,category_name):
    
    loginpage = LoginPage(browser)
    categorypage = Category(browser)
    
    loginpage.login(USERNAME,PASSWORD)
    heading_text = categorypage.select_category(category_name)
    test_logger.info(f"Redirecting to {category_name}")
    assert category_name.capitalize() in browser.current_url,f"Category page not redirected correctly"
    categorypage.add_items_to_cart('HP ElitePad 1000 G2 Tablet')
    
def test_add_items_to_cart(browser):
    
    loginpage = LoginPage(browser)
    categorypage = Category(browser)
    cartpage = CartPage(browser)
        
    loginpage.login(USERNAME,PASSWORD)
    categorypage.add_items_to_cart('TABLETS','HP Pro Tablet 608 G1')
    cartpage.click_on_cart_icon()
    cartpage.is_on_shopping_cart_page()
    cartpage.get_cart_item()
    cartpage.get_cart_items_with_quantity()
