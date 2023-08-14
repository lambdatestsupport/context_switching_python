from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

location_data = {
    "lat": "51.2277",
    "long": "0.00"
}


latitude = float(location_data['lat'])
longitude = float(location_data['long'])


desired_caps = {
    "deviceName":"Galaxy S22 Ultra 5G",
    "platformName": "Android",
    "platformVersion": "13",
    "app": "lt://APP10160631101690291653597364",  # Enter app_url here
    "isRealMobile": True,
    "build": "Python Vanilla Android",
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True,
    "language":"en",
    "locale":"GB",
    "autoAcceptAlerts":True,
    "autoDismissAlerts":True,
    "autoGrantPermissions":True,
    "fixedIP":"R5CT20LXYGL"

    # "locationServicesAuthorized": True,
    # "locationServicesEnabled": True,
    # "gpsEnabled": True,
    # "location": f"{latitude},{longitude}"

}


def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  "ritamg"+":"+"ur_acessKey"+"@mobile-hub.lambdatest.com/wd/hub")
        confirm = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.trivago.dev:id/activityPlatformSelectionConfirmButton")))
        confirm.click()
        time.sleep(15)
        window_size = driver.get_window_size()
        start_x = int(window_size['width'] / 2)
        start_y = int(window_size['height'] * 0.8)
        end_x = start_x
        end_y = int(window_size['height'] * 0.2)

        i=0
        while(i<=2):
            driver.swipe(start_x, start_y, end_x, end_y, duration=50)
            i+=1
        allow = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.XPATH, "//*[@resource-id='com.trivago.dev:id/activityCookieConsentContentAcceptButton']")))
        allow.click()
        time.sleep(15)
        yes = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.XPATH, "//*[@resource-id='com.trivago.dev:id/fragmentHomeExpandedDealformSearchTextView']")))
        yes.click()
        time.sleep(30)
        view = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.XPATH, "//*[@resource-id='com.trivago.dev:id/viewBestDealViewOfferTextView']")))
        view.click()
        time.sleep(45)
        #all_context gets all the contexts
        all_contexts = driver.contexts
        print(all_contexts)
        driver.switch_to.context('WEBVIEW_chrome')
        #current context gets the current context
        current_context = driver.context
        print("Current Context:", current_context)
        #Switch to current context
        driver.switch_to.context(current_context)
        time.sleep(45)
        driver.quit()
    except:
        driver.quit()


startingTest()
