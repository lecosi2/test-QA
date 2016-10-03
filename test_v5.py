# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest, time, re

class TestV5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities= DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(3)
        self.base_url = "https://seguros.comparamejor.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_v5(self):
        driver = self.driver
        driver.get(self.base_url + "/seguros-para-vehiculos/v5/#/consultar-placa")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("yph79c")
        driver.find_element_by_xpath("//div[@id='step-query-registration']/div/div[2]/form/button").click()
        print "ingresa placa"
        driver.implicitly_wait(5)
        driver.find_element_by_css_selector("div.btnuj.btn-icon-content").click()
        print "tipo de vehiculo"
        driver.find_element_by_xpath("//img[@alt='RENAULT']").click()
        print "pasó boton3"
        driver.find_element_by_xpath("//div[@id='step-vehicle-model']/div[2]/div[35]").click()
        print "pasó boton4"
        driver.find_element_by_css_selector("span.btnuj").click()
        print "pasó boton5"
        driver.find_element_by_xpath("//*[@id='step-vehicle-reference']/ul/li/span").click()
        print "pasó boton6"
        driver.find_element_by_css_selector("#step-vehicle-complete-reference > ul > li:nth-child(1) > span").click()
        print "pasó boton7"
        driver.find_element_by_css_selector("i.cmuj-path").click()
        print "pasó boton8"
        driver.find_element_by_css_selector("div.btnuj.btn-icon-content").click()
        print "pasó boton9"
        driver.find_element_by_css_selector("#step-vehicle-body > ul > li:nth-child(1)").click()
        print "pasó boton10"
        driver.find_element_by_css_selector("#step-vehicle-city > ul > li:nth-child(1) > span").click()
        driver.find_element_by_css_selector("#step-identification-type > ul > li:nth-child(1)").click()
        print "pasó boton11"
        driver.find_element_by_xpath("//input[@type='text']").clear()
        print "pasó boton12"
        driver.find_element_by_xpath("//input[@type='text']").send_keys("1070611554")
        print "pasó boton13"
        driver.find_element_by_xpath("//div[@id='step-identification']/form/button").click()
        print "pasó boton14"
        time.sleep(2)
        driver.find_element_by_xpath("//input[@type='text']").clear()
        print "pasó boton15"
        driver.find_element_by_xpath("//input[@type='text']").send_keys("test")
        print "pasó boton16"
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        print "pasó boton17"
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
        print "pasó boton18"
        driver.find_element_by_xpath("//div[@id='step-complete-name']/form/button").click()
        print "pasó boton19"
        driver.find_element_by_css_selector("div.btnuj.btn-icon-content").click()
        print "pasó boton20"
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/table/tbody/tr/td[2]/div[2]/div[53]").click()
        print "pasó boton21"
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/table/tbody/tr[3]/td[2]/div[2]/div[11]").click()
        print "pasó boton22"
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/table/tbody/tr[5]/td[2]/div[2]/div[26]").click()
        print "pasó boton23"
        driver.find_element_by_xpath("//div[@id='step-date-of-birth']/button").click()
        print "pasó boton24"
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("leohcollazos@gmail.com")
        driver.find_element_by_xpath("//div[@id='step-email-address']/form/button").click()
        driver.find_element_by_id("mobile_phone").clear()
        driver.find_element_by_id("mobile_phone").send_keys("3131111111")
        driver.find_element_by_xpath("//div[@id='step-phone-numbers']/form/button").click()
        driver.find_element_by_xpath("//div[@id='step-current-situation']/ul/li[5]/span/span").click()
        print "datos personales"
        driver.find_element_by_xpath("//*[@id='step-promocode']/ul/li[2]/div").click()
        print "describe situacion actual"
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='step-promocode']/ul/li[2]/div").click()
        driver.find_element_by_xpath("//*[@id='step-promocode']/div[3]/label/input").click
        driver.find_element_by_xpath("//*[@id='step-promocode']/div[4]/label/input").click()
        print "codigo promocional"
        driver.find_element_by_xpath("//*[@id='step-promocode']/button").click

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
