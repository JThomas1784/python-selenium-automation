from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.target.com/")
sleep(60)

sign_in_button_top = driver.find_element(By.XPATH, "//button[@aria-label='Sign in']")
sign_in_button_top.click()

side_nav_sign_in = driver.find_element(By.XPATH, "//a[@id='account']")
side_nav_sign_in.click()

sign_in_text = driver.find_element(By.XPATH, "//h1[text()='Sign into your Target account']")

sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")

driver.quit()