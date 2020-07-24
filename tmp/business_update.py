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


driver.find_element(By.XPATH,'//div[@class="nav-collapse collapse"]/ul[1]/li[3]/a').click()#商机菜单

'''编辑'''
# driver.find_element(By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[3]').click()#点击编辑
# time.sleep(2)
# driver.find_element(By.ID, 'owner_name').click()# 选择负责人
# time.sleep(2)
# driver.find_element(By.XPATH,'//tbody[@id="d_content"]/tr[1]/td[1]/input').click()#进行选择
# driver.find_element(By.CSS_SELECTOR,'div[id="dialog-role-list"]+div>div :nth-child(1)').click()  # 点击OK
#
# driver.find_element(By.ID, 'customer_name').click()  # 选择客户
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="datas"]/tr[1]/td[1]/input[1]').click()
# driver.find_element(By.CSS_SELECTOR, 'div[id="dialog-message"]+div>div :nth-child(1)').click()  # 点击OK
#
# driver.find_element(By.NAME,'submit').click()

'''推进'''
# driver.find_element(By.CLASS_NAME,'advance').click()
# time.sleep(2)
# # ele = driver.find_element(By.XPATH,'//div[@id="dialog-advance"]/form/table/tbody/tr[2]/td[2]/select')
# # select = Select(ele)
# # select.select_by_visible_text("签订合同")
# driver.find_element(By.XPATH,'//div[@id="dialog-advance"]/form/table/tbody/tr[5]/td[2]/input[1]').click()

'''删除'''
# driver.find_element(By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[1]/input').click()
# driver.find_element(By.ID,'delete').click()
# driver.switch_to.alert.accept()

'''查看'''
driver.find_element(By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[1]').click()#查看
driver.find_element(By.XPATH,'//ul[@id="left_list"]/li[1]/span')