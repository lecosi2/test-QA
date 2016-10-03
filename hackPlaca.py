# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestExpress(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        """desired_cap = {'browser': 'Chrome', 'browser_version': '47.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
        self.driver = webdriver.Remote(
        command_executor='http://lecosi2:qBJHZpaet33yrXqofYFZ@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)"""
        self.driver.implicitly_wait(30)
        self.base_url = "https://seguros.comparamejor.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_express(self):
        driver = self.driver
        driver.get(self.base_url + "/seguros-para-vehiculos/express/#/consultar-placa")
        driver.find_element_by_id("vehicle_registration").clear()
        driver.find_element_by_id("vehicle_registration").send_keys("xcv234")
        driver.find_element_by_xpath("//*[@id='button-quote']").click()
        time.sleep(5)
        placa=driver.find_element_by_xpath("//*[@id='step-vehicle-body']/span[1]").text
        print "placa= "+ placa
        if placa == "CHEVROLET - CRUZE PLATINUM [LT]/2013":
            print "pasó sin problemas"
        else:
            raise Exception ("se demoró mucho el hack")
 
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
