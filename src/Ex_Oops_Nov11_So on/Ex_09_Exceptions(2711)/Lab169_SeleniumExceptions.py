from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


try:

    driver = webdriver.Chrome()
    driver.get("http://example.com")
    driver.maximize_window()
    driver.find_element("id", "no button exists")
except NoSuchElementException as nse:
    print("element not found", nse.msg)

