# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCaseSupprimerPim(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_supprimer_pim(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, ".oxd-form").submit()

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.LINK_TEXT, "PIM").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").send_keys("hello  world")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        elements_before_deletion = driver.find_elements(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div/div/div/label/span/i")

        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div/div/div/label/span/i").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button/i").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        elements_after_deletion = driver.find_elements(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div/div/div/label/span/i")
        
        deleted_element_count = len(elements_before_deletion) - len(elements_after_deletion)
        assert deleted_element_count == 1
        
        time.sleep(5)
    
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
