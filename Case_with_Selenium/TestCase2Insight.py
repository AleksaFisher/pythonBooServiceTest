from selenium import webdriver
from selenium.webdriver.common.by import By


import logging
LOGGER = logging.getLogger(__name__)

class TestTestCase2Insight():
    def setup_method(self, method):
        self.driver = webdriver.Chrome("/Users/afisher/Downloads/chrome_drivers/98/chromedriver")



    def teardown_method(self, method):

        pass

    def test_case2(self):
        self.driver.get("https://blog.griddynamics.com/")
        self.driver.set_window_size(1440, 790)


        element = self.driver.find_element(By.LINK_TEXT, "Insights")
        assert element.is_displayed()
        element.click()

        # element = self.driver.find_element(By.LINK_TEXT, "Articles")
        # assert element.is_displayed()
        # element.click()

        self.driver.find_element(By.CSS_SELECTOR, "#topiclist .selected").click()
        self.driver.find_element(By.CSS_SELECTOR, "div > span:nth-child(6)").click()
        self.driver.find_element(By.CSS_SELECTOR, "#topiclist .selected").click()
        self.driver.find_element(By.CSS_SELECTOR, "#topiclist > div").click()

        element =  self.driver.find_element(By.CSS_SELECTOR, "#topiclist .selected")
        assert element.is_displayed()
        # cloud devops in filter
        element.click()

        element = self.driver.find_element(By.CSS_SELECTOR, "div > span:nth-child(6)")
        assert element.is_displayed()
        element.click()


        #element = self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c66-5 > .ng-star-inserted:nth-child(1) span")
       # assert element.is_displayed()
        #element.click()

        element5 = self.driver.find_elements(By.XPATH, "//div[@class='row regular insertsearch']")
        LOGGER.critical(f"List:{len(element5)}")
        assert len(element5) > 0