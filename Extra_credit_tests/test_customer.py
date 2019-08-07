import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test_customer_mfscrm(unittest.TestCase):
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

        # from homepage select customer
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[3]/a").click()
        time.sleep(2)

        # Add a new customer
        cust_n = "Buzz Lightyear"
        org = "Infinity and Beyond"
        r = "Toy"
        bldg = 704
        acct = 999999999
        addr = "3333 Madison Rd."
        cit = "Omaha"
        st = "NE"
        zip = 11111
        email = "buzzlightyear@unoamaha.edu"
        phnum = 4023339999

        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/div/input")
        elem.send_keys(cust_n)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/div/input")
        elem.send_keys(org)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/div/input")
        elem.send_keys(r)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[4]/div/input")
        elem.send_keys(bldg)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[5]/div/input")
        elem.send_keys(acct)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[6]/div/input")
        elem.send_keys(addr)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[7]/div/input")
        elem.send_keys(cit)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[8]/div/input")
        elem.send_keys(st)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[9]/div/input")
        elem.send_keys(zip)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[10]/div/input")
        elem.send_keys(email)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[11]/div/input")
        elem.send_keys(phnum)

        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(1)
        driver.refresh()
        time.sleep(1)

        # Edit existing customer that was added
        n_bldg = 704
        n_addr = "3333 Madison Rd."

        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[12]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/form/div[4]/div/input").clear()
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[4]/div/input")
        elem.send_keys(n_bldg)
        driver.find_element_by_xpath("/html/body/div/div/div/form/div[6]/div/input").clear()
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[6]/div/input")
        elem.send_keys(n_addr)

        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(1)
        driver.refresh()
        time.sleep(1)

        # Get a customer's summary (that has products and services)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[14]/a").click()
        time.sleep(1)

        # nav back to customer list
        driver.find_element_by_xpath("/html/body/nav/div/div/a").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()