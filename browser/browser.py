import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait


binarylocation = os.environ.get("BINARY_LOCATION")

print(binarylocation)

options = Options()
options.headless = False
options.binary_location = r"/home/mike/firefox/firefox"
driver = webdriver.Firefox(options=options)
driver.get("https://www.selenium.dev/documentation/webdriver/")

browser_link = driver.find_element_by_link_text("Browser")

WebDriverWait(driver, timeout=3)

browser_link.click()

support_button = driver.find_element_by_class_name("selenium-button-container")

WebDriverWait(driver, timeout=3)

support_button.click()

i = 1
while i < 2:
    driver.refresh()
    WebDriverWait(driver, timeout=10)
