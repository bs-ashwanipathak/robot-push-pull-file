*** Settings ***
Library    AppiumLibrary
Library    glue.py

*** Test Cases ***
Test Wiki app
    Start Session
    IOSPUSH FILE
    Sleep   5
    IOSPULL FILE
    Sleep   5
    Close application

*** Keywords ***
Start Session
    Open application    https://BROWSERSTACK_USERNAME:ACCESS_KEY@hub-cloud.browserstack.com/wd/hub  
    ...  automationName=XCUITest
    ...  platformName=ios  
    ...  deviceName=iPhone 14
    ...  platformVersion=16.0 
    ...  app=bs://sample.app
