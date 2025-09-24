from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element(driver: object, by: object, value: object, timeout: object = 10) -> WebElement | None:
    #wait element function
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        return element
    except Exception as e:
        print("wait element not found")
        return None


def click_next_if_page_present(driver: object, by: object, value: object, timeout: object = 10) -> WebElement:
#click next button if page show
    try:
        #wait element appear
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((page_indicator_locator)))
        print("page found")

        #click next button
        next_button = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((next_button_locator)))
        next_button.click()
        print("next button clicked")

        return True
    except Exception as e:
        print("clicknext element not found")
        return None