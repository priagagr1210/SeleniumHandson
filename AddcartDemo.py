
# AddcartDemo.py
# Automated script to log in, add an item to cart, and complete checkout on saucedemo.com using Selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the SauceDemo login page
driver.get("https://www.saucedemo.com/")

# Set implicit wait for elements to load
driver.implicitly_wait(50)

# Log in to the website
username = driver.find_element("xpath", "//*[@id='user-name']")
username.send_keys("standard_user")
time.sleep(2)  # Wait for input to register

password = driver.find_element("xpath", "//*[@id='password']")
password.send_keys("secret_sauce")
time.sleep(2)

# Click the login button
driver.find_element("xpath", "//*[@id='login-button']").click()
time.sleep(2)

# Add backpack to cart
driver.find_element("xpath", "//*[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(2)

# Go to cart
driver.find_element("xpath", "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()
time.sleep(2)

# Click checkout
driver.find_element("xpath", "//*[@id='checkout']").click()
time.sleep(2)

# Enter checkout details
name = driver.find_element("xpath", "//*[@id='first-name']")
name.send_keys("Priyanka")
time.sleep(2)

lastname = driver.find_element("xpath", "//*[@id='last-name']")
lastname.send_keys("Agrawal")
time.sleep(2)

pin_code = driver.find_element("xpath", "//*[@id='postal-code']")
pin_code.send_keys("580004")
time.sleep(2)

# Continue to next step
driver.find_element("xpath", "//*[@id='continue']").click()
time.sleep(2)

# Finish the purchase
driver.find_element("xpath", "//*[@id='finish']").click()
time.sleep(2)

# Close the browser
driver.quit()