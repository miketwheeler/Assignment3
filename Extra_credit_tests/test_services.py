import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test_services_mfscrm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
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

        #select services from main page
        serv_cat = "Food Prep/Delivery"
        Description = "Delivering fresh food from the side-Wok"
        location = "Mammel  Rm 240"
        serv_charge = 500
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[3]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/select/option[5]").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys(serv_cat)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys(Description)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_location")
        elem.send_keys(location)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys(serv_charge)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/form/button").submit()
        time.sleep(2)

        # edit this product - update quantity and price
        n_descr = "This food is fantastic and relevant for business meetings, comes with plates and napkins but no forks!"
        n_serv_charge = 1000
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[8]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_description")
        elem.clear()
        elem.send_keys(n_descr)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_service_charge")
        elem.clear()
        elem.send_keys(n_serv_charge)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/form/button").submit()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()