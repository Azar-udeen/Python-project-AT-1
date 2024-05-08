from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class HRMLogin():

    def __init__(self):
        self.username = "Admin"
        self.password = "admin123"
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        sleep(2)
        #Enter valid credentials
        webelement_of_username = self.driver.find_element(By.NAME,"username")
        webelement_of_username.send_keys(self.username)
        Webelement_of_password = self.driver.find_element(By.NAME,"password")
        Webelement_of_password.send_keys(self.password)
        Webelement_of_Login_button = self.driver.find_element(By.XPATH,'//button[@type="submit"]')
        Webelement_of_Login_button.click()

    def add_employee(self):
        # Go to PIM module
        pim_module = self.driver.find_element(By.XPATH,"(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]")
        pim_module.click()

        # Click on Add
        add_button = self.driver.find_element(By.XPATH,'//button[@type="submit"]')
        add_button.click()

        # Fill in employee details
        first_name_input = self.driver.find_element(By.NAME,"firstName")

        last_name_input = self.driver.find_element(By.NAME,"lastName")

        first_name_input.send_keys("Karthi")
        last_name_input.send_keys("Raja")
        #Enter employee Id
        employee_id = self.driver.find_element(By.CLASS_NAME,"oxd-input oxd-input--active")
        employee_id.send_keys("0420")

        # Click save
        save_button = self.driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space")
        save_button.click()


login_test = HRMLogin()
login_test.login()
# Perform other actions after successful login if needed
login_test.add_employee()







