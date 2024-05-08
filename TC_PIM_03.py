
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class Test_login():
    def setup(self):
        self.driver_1 = webdriver.Chrome()
        self.driver_1.maximize_window()

    def Test_Login_failed(self):
        self.driver_1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver_1.implicitly_wait(20)
        self.driver_1.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver_1.implicitly_wait(20)
        self.driver_1.find_element(By.XPATH, "//*[@type='password']").send_keys("admin123")
        self.driver_1.find_element(By.XPATH, "//*[@type='submit']").click()
        self.driver_1.implicitly_wait(20)
        self.driver_1.find_element(By.XPATH, "(//li[@class='oxd-main-menu-item-wrapper'])[2]").click()
        self.driver_1.implicitly_wait(20)
        self.driver_1.find_element(By.XPATH, "(//*[@type='button'])[7]").click()
        self.print("Delete Employee successfully")

    def tearDown(self):
        self.driver_1.close()
        self.driver_1.quit()