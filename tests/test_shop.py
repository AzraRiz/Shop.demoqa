from pages.home_page import TestShop
from multiprocessing.connection import wait
from multiprocessing.sharedctypes import Value
import time
from turtle import clear
from xml.dom.minidom import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_shop(driver):
    home_page = TestShop (driver)
    home_page.test_go_to("https://shop.demoqa.com/")
    home_page.test_filter_product("dress")
    assert home_page.test_verify_error() == "No products were found matching your selection."
    home_page.test_add_to_cart("dress")
    home_page.test_your_cart_text()
    assert home_page.test_your_cart_text() == "CART"
    home_page.test_item_name_text("//*[@id='post-6']/div/div/form/table/tbody/tr[1]/td[2]/a")
    assert home_page.test_item_name_text("//*[@id='post-6']/div/div/form/table/tbody/tr[1]/td[2]/a") == "WHITE BANDAGE CUT OUT BODYCON MINI DRESS - WHITE"
    home_page.test_checkout_page()
    home_page.test_checkout_page_text()
    assert home_page.test_checkout_page_text() == "CHECKOUT"
    time.sleep(5)
    