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
        time.sleep(1)

        #add a post as administrator
        title = "Selenium test title from admin"
        text = "This here is a post sent from admin and this is the text that will display."
        validtodate = "2019-08-05"
        validtotime = "17:34:08"
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/fieldset/div/div/div/select/option[3]").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys(title)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_text")
        elem.send_keys(text)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_published_date_0")
        elem.send_keys(validtodate)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_published_date_1")
        elem.send_keys(validtotime)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input").submit()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/a").click()
        time.sleep(3)

        #add comment as administrator
        author = "tester"
        text1 = "This is a test comment from the admin, made on the post we made at earlier step"
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/fieldset/div/div/div/select/option[12]").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_author")
        elem.send_keys(author)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_text")
        elem.send_keys(text1)
        time.sleep(.5)
        driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input").submit()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/a").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


