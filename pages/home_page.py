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

# S1 Open the application in a web browser and create an account using valid data.
class TestRegister:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    def test_go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window() 
# Dismiss pop-up message
    def test_dismiss (self):
        dismiss_link = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-store-notice__dismiss-link")))
        dismiss_link.click()
        myaccount_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='noo-site']/header/div[1]/div/ul[2]/li[2]/a")))
        myaccount_button.click() 
# Fill register form using data from test_register.py 
    def test_register(self, username, email, password):
        self.wait 
        self.driver.execute_script("window.scrollTo(0, 500);")
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "reg_username")))
        username_field.click()
        username_field.clear()
        username_field.send_keys(username)
        email_field = self.wait.until(EC.element_to_be_clickable((By.ID, "reg_email")))
        email_field.click()
        email_field.clear()
        email_field.send_keys(email)
        self.driver.execute_script("window.scrollTo(0, 500);")
        password_field = self.wait.until(EC.element_to_be_clickable((By.ID, "reg_password")))
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)
        self.driver.execute_script("window.scrollTo(0, 500);")
        register_button = self.driver.find_element(By.XPATH, "//*[@id='customer_login']/div[2]/form/p[4]/button")
        register_button.click() 
# Verify My Account page - register successful 
    def test_myaccount_text(self): 
        myaccount_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='noo-site']/section/div/div/h1")))
        return myaccount_element.text 

# S2 Open the application in a web browser and login using valid data.
class TestLogin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)   
    def test_go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window() 
# Dismiss pop-up message to have access to My Account button
    def test_dismiss (self):
        dismiss_link = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-store-notice__dismiss-link")))
        dismiss_link.click()
        myaccount_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='noo-site']/header/div[1]/div/ul[2]/li[2]/a")))
        myaccount_button.click()       
# Login using valid data from test_login.py
    def test_login(self, username, password):
        self.wait 
        username_logfield = self.wait.until(EC.element_to_be_clickable((By.ID, "username")))
        username_logfield.click()
        username_logfield.clear()
        username_logfield.send_keys(username)
        password_logfield = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_logfield.click()
        password_logfield.clear()
        password_logfield.send_keys(password)
        checkbox = self.driver.find_element(By.ID,"rememberme")
        checkbox.click()
        login_button = self.driver.find_element(By.XPATH, "//*[@id='customer_login']/div[1]/form/p[3]/button")
        login_button.click() 
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)
# Test logout button
        logout_button = self.driver.find_element(By.XPATH, "//*[@id='post-8']/div/div/div/p[1]/a")
        logout_button.click() 

# S3 Use search bar for a product and on displayed product list apply filters and verify that they are applied.
class TestShop:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)   
    def test_go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()   
# Test filters
    def test_filter_product (self, product):
        self.wait
# In search bar enter product name from test_shop.py
        search_bar = self.driver.find_element(By.CLASS_NAME, "noo-search")
        search_bar.click()
        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='noo-site']/header/div[3]/div[2]/form/input[1]")))
        search_input.send_keys(product) 
        search_input.submit()
# Choose form of product display - list
        filter_style = self.driver.find_element(By.XPATH, "//*[@id='noo-site']/div[2]/div[1]/div/div[2]/form[3]/select")
        filter_style.click()
        filter_object = Select(filter_style)
        filter_object.select_by_visible_text("List")
        time.sleep(3)
# Choose form of product display - relevance or price or date
        filter_relevance = self.driver.find_element(By.XPATH, "//*[@id='noo-site']/div[2]/div[1]/div/form/select")
        filter_relevance.click()
        relevance_object = Select(filter_relevance)
        relevance_object.select_by_value("date")
        time.sleep(3)
# Choose filter color of product
        filter_color = self.driver.find_element(By.CLASS_NAME, "noo-woo-filter")
        filter_color.click()
        color_object = Select(filter_color)
        color_object.select_by_visible_text("Black")
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(3)
# Verify error
    def test_verify_error(self):
        error_text = self.driver.find_element (By.XPATH, "//*[@id='noo-site']/div[2]/p")
        return error_text.text 
# Return to search bar to find and select a product, then add it to a cart and verify that it is in the cart.
    def test_add_to_cart(self, product):
        self.wait
        self.driver.execute_script("window.scrollTo(0, -500);")
        search_bar = self.driver.find_element(By.CLASS_NAME, "noo-search")
        search_bar.click()
# Select product from test_shop.py
        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='noo-site']/header/div[3]/div[2]/form/input[1]")))
        search_input.send_keys(product) 
        search_input.submit()
        self.driver.execute_script("window.scrollTo(0, 500);")
        product_one = self.driver.find_element(By.XPATH, "//*[@id='noo-site']/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/a/img")
        product_one.click()
        self.driver.execute_script("window.scrollTo(0, 500);")
# Choose color of product
        color_option = self.driver.find_element(By.ID, "pa_color")
        color_option.click()
        color_choice = Select(color_option)
        color_choice.select_by_value("white")
# Choose size of product
        size_option = self.driver.find_element(By.ID, "pa_size")
        size_option.click()
        size_choice = Select(size_option)
        size_choice.select_by_value("medium")
        self.driver.execute_script("window.scrollTo(0, 700);")
        time.sleep(3)
