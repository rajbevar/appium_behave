import os
from time import sleep

from appium import webdriver
import argparse


def before_all(context):
    # context.config.setup_logging()
    pass

def before_feature(context, feature):
    if 'android' in feature.tags:
        app = os.path.join(os.path.dirname(__file__),
                           '../apps/Imdb/android',
                           'com.imdb.mobile.apk')
        app = os.path.abspath(app)
        context.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app' : app,
                'platformName' : 'Android',
                'platformVersion' : '4.4',
                'deviceName' : None,
                'udid' : '01a135891395669f',
                'appActivity' : '.HomeActivity',
                'appPackage' : 'com.imdb.mobile'
            }
        )
    elif 'ios' in feature.tags and 'simple1' in feature.tags:
        print("Entered inside before feature")
        '''
        app = os.path.join(os.path.dirname(__file__),
                           '../apps/TestApp/build/Release-iphonesimulator',
                           'TestApp.app')
        '''
        app = "/Users/rajani/Desktop/UICatalog 2.app"
        #app = os.path.abspath(app)

        context.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '12.4',
                #'platformVersion': '13.2.2',
                #'platformVersion': '12.3.1',
                "automationName": 'XCUITest',
                'deviceName': "iPhone 6s",
                #"udid": "93d132319fa379e2ed89b722d285797ac18a43a5",
                #"udid": "71c23d2a5b4e375bff404cdc33f46c5e51e943a0",
                #"deviceName": "HFTest iPhone"
                #"deviceName": "Rajani's iPhone"
            })
    elif 'ios' in feature.tags and 'butcele' in feature.tags:
        app = os.path.join(os.path.dirname(__file__),
                           '../apps/Butcele',
                           'butcele.app')
        app = os.path.abspath(app)
        context.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '8.3',
                'deviceName': "iPhone 6" # Force device to run on simulator such as : iPhone 6
            })

def after_feature(context, feature):
    sleep(1)
    context.driver.save_screenshot("features/reports/screen_final.png")
    context.driver.quit()