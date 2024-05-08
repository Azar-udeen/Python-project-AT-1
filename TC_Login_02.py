from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class HRMLogin():

    def __init__(self):
        self.username = "Admin"
        self.password = "Invalidpassword"
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
        sleep(2)



login_test = HRMLogin()
login_test.login()
# Perform other actions after successful login if needed








