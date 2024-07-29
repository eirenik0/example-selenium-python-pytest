import pytest

from appium.webdriver import Remote
from applitools.selenium import *


@pytest.fixture(scope="function")
def eyes():
    eyes = Eyes()
    yield eyes
    eyes.abort()


@pytest.fixture(scope="function")
def driver():
    capabilities = {
        "platformName": "iOS",
        "appium:platformVersion": "17.5",
        "appium:deviceName": "iPhone 15 Pro Max",
        "appium:deviceOrientation": "PORTRAIT",
        "idleTimeout": 180,
        'browserName': 'Safari',
    }
    return Remote(
        command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=capabilities
    )


def test_appium_ios_mob(driver, eyes):
    driver.get("https://demo.appliools.com")
    eyes.open(driver, app_name="Eyes Appium SDK")
    eyes.check(Target.window().fully())
    eyes.close(raise_ex=True)
