"""
Plik z definicjami page objectu z metodami umożliwiającymi stworzenie nowego konta.

Tutaj klik w "my account".
"""
from selenium.webdriver.common.keys import Keys

from locators import locators


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver

        # my account page elements - do nich przypisujemy zmienne z pliku z lokatorami (rejestracja i login):
        self.username_input = locators.MyAccountPage.username_input
        self.password_input = locators.MyAccountPage.password_input
        self.reg_email_input = locators.MyAccountPage.reg_email_input
        self.reg_password_input = locators.MyAccountPage.reg_password_input
        self.logout_link = locators.MyAccountPage.logout_link
        self.error_msg = locators.MyAccountPage.error_msg

    # metoda otwierająca stronę My Account:
    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    # metoda umożliwiająca logowanie do konta:
    def log_in(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)

    # metoda tworząca konto:
    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.reg_password_input).send_keys(Keys.ENTER)

    # info o stanie page objectu:
    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    # pobieramy info błędu:
    def get_error_msg(self):
        return self.driver.find_element(*self.error_msg).text

"""
Dla argumentu self dodano gwiazdkę dla metody find_element, ponieważ argument to krotka.
Krotka zostanie dziek itemu rozpakowana i oba elementy znajdujące się w krotce, zostaną przypisane
w wywołaniu metody.
"""