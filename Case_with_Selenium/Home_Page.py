from selenium.webdriver.common.action_chains import ActionChains

class HomePage():
    element_name = ".section-block:nth-child(3) > .section-button"
    element_body = "body"
    element_about = "About"
    text_selected = '//*[contains(text(),"Grid Dynamics is a publicly-traded")]'
    text_find =                    "Grid Dynamics is a publicly-traded end-to-end software engineering," \
                                " information technology consulting company working with enterprise" \
                                " clients across numerous industries. And our esteemed clients are some" \
                                " of the most respected brands in the world, so there’s a great chance" \
                                " you’ve seen our work!"
   # def open_page(self):
    #    self.open()
    actions = ActionChains(self.driver)