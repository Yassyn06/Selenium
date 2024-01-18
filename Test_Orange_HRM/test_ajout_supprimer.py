# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestCaseAjouterSupprimer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case_ajouter_supprimer(self):
        driver = self.driver
       # Connexion
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(0.5)
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(0.5)

        
        # Navigation sur la page viewEmployeeList
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.LINK_TEXT, "PIM").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        time.sleep(0.5)

       # Ajout de l'élément:
        
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")

        driver.find_element(By.NAME, "firstName").click()
        driver.find_element(By.NAME, "firstName").clear()
        driver.find_element(By.NAME, "firstName").send_keys("hello")
        time.sleep(0.5)
        driver.find_element(By.NAME, "lastName").clear()
        driver.find_element(By.NAME, "lastName").send_keys("world")
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        time.sleep(3)


       # Suppression de l'élément:
        
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/110")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li[2]/a/span").click()
        
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").send_keys("hello  world")
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        
        nombre_elements = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print(f'Nombre des éléments après ajout : {len(nombre_elements)}')
        time.sleep(0.5)

        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div/div/div/label/span/i").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button/i").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        time.sleep(0.5)

        nombre_elements = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
        print(f'Nombre des éléments après suppression : {len(nombre_elements)}')
        time.sleep(3)
    
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

    