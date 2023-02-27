## Shop.Demoqa Smoke Test 

This is automated smoke test for e-commerce application 
:arrow_right:<https://shop.demoqa.com/>

:information_source:
<p align="justify">Main purpose of this e-commerce application is to provide users with positive shopping experience, so for creating this automated smoke test we have followed next assignment steps:

- Write test cases for this application (concentrate on real user flows)
- From all the test cases, identify what you think represents a Smoke Test
- Identify positive and negative test cases
- With a programming/scripting language and testing framework of your choice, automate the smoke test 
- Create Github repository and push your assignment solution with the documentation on how to run the automated tests there (focus on writing comprehensive Readme file)
- Report bugs if you find any, with detailed steps to reproduce
</p>

#### Requirements
<p align="justify">This automated test is created using Python programming language in Visual Studio Code as a code editor with Pytest and Selenium version 4.5.0 testing framework as in combination they can be used primarily for writing end-to-end tests for testing frontend applications.
</p>

#### Recommended
1. Check if Python is installed C:\Users> python --version
2. If You do not have Python installed you can download it on :arrow_right:<https://www.python.org/>
3. Download latest Python version and start instalation file
4. Click on checkbox “Add Python 3.10 to PATH” in last instalation screen
5. To install Selenium for Python we must use command 
`pip install selenium`
(Ruby gem command, NuGet in C#...)
In our test file later we will use first line of code
`from selenium import webdriver` 
to call for a driver
6. Next thing to install is a driver for web
browser. We will use webdriver_manager package so that we wouldn't have to install driver for each web driver seperately. When we use webdriver_manager package we can import any driver in our test file. To install webdriver_manager we must give next command
`pip install webdriver_manager`
7. In test file import ChromeDriverManager from webdriver_manager.chrome package with second line of code 
`from webdriver_manager.chrome import ChromeDriverManager`
Then in the same file we will import Service from
selenium.webdriver.chrome.service pacakge with third line of code 
`from selenium.webdriver.chrome.service import Service`
In next step we will create Service instance by adding line of code
`service = Service(executable_path=ChromeDriverManager().install())`
Then we will initialize driver using previously created Service instance in which we have saved variable service by adding next line of code
`driver = webdriver.Chrome(service=service)`
Keep in mind that we have initialized driver by using driver variable and we will use that same variable for all interactions with our web browser, in this case Google Chrome. 
**Also, these code lines are ofcourse already written in this test but are here for clarification.**
**If you are not using Chrome web browser**, you can find instructions for other browsers following this link
:arrow_right:<https://pypi.org/project/webdriver-manager/>
8. To install pytest we will then use command
`pip install pytest`

###Project structure for pytest
After installing pytest we must adjust our file and folder structure:
1. in Project folder create folder *pages* containing product code packages
1. in Project folder create folder *tests* in which we will put all files containing tests 
2. name of each test file must begin with _test or end with _test
3. tests inside files must be functions whose names begin with test_ and can stand outside class or in class (class name must begin with *Test*)
4. we start tests using command `pytest` in home_page.py 
5. we use file conftest.py as a fixture which enables us to set certain preconditions, to control the Setup and Teardown of tests and runs.

:information_source: **More information**
:arrow_right: <https://rb.gy/mfyb9v>
:arrow_right: <https://docs.pylenium.io/getting-started/project-structure-with-pytest>

<p align="justify"><b>If you are using Visual Studio Code it is important to keep in mindthat this editor does not directly support Python.</b> Therefore, we need VS code extensions for python such as Pylance, Python and IntelliCode by Microsoft.</p>
         
## What did we test :grey_question:
    - Creating an account / Register test
    - Logging in with an existing account / Login test
    - Shopping for products / Shop test
    - Placing an order / Payment test

<p align="justify">At the begining of tests regarding creating an account and logging in it is important to keep in mind pop-up warning which we <b>must</b> remove to have access to My Account link.</p>
```python
def dismiss (self):
    dismiss_link = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-store-notice__dismiss-link")))
    dismiss_link.click()
```

## Smoke Test Results :grey_exclamation:
<p align="justify">Among 26 test cases concentrated on real user flows, 5 were identified and chosen for Smoke test.</p>

<p align="justify">Automated Smoke Test has show us one defect ID BS3 classified as minor keeping in mind that the user can view products and finalize shopping.</p>

![Screenshot](/screenshots/Screenshot%20B01.jpg)
*screenshot B01: Page contains products in color "Black"*

Then
![Screenshot](/screenshots/Screenshot%20B01%20(2).jpg)
*screenshot B01: When using color filter for color black above message appears and same problem occurs with other filters*

