import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class createPostLoggedInUser_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.clear()
        elem.send_keys(user)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_password")
        elem.clear()
        elem.send_keys(pwd)
        time.sleep(.5)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()