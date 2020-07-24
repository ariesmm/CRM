import time


class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url=url)
        time.sleep(2)

    def quit(self):
        self.driver.quit()
