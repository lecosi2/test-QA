# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestExpress(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities= DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(30)
        self.base_url = "https://seguros.comparamejor.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_express(self):
        driver = self.driver
        driver.get(self.base_url + "/seguros-para-vehiculos/express/#/consultar-placa")
        driver.find_element_by_id("vehicle_registration").clear()
        driver.find_element_by_id("vehicle_registration").send_keys("xcv324")
        driver.find_element_by_xpath("//*[@id='button-quote']").click()
        time.sleep(2)
        driver.find_element_by_css_selector("i.cmuj-car").click()
        driver.find_element_by_css_selector("img.img-responsive").click()
        Select(driver.find_element_by_id("models")).select_by_visible_text("2014")
        driver.find_element_by_xpath("//div[@id='step-vehicle-model']/div[2]/span[2]/span").click()
        driver.find_element_by_css_selector("span.text").click()
        driver.find_element_by_css_selector("span.btnuj").click()
        driver.find_element_by_xpath("//*[@id='step-vehicle-reference']/ul/li[1]/span/span").click()
        driver.find_element_by_xpath("//div[@id='step-vehicle-zero-km']/ul/li[2]/div/span").click()
        driver.find_element_by_css_selector("div.btn-icon-content > span.icon").click()
        driver.find_element_by_css_selector("span.text").click()
        driver.find_element_by_xpath("//*[@id='step-identification-type']/ul/li[1]").click()
        driver.find_element_by_id("identification").clear()
        driver.find_element_by_id("identification").send_keys("1070611554")
        driver.find_element_by_xpath("//div[@id='#identification']/div/div/div/div/div[2]/button").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("test")
        driver.find_element_by_id("last").clear()
        driver.find_element_by_id("last").send_keys("test")
        Select(driver.find_element_by_id("occupation")).select_by_visible_text("Empleado(a)")
        Select(driver.find_element_by_id("year")).select_by_visible_text("1980")
        Select(driver.find_element_by_id("month")).select_by_visible_text("Noviembre")
        Select(driver.find_element_by_id("day")).select_by_visible_text("18")
        Select(driver.find_element_by_id("sex")).select_by_visible_text("Masculino")
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/div[2]/div[2]/button").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("leohcollazos@gmail.com")
        driver.find_element_by_id("mobile_phone").clear()
        driver.find_element_by_id("mobile_phone").send_keys("321465732")
        driver.find_element_by_xpath("//div[@id='step-email-address']/div[2]/ul/li[2]/span/span/span").click()
        driver.find_element_by_id("mobile_phone").clear()
        driver.find_element_by_id("mobile_phone").send_keys("3214657321")
        driver.find_element_by_xpath("//div[@id='step-email-address']/div[2]/ul/li[2]/span/span/span").click()
        driver.find_element_by_xpath("//div[@id='step-promocode']/ul/li[2]/div").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[4]/div/div[2]").click()
        time.sleep(15)
        opp = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[3]/span[1]/span[2]").text
        print "opp= " + opp

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
