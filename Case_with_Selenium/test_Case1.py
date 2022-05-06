# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from Case_with_Selenium.Home_Page import HomePage

class TestCase1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome("../chromedriver/chromedriver")


    def teardown_method(self, method):
        self.driver.quit()

    def test_case1(self):
        self.driver.get("https://blog.griddynamics.com")
        self.driver.set_window_size(1440, 790)
        element = self.driver.find_element(By.CSS_SELECTOR, HomePage.element_name)
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.CSS_SELECTOR, HomePage.element_body)
        element = self.driver.find_element(By.LINK_TEXT, HomePage.element_about)
        self.driver.find_element(By.LINK_TEXT, HomePage.element_about).click()

        selected_text = self.driver.find_element(By.XPATH,
                                                 HomePage.text_selected).text
        print(f"selected_text:{selected_text}\n")
        assert selected_text == HomePage.text_find

