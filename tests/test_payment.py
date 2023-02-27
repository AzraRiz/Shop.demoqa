from pages.home_page import TestPayment
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

def test_payment(driver):
    home_page = TestPayment (driver)
    home_page.test_go_to("https://shop.demoqa.com/")
    home_page.test_buy_item()
    home_page.test_billing_information("Emilija", "Nepoznato", "Nikole Tesle 57", "Sarajevo", "71000", "061235467", "test97@email.com")  
    home_page.test_terms()
    home_page.test_place_order()
    home_page.test_order()
    assert home_page.test_order() == "Thank you. Your order has been received."
    time.sleep(5)
    