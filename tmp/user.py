import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
time.sleep(2)

driver.find_element(By.XPATH,'//div[@class="nav-collapse collapse"]/ul[2]/li[6]/a').click()#用户设置
driver.find_element(By.LINK_TEXT,"组织架构").click()#组织架构

driver.find_element(By.ID,'add_department').click()#新增部门
time.sleep(1)
driver.find_element(By.NAME,'name').send_keys("总经办")
driver.find_element(By.XPATH,'/html/body/div[8]/div[3]/div/button[1]').click()
time.sleep(1)
driver.find_element(By.ID,'add_role').click()#添加岗位
time.sleep(1)
driver.find_element(By.XPATH,'//form[@id="role_add"]/div[1]/div/input').send_keys("行政主管")
ele = driver.find_element(By.NAME,'department_id')
select = Select(ele)
select.select_by_visible_text('总经办')
driver.find_element(By.XPATH,'/html/body/div[9]/div[3]/div/button[1]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'a[id="add_role"]+a').click()#添加用户
time.sleep(3)
driver.find_element(By.CLASS_NAME,'').send_keys("zhangsan")#用户名
driver.find_element(By.ID,'password').send_keys("zhangsan")#密码

# ele = driver.find_element(By.NAME,'category_id')
# select = Select(ele)
# select.select_by_visible_text("管理员")



