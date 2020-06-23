from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class UICatalogPage(object):
    def __init__(self, context):
        #self.driver = context.driver
        self.driver = context.driver
        #context.driver = context.driver

        #self.alert_menu = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(MobileBy.ACCESSIBILITY_ID, "Alert Views"))

    #Alert_menu = WebDriverWait()
    locator_dictionary = {
        "Alert": "Alert Views",
        #"Others": (MobileBy.ACCESSIBILITY_ID, "Other"),
        #"Cancel": (MobileBy.ACCESSIBILITY_ID, "Cancel")
    }

    def get_element_by_id(self, element_id):
        #return self.driver.find_element_by_accessibility_id(element_id)
        #if (EC.presence_of_element_located(MobileBy.ACCESSIBILITY_ID, element_id)):
        #    print("Inside EC")
        #else:
        #    print("inside else")
        #element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MobileBy.ACCESSIBILITY_ID, element_id))
        return self.driver.find_element_by_accessibility_id(element_id)


