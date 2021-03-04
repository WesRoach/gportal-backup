import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor="https://hub:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME,
)

driver.get("https://www.g-portal.com/int/server/valheim/400137/system/backup")

# Navigate Authentication
driver.find_element_by_id("login").send_keys(os.environ["GPORTAL_EMAIL"])
driver.find_element_by_id("password").send_keys(os.environ["GPORTAL_PASSWORD"])
driver.find_element_by_class_name("submit").click()

# Just print the contents
driver.page_source

# Create Backup
# driver.find_element_by_id("make_backup").click()
# driver.find_element_by_css_selector(
#     "body > div.dialog.dialog--size-default > div > div > div > div > button:nth-child(2)"
# ).click()
