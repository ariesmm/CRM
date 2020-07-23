from selenium import webdriver

def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def firfox_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver