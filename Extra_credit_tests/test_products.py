import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test_products_mfscrm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(1)

        # add a new product to a customer
        product = "Sparkling Fruit Tray"
        pDescr= "This is a tropical and berries tray organized to impress and entice devouring."
        qty = 10
        charge = 500
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[3]/a").click()
        time.sleep(1.2)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/select/option[5]").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_product")
        elem.send_keys(product)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys(pDescr)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(qty)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys(charge)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div/form/button").submit()
        time.sleep(2)

        # edit this product - update quantity and price
        n_qty = 20
        n_charge = 1000
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[7]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_quantity")
        elem.clear()
        elem.send_keys(n_qty)
        time.sleep(.5)
        elem = driver.find_element_by_id("id_charge")
        elem.clear()
        elem.send_keys(n_charge)
        time.sleep(.5)
        driver.find_element_by_xpath("/html/body/div/div/div/form/button").submit()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()