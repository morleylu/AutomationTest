import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
import os


@pytest.fixture(scope="module")
def driver_setup():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'platformVersion': '9',
       # 'path': 'D:\\MyObservatory.apk',
        # apk package name
        'appPackage': 'hko.MyObservatory_v1_0',
        # apk launcherActivity
        'appActivity': 'hko.MyObservatory_v1_0.AgreementPage'
        }

    #setup Appium options and contect the server
    options = UiAutomator2Options().load_capabilities(desired_caps)
    appium_server_url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(appium_server_url, options=options)

    #Provide the driver instance to the test
    yield driver

    #Quit the driver after test complete
    if driver:
        driver.quit()

    return driver