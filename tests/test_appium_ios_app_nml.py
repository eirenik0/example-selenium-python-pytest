import pytest

from appium.webdriver import Remote
from applitools.selenium import *

from tests.utils import get_resource_path


@pytest.fixture(scope="function")
def eyes():
    eyes = Eyes()
    eyes.configure.add_multi_device_target(
        IosMultiDeviceTarget.iPhone_11_Pro,
        IosMultiDeviceTarget.iPhone_13,
        IosMultiDeviceTarget.iPhone_14,
    )
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
        'automationName': 'XCUITest',
        'app': get_resource_path('UFGTestApp_x86.app.zip')
    }
    return Remote(
        command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=capabilities
    )


def test_appium_ios_web(driver, eyes):
    eyes.open(driver, app_name="Eyes Appium SDK")
    eyes.check(Target.window().fully())
    eyes.close(raise_ex=True)
