"""
Plik z klasą i lokatorami.
"""
from selenium.webdriver.common.by import By


# klasa dla lokatorów update_billing_address:

class BillingAddressLocators:

    # lokatory przeniesione z update_billing_address
    # lokatory definiujemy w postaci krotek:

    # update: lokatory dot. email i password przeniesione do my_account_page
    # pozostałe lokatory skopiowane do billing_address_page

    # reg_email_input = (By.ID, "reg_email")
    # reg_password_input = (By.ID, "reg_password")
    addresses_link = (By.LINK_TEXT, "Addresses")
    edit_link = (By.LINK_TEXT, "Edit")
    first_name_input = (By.ID, "billing_first_name")
    last_name_input = (By.ID, "billing_last_name")
    country_select = (By.ID, "billing_country")
    address_input = (By.ID, "billing_address_1")
    postcode_input = (By.ID, "billing_postcode")
    city_input = (By.ID, "billing_city")
    phone_input = (By.ID, "billing_phone")
    save_address_button = (By.XPATH, "//button[@value='Save address']")
    message_div = (By.XPATH, "//div[@class='woocommerce-message']")


# klasa dla lokatorów login_test i create_account:

class MyAccountPage:

    # login page:
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")

    # create account page:
    reg_email_input = (By.ID, "reg_email")
    reg_password_input = (By.ID, "reg_password")

    my_account_link = (By.XPATH, "//li[@id='menu-item-22']//a")

    error_msg = (By.XPATH, "//ul[@class='woocommerce-error']//li")

    logout_link = (By.LINK_TEXT, "Logout")
