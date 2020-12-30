from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired_cap = {
 'browserName': 'iPhone',
 'device': 'iPhone 11',
 'realMobile': 'true',
 'os_version': '14.0',
 'name': 'BStack-[Python] Sample Test', # test name
 'build': 'BStack Build Number 1' # CI/CD job or build name
}
driver = webdriver.Remote(
    command_executor='https://nidhishashetty1:wsyX9aQHCR44pEu7ujzN@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
driver.get("https://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
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
