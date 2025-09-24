import time
import pytest

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime,timedelta

from AppUIVerification.Basefucntion.basepage import wait_for_element
from AppUIVerification.Basefucntion.conftest import driver_setup

def test_app(driver_setup):
    driver = driver_setup
    print("launch successfully")
    time.sleep(3)

    #accept agreement
    driver.find_element(by=AppiumBy.ID, value='hko.MyObservatory_v1_0:id/btn_agree').click()
    driver.find_element(by=AppiumBy.ID, value='hko.MyObservatory_v1_0:id/btn_agree').click()
    time.sleep(3)

    #accept location aggreement
    driver.find_element(by=AppiumBy.ID, value='android:id/button1').click()
    time.sleep(3)

    #click permission allow button
    driver.find_element(by=AppiumBy.ID, value='com.android.packageinstaller:id/permission_allow_button').click()
    '''
    #wait if appear "十号飓风信号" and close the dialog
    page_indicator = (AppiumBy.ACCESSIBILITY_ID, value == '十号飓风信号')
    next_button = (AppiumBy.ID, value == 'hko.MyObservatory_v1_0:id/close_btn')
    '''
    time.sleep(5)

    driver.find_element(by=AppiumBy.ID, value='hko.MyObservatory_v1_0:id/exit_btn').click()
    driver.find_element(by=AppiumBy.ID, value='hko.MyObservatory_v1_0:id/exit_btn').click()
    time.sleep(5)

    #close alert dialog if it displayed
    driver.find_element(by=AppiumBy.ID, value='android:id/button1').click()
    time.sleep(5)

    #validate'我的天文台' display and all dialog close, app open successfully
    driver.find_element(by=AppiumBy.ID, value='hko.MyObservatory_v1_0:id/top_layout')
    print('APP open successfully')
    time.sleep(5)

    #Open 9-day Forecast Screen
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='转到上一层级').click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='已隐藏\n预报及警告服务').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/title" and @text="九天预报"]').click()
    element = wait_for_element(driver, AppiumBy.ACCESSIBILITY_ID, value='九天预报')

    #Get current date
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    #get tomorrow date
    month = tomorrow.month
    day = tomorrow.day
    expected_date = str(month) + '月' + str(day) + '日'
    print(expected_date)

    #Assert1: output the first date
    wait = WebDriverWait(driver, 10)
    date_element = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, format(expected_date))))

    app_date_text=date_element.text
    print(f'first Date text from app: {app_date_text}')

    #Assertion3: verify the fisrtdate = expecteddate
    assert app_date_text==expected_date
    print('assertion pass')