# Choose qty of product
        quantity_plus = self.driver.find_element(By.CLASS_NAME, "icon_plus")
        quantity_plus.click()
        time.sleep(3)
        add_button = self.driver.find_element(By.XPATH, "//*[@id='product-1467']/div[1]/div[2]/form/div/div[2]/button")
        add_button.click()
        self.driver.execute_script("window.scrollTo(0, -500);")
# Go to cart
        viewcart_button = self.driver.find_element(By.XPATH, "//*[@id='noo-site']/div[2]/div/div/div[1]/div/a")
        viewcart_button.click()
    def test_your_cart_text(self):
        self.driver.execute_script("window.scrollTo(0, 700);")
# Verify that you are on Cart page
        your_cart_page = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='noo-site']/section/div/div/h1")))
        return your_cart_page.text
    def test_item_name_text(self, xpath):
        self.driver.execute_script("window.scrollTo(0, 700);")
# Verify that correct product is in cart
        item_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return item_title.text
# From cart navigate to the checkout page. 
    def test_checkout_page (self):
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(3)
        checkout_button = self.driver.find_element(By.XPATH, "//*[@id='post-6']/div/div/div[2]/div[2]/div/a")
        checkout_button.click()
    def test_checkout_page_text (self):
# Verify that you are on checkout page
        checkout_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Checkout']")))
        return checkout_text.text 
    
# S5 From cart navigate to the checkout page, enter valid payment details in mandatory fields and verify that the payment is successful. 
class TestPayment: 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)   
    def test_go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()  
# Choose product, color, size, qty and add to cart
    def test_buy_item(self):
        self.driver.execute_script("window.scrollTo(0, 1000);")
        shirt_item = self.driver.find_element(By.XPATH, "//*[@id='noo-site']/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/h3/a") 
        shirt_item.click()
        self.driver.execute_script("window.scrollTo(0, 1000);")
        color_option = self.driver.find_element(By.ID, "pa_color")
        color_option.click()
        color_choice = Select(color_option)
        color_choice.select_by_value("pink")
        size_option = self.driver.find_element(By.ID, "pa_size")
        size_option.click()
        size_choice = Select(size_option)
        size_choice.select_by_value("36")
        quantity_plus = self.driver.find_element(By.CLASS_NAME, "icon_plus")
        quantity_plus.click()
        time.sleep(2)
        add_button = self.driver.find_element(By.XPATH, "//*[@id='product-1497']/div[1]/div[2]/form/div/div[2]/button")
        add_button.click()
        self.driver.execute_script("window.scrollTo(0, 500);")
        cart_button = self.driver.find_element(By.XPATH, "//*[@id='noo-site']/div[2]/div/div/div[1]/div/a")
        cart_button.click()
        self.driver.execute_script("window.scrollTo(0, 800);")
# From cart navigate to checkout
        checkout_button = self.driver.find_element(By.XPATH, "//*[@id='post-6']/div/div/div[2]/div[2]/div/a")
        checkout_button.click()   
# At checkout fill billing information form using data from test_payment.py    
    def test_billing_information (self, name, surname, address, city, code, phone, email):
        self.wait
        self.driver.execute_script("window.scrollTo(0, 800);")
        first_name = self.driver.find_element(By.ID, "billing_first_name")
        first_name.click()
        first_name.clear()
        first_name.send_keys(name) 

        last_name = self.driver.find_element(By.ID, "billing_last_name")
        last_name.click()
        last_name.clear()
        last_name.send_keys(surname) 
        time.sleep(5)
        
        country_billing = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='select2-billing_country-container']")))
        country_billing.click()
        country_choice = self.driver.find_element(By.XPATH, "//*[@id='billing_country']/option[31]")
        country_choice.click()
        time.sleep(5)
        
        address_billing = self.wait.until(EC.element_to_be_clickable((By.ID, "billing_address_1")))
        address_billing.click()
        address_billing.clear()
        address_billing.send_keys(address) 
        self.driver.execute_script("window.scrollTo(0, 500);")
        
        city_billing = self.wait.until(EC.element_to_be_clickable((By.ID, "billing_city")))
        city_billing.click()
        city_billing.clear()
        city_billing.send_keys(city) 
                
        postal_code = self.wait.until(EC.element_to_be_clickable((By.ID, "billing_postcode")))
        postal_code.click()
        postal_code.clear()
        postal_code.send_keys(code) 
        
        phone_billing = self.wait.until(EC.element_to_be_clickable((By.ID, "billing_phone")))
        phone_billing.click()
        phone_billing.clear()
        phone_billing.send_keys(phone) 
    
        email_billing = self.wait.until(EC.element_to_be_clickable((By.ID, "billing_email")))
        email_billing.click()
        email_billing.clear()
        email_billing.send_keys(email) 
# Agree to terms and conditions
    def test_terms (self):
        self.wait
        terms_box = self.wait.until(EC.element_to_be_clickable((By.ID, "terms")))    
        terms_box.click()
# Click place order button
    def test_place_order (self):
        self.wait
        order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='place_order']")))
        order_button.click()
    def test_order (self):
        self.wait
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(3)
# Verify that order is placed
        order_details = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-thankyou-order-received")))
        return order_details.text  
    
    