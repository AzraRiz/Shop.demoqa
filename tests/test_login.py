from pages.home_page import TestLogin
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

def test_login(driver):
    home_page = TestLogin (driver)
    home_page.test_go_to("https://shop.demoqa.com/")
    home_page.test_dismiss()
    home_page.test_login("Mirjana", "password997!pass") 
    time.sleep(2)
    