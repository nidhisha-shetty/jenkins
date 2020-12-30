from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
username = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
build_name = os.getenv("BROWSERSTACK_BUILD_NAME")
# browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
# browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")

caps = {
 'os': 'Windows',
 'os_version': '10',
 'browser': 'chrome',
 'browser_version': 'latest',
 'name': 'BStack-[Jenkins] Sample Test', # test name
 'build': build_name, # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
 # 'browserstack.local': browserstack_local,
 # 'browserstack.localIdentifier': browserstack_local_identifier,
 'browserstack.user': username,
 'browserstack.key': access_key
}

driver = webdriver.Remote(
    command_executor='https://hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=caps)

# desired_cap = {
#  'browserName': 'iPhone',
#  'device': 'iPhone 11',
#  'realMobile': 'true',
#  'os_version': '14.0',
#  'name': 'BStack-[Python] Sample Test', # test name
#  # 'build': 'BStack Build Number 1' # CI/CD job or build name
# }
# driver = webdriver.Remote(
#     command_executor='https://nidhishashetty1:wsyX9aQHCR44pEu7ujzN@hub-cloud.browserstack.com/wd/hub',
#     desired_capabilities=desired_cap)
driver.get("https://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
##test
##test2
#test3


elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
# Setting the status of test as 'passed' or 'failed' based on the condition; if title of the web page starts with 'BrowserStack'
if (driver.title[:12]=="BrowserStack"):
	driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
else:
	driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
driver.quit() 
