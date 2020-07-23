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
#新增线索
# driver.find_element(By.XPATH,'//div[@class="nav-collapse collapse"]/ul[1]/li[1]/a').click()
# driver.find_element(By.CLASS_NAME,'btn-primary').click()
# driver.find_element(By.ID,'contacts_name').send_keys('zhoulisha')
# driver.find_element(By.NAME,'submit').click()


#商机
driver.find_element(By.XPATH,'//div[@class="nav-collapse collapse"]/ul[1]/li[3]/a').click()#商机菜单
driver.find_element(By.CLASS_NAME,'btn-primary').click()#添加商机按钮

driver.find_element(By.ID,'owner_name').click()    #选择负责人
time.sleep(2)
driver.find_element(By.XPATH,'//tbody[@id="d_content"]/tr[1]/td[1]/input').click()
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-role-list"]+div>div :nth-child(1)').click()  #点击OK

driver.find_element(By.ID,'customer_name').click()  #选择客户
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="datas"]/tr[1]/td[1]/input[1]').click()
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-message"]+div>div :nth-child(1)').click()  #点击OK
driver.find_element(By.ID,'name').send_keys("新增商机123")        #商机名
driver.find_element(By.ID,'estimate_price').send_keys("10000")  #预计成交价

driver.find_element(By.XPATH,'//form[@id="form1"]/table/tbody/tr[12]/th/input').click()  #添加产品
time.sleep(2)
driver.find_element(By.XPATH,'//tbody[@id="data"]/tr[1]/td[1]/input[1]').click()
driver.find_element(By.CSS_SELECTOR,'div[id="dialog-product-list"]+div>div :nth-child(1)').click()  #点击OK
driver.find_element(By.XPATH,'//form[@id="form1"]/table/tfoot/tr/td/input[1]').click() #点击保存
time.sleep(2)
driver.find_element(By.XPATH,'//from[@id="form1"]/table/tbody/tr[1]/td[12]/a[3]').click()#点击编辑
time.sleep(2)
driver.quit()
