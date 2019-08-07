import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test_deletes_mfscrm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        #get homepage, login user
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(1)

        #delete from services
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[3]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[9]/a").click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.get("http://127.0.0.1:8000")

        #delete from products
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[3]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[8]/a").click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.get("http://127.0.0.1:8000")

        #delete from customers
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[3]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[13]/a").click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(2)