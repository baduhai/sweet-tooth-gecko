import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get("https://www.coingecko.com/account/candy?locale=en")


if "TIMEOUT" in os.environ:
    timeout = int(os.environ.get("TIMEOUT"))
    print("Set page timout to " + os.environ.get("TIMEOUT") + " seconds.")
else:
    timeout = 5
    print("Timeout variable not set, using default(5 seconds).")


if os.environ.get("GOTIFY") == "true":
    def gotify_notify(msg):
        print("Sending notification with message: " + msg)
        gotify_url = os.environ.get("GOTIFY_ADDRESS") + "/message?token=" + os.environ.get("GOTIFY_TOKEN")
        resp = requests.post(gotify_url, json={
            "message": msg,
            "priority": 5,
            "title": "Sweet Tooth Gecko"
        })
else:
    def gotify_notify(msg):
        print("Gotify notifications disabled")

try:
    driver.get('https://www.coingecko.com/account/candy?locale=en')
    print("Site access successful.")
except BaseException:
    message = "Error: Could not access https://www.coingecko.com/account/candy?locale=en."
    print(message)
    gotify_notify(message)
    exit(1001)

try:
    driver.find_element_by_id("user_email").send_keys(os.environ.get("USEREMAIL"))
    driver.find_element_by_id("user_password").send_keys(os.environ.get("PASSWORD"))
    driver.find_element_by_id("user_password").submit();
    print("Login successful.")
except BaseException:
    message = "Error: Could not login."
    print(message)
    gotify_notify(message)
    exit(1002)

try:
    timoutelement = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.unobtrusive-flash-message-wrapper.unobtrusive-flash-notice")))
    print("Candy page loaded")
except TimeoutException:
    message = "Error: Loading took too long."
    print(message)
    gotify_notify(message)
    exit()

# try:
#     candybalance = driver.find_element_by_css_selector("div.font-weight-bold:nth-child(4)")
#     print("Current candy balance: " + candybalance.text + ".")
# except BaseException:
#     print("Could not find current candy balance, continuing.")

try:
    driver.find_element_by_css_selector("input.btn.btn-primary.col-12.collect-candy-button").click()
    message = "Cadies successfully collected."
    print(message)
    gotify_notify(message)
except NoSuchElementException:
    driver.find_element_by_css_selector("div.btn.bg-secondary.col-12.text-sm.text-white.collect-candy-button")
    message = "No candies available for collection."
    print(message)
    gotify_notify(message)
    exit()
except:
    message = "Could not find button to get new candy."
    print(message)
    gotify_notify(message)
    exit(1002)

# Couldn't figure out how to get new balance.
# try:
#     time.sleep(1)
#     newcandybalance = driver.find_element_by_css_selector("div.font-weight-bold:nth-child(4)")
#     newcandy = newcandybalance - candybalance
#     print("Got " + newcandy + " new candies! New candy balance: " + newcandybalance)
# except:
#     print("Could not find new candy balance")
#     exit(1002)

