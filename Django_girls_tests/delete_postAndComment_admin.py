import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class create_post_admin_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(.5)
        driver.find_element_by_id("login-form").submit()

        time.sleep(.5)

        # delete a post as administrator
        title = "Selenium test title from admin"
        text = "This here is a post sent from admin and this is the text that will display."
        validtodate = "2019-08-05"
        validtotime = "17:34:08"
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/a").click()
        time.sleep(.5)
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div/label/select/option[2]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td/input").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").submit()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[4]").submit()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/a").click()
        time.sleep(3)

        # delete comment as administrator
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div/label/select/option[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td/input").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").submit()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[4]").submit()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/a").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()