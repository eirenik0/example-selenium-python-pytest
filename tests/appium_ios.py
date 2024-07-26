import os
from appium import webdriver
# from appium.options.android import UiAutomator2Options
from applitools.selenium.eyes import Eyes

class HelloWorld:

    # Initialize the eyes SDK and set your private API key.
    eyes = Eyes()

    # Set the desired capapbilities, be sure to change the values accordingly
    # desired_caps = {}
    # desired_caps['platformName'] = 'iOS'
    # desired_caps['browserName'] ='Safari'
    # desired_caps['deviceName'] = 'iPhone 15'
    # desired_caps['platformVersion'] = '17.5'
    # desired_caps['automationName'] = 'XCUITest'

    # Open browser
    # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '17.5',  # Replace with your iOS version
        'deviceName': 'iPhone 15 Pro Max',  # Replace with your simulator name
        'udid': 'BA898BDF-2EEF-436D-AFA9-799855B2F9BE',
        # 'browserName': 'Safari',
        'app': '/Users/anand.bagmar/projects/applitools/getting-started-with-mobile-visualtesting/sampleApps/HelloWorldiOS.app',
        'automationName': 'XCUITest',
        'newCommandTimeout': 30000,
        'showXcodeLog': True,
        'fullReset': False
    }

    # Create the Appium driver instance
    # options = UiAutomator2Options()
    # options.load_capabilities(desired_caps)

    driver = webdriver.Remote(
        'http://localhost:4723/wd/hub',
        # options=options
        desired_capabilities=desired_caps
    )
    try:

        # Start the test.
        eyes.open(driver=driver, app_name='Hello World!', test_name='My first Appium web Python test!')

        # Navigate the browser to the "Hello World!" web-site.
        driver.get('https://applitools.com/helloworld')

        # Visual validation point #1.
        eyes.check_window('Hello!')

        # Click the "Click me!" button.
        # driver.find_element_by_tag_name('button').click()

        # Visual validation #2.
        eyes.check_window('Click!')

        # End the test.
        eyes.close()

    finally:

        # Close the browser.
        driver.quit()

        # If the test was aborted before eyes.Close was called, end the test as aborted.
        eyes.abort_if_not_closed()
