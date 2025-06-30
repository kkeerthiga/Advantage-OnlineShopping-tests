import logging.handlers
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import os
import datetime
import logging


LOGIN_URL ="https://www.advantageonlineshopping.com/#/"


logger = logging.getLogger("Automate_OnlineShopping")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(name)s -%(levelname)s - %(message)s ")
console_Handler = logging.StreamHandler()
console_Handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(console_Handler)


def pytest_addoption(parser):
        parser.addoption (
            "--browser" ,  action = "store" , default= "chrome" , help= "browser to run test on chrome or edge"
        )
    
@pytest.fixture(scope="function")
def browser(request):
    
    browser_name = request.config.getoption("--browser").lower()
    driver =None
    
    logger.info(f"Setting up {browser_name} for test") 
    
    if browser_name=="chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        logger.info("Chrome browser opened for test")
    elif browser_name =="Edge":
        service =EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        logger.info("Edge browser opened for tests")
    else:
        pytest.fail("unsupported browser:{browser_name}. Use Chrome or Edge")
        
    driver.maximize_window()
    driver.get(LOGIN_URL)
    
    yield driver               
    
    