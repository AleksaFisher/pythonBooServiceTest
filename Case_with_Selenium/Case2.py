# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCase2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome("/Users/afisher/Downloads/chrome_drivers/98/chromedriver")
   # self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_case2(self):
    self.driver.get("https://blog.griddynamics.com/")
    self.driver.set_window_size(1440, 790)
    self.driver.execute_script("window.scrollTo(0,0.5)")
    element = self.driver.find_element(By.LINK_TEXT, "Solutions")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Cloud & DevOps").click()
    self.driver.execute_script("window.scrollTo(0,4)")
    self.driver.execute_script("window.scrollTo(0,208)")
    self.driver.find_element(By.CSS_SELECTOR, ".cdk-focused > .card-anchor > .background-block").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,329.5)")
    self.driver.execute_script("window.scrollTo(0,233.5)")
    self.driver.find_element(By.CSS_SELECTOR, ".cdk-focused > .card-anchor > .background-block").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,365.5)")
    self.driver.execute_script("window.scrollTo(0,205.5)")
    element = self.driver.find_element(By.LINK_TEXT, "Services")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.LINK_TEXT, "Digital transformation")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.LINK_TEXT, "All solutions")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "All solutions").click()
    self.driver.execute_script("window.scrollTo(0,293.5)")
    self.driver.find_element(By.CSS_SELECTOR, ".cdk-focused > .description-label").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,269)")
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,203)")
    self.driver.find_element(By.CSS_SELECTOR, ".cdk-focused > .description-label").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,268.5)")

   # print(f"selected_text:{selected_text}\n")
   # assert selected_text == HomePage.text_find
