import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_cart(browser):
    alarm = None
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    except NoSuchElementException:
        alarm = 'No add to cart button'

    assert alarm != 'No add to cart button', alarm
