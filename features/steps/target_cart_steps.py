from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then, use_fixture

# Amazon Locators
Top Logo: [role="img"][aria-label="Amazon"]
Create Account: h1.a-spacing-small
Your Name: input#ap_customer_name
Mobile Number or Email: input#ap_email
Password: input#ap_password
Re-enter password: input#ap_password_check
Create your account/Continue: input#continue
Conditions of use: a[href="/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&amp;nodeId=508088"]
Privacy Notice: a[href="/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&amp;nodeId=468496"]
Bottom Sign-In: a[href="/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&prevRID=E0NX75YZBSSHMCK0NCPE&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"]

@given("I am on the Target homepage")
def open_target(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com/")

@when("I click on the cart icon")
def click_cart_icon(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, ".header__cart-icon")
    cart_icon.click()

@then("I see the message 'Your cart is empty'")
def verify_empty_cart(context):
    empty_message = context.driver.find_element(By.XPATH, "//div[contains(text(), 'Your cart is empty')]")
    assert empty_message.is_displayed()
    assert empty_message.text == "Your cart is empty"

@then("I close the browser")
def close_browser(context):
    context.driver.quit()