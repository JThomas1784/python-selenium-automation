from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Locate element:
from selenium.webdriver.common.by import By

from sample_script import driver

# Locate by ID:
driver.find_element(By.ID, value:'twotabsearchtextbox')
driver. find_element(By.ID, value:'nav-logo-sprites')
# By Xpath, using 1 attribute
driver.find_element(By.XPATH, value: "//img[@alt='Shop Studio Pro headphones']")
driver.find_element(By.XPATH, value: "//input [@name='field-keywords'])|
driver.find_element(By.XPATH, value: "//input [@placeholder= 'Search Amazon']")
# By Xpath, multiple attributes
driver.find_element(By.XPATH,
value: "//a[@class= 'nav-a ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers' and @tabindex='0']")
# By Xpath, text:
driver.find_element(By.XPATH, value: "//a[text(='Best Sellers']")
driver.find_element(By.XPATH, value: *W/altext()="Best Sellers"]')
# By Xpath, text and attributes:
driver.find_element(By.XPATH, value: "//a[text()='Best Sellers' and @class='nav-a ']")
# By attributes or text only, any tag
driver.find_element(By.XPATH, value: