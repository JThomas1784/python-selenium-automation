from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Open Chrome in incognito mode (headless is optional)
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# options.add_argument("--headless")  # To run in headless mode (no browser window)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to Target
driver.get("https://www.target.com/")

# Click sign in button (top right corner)
sign_in_button_top = driver.find_element(By.XPATH, "//button[@aria-label='Sign in']")
sign_in_button_top.click()

# Click sign in from side navigation
side_nav_sign_in = driver.find_element(By.XPATH, "//a[@id='account']")
side_nav_sign_in.click()

# Verify sign-in page title (optional)
assert driver.title == "Target : Sign In"

# Verify "Sign into your Target account" text
sign_in_text = driver.find_element(By.XPATH, "//h1[text()='Sign into your Target account']")

# Verify Sign In button presence
sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# Print verification message
print("Test Passed: Sign in page loaded successfully.")
print(f"  - Sign in text found: {sign_in_text.text}")
# No assertion for button presence as requested

# Close the browser
driver.quit()