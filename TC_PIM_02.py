from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver_1 = webdriver.Firefox()
driver_1.maximize_window()
sleep(5)
driver_1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver_1.implicitly_wait(20)
driver_1.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver_1.implicitly_wait(20)
driver_1.find_element(By.XPATH, "//*[@type='password']").send_keys("admin123")
driver_1.find_element(By.XPATH, "//*[@type='submit']").click()
driver_1.implicitly_wait(20)
sleep(5)
driver_1.find_element(By.XPATH, "(//li[@class='oxd-main-menu-item-wrapper'])[2]").click()
driver_1.implicitly_wait(20)
driver_1.find_element(By.XPATH, "(//*[@type='button'])[6]").click()
driver_1.implicitly_wait(20)
sleep(5)
driver_1.find_element(By.NAME, "firstName").send_keys("SACHIN")
driver_1.find_element(By.NAME, "middleName").send_keys("RAMESH")    
driver_1.find_element(By.NAME, "lastName").send_keys("tendulkar")
driver_1.find_element(By.XPATH,"(//button[@type='submit'])[2]").click

print("Successfully employee detail addition")
