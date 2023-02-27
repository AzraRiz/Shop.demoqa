from pages.home_page import TestRegister
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

def test_register(driver):
    home_page = TestRegister (driver)
    home_page.test_go_to("https://shop.demoqa.com/")
    home_page.test_dismiss()
    home_page.test_register("Emilija", "testiranje@email.com", "password997!pass")
    assert home_page.test_myaccount_text() == "MY ACCOUNT"
    time.sleep(2)
    