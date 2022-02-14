import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = Options()
options.headless = False
options.binary_location = r"/home/mike/firefox/firefox"
driver = webdriver.Firefox(options=options)


def selenium_website():
    """Some basic clicking on the selenium website"""

    driver.get("https://www.selenium.dev/documentation/webdriver/")

    browser_link = driver.find_element_by_link_text("Browser")

    WebDriverWait(driver, timeout=3)

    browser_link.click()

    support_button = driver.find_element_by_class_name("selenium-button-container")

    WebDriverWait(driver, timeout=3)

    support_button.click()

    i = 1
    while i < 4:
        driver.refresh()
        WebDriverWait(driver, timeout=10)
        i = i + 1


def wikipedia_famous_people_biography(searchText: str):
    """Searches a person on Wikipedia, chooses the first option
    from the drop-down suggestion menu, and jumps to the biography
    section"""

    driver.get("https://www.wikipedia.org/")
    search_box = driver.find_element(by="name", value="search")
    search_box.send_keys(f"{searchText}")

    WebDriverWait(driver, timeout=5)

    ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.RETURN).perform()

    # Once the table of contents has loaded, we're on the new page
    new_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "toc"))
    )

    ## Loop to iterate over all links and find the one we want

    # find all the hyperlink elements on the page
    # links_on_page = new_page.find_elements(by="css selector", value="a")

    # for link in links_on_page:
    #     if "Biography" in link.text:
    #         link.click()

    ## Find the link directly and action rather than looping
    required_link = new_page.find_element(by="partial link text", value="Biography")
    required_link.click()


def main():
    selenium_website()
    wikipedia_famous_people_biography("John Donne")


if __name__ == "__main__":
    main()
