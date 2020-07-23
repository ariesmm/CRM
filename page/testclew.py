import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost/index.php?m=leads')
time.sleep(3)
driver.find_element(By.NAME,'name').clear()
driver.find_element(By.NAME,'name').send_keys("admin")
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys("zls19930227")
driver.find_element(By.NAME,'autologin').click()
driver.find_element(By.NAME,'submit').click()
driver.find_element(By.XPATH,'//div[@class="nav-collapse collapse"]/ul[1]/li[1]/a').click()
driver.find_element(By.CLASS_NAME,'btn-primary').click()
driver.find_element(By.ID,'contacts_name').send_keys('zhoulisha')
driver.find_element(By.NAME,'submit').click()