import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()


class Page:
    """Class to create a page object given a url"""

    def __init__(self, url: str):
        self._url = url
        binary_location = os.environ.get("BINARY_LOCATION")

        options = Options()
        options.headless = False
        options.binary_location = fr"{binary_location}"
        self._driver = webdriver.Firefox(options=options)
        self._driver.get(f"{self._url}")


class SeleniumPage(Page):
    def doSomeClickingAndRefreshing(self):

        browser_link = self._driver.find_element_by_link_text("Browser")
        WebDriverWait(self._driver, timeout=3)

        browser_link.click()
        support_button = self._driver.find_element_by_class_name(
            "selenium-button-container"
        )
        WebDriverWait(self._driver, timeout=3)

        support_button.click()

        i = 1
        while i < 4:
            self._driver.refresh()
            WebDriverWait(self._driver, timeout=10)
            i += 1


class WikipediaPage(Page):
    def biographySearch(self, personName: str) -> object:
        """Searches a person on Wikipedia, chooses the first option
        from the drop-down suggestion menu, and jumps to the biography
        section"""

        search_box = self._driver.find_element(by="name", value="search")
        search_box.send_keys(f"{personName}")

        WebDriverWait(self._driver, timeout=5)

        ActionChains(self._driver).key_down(Keys.CONTROL).send_keys(
            Keys.RETURN
        ).perform()
        new_page = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, "toc"))
        )

        required_link = new_page.find_element(by="partial link text", value="Biography")
        required_link.click()


def refactored_selenium_website():

    page = SeleniumPage("https://www.selenium.dev/documentation/webdriver/")
    page.doSomeClickingAndRefreshing()


def refactored_wikipedia_famous_people_biography(searchText: str):

    page = WikipediaPage("https://www.wikipedia.org/")
    page.biographySearch(f"{searchText}")


def main():

    refactored_selenium_website()
    refactored_wikipedia_famous_people_biography("Ada Lovelace")


if __name__ == "__main__":
    main()
