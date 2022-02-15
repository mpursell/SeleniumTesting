import pytest
from browser.browser import Page

def test_Page():
    
    #Arrange
    test_url = "https://start.duckduckgo.com"

    #Act
    page = Page(test_url)

    #Assert
    assert page._url == "https://start.duckduckgo.com"
