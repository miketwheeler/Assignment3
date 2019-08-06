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
        elem = driver.find_element_by_id("id_password")
        elem.clear()
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(2)

        # delete comment from logged in user
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[13]/h1/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/a").click()
        time.sleep(1)
        driver.get("http://127.0.0.1:8000")
        time.sleep(2)

        # delete post from logged in user
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[13]/h1/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/a[2]").click()
        time.sleep(1)
        assert "Deleted Blog Entry"
        time.sleep(3)



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
