from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from pages.my_account_page import MyAccountPage


# upgrade - dodajemy klasę i parametr self metodom oraz fixture odpalający metodę setup przed testami:
@pytest.mark.usefixtures("setup")
class TestLogIn:
    # metoda sprawdzająca poprawne zalogowanie się:
    def test_log_in_passed(self):

        # upgrade - przed odpaleniem testu definiujemy page object:
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("testujemy@python.org", "python123!@#")

        assert my_account_page.is_logout_link_displayed()

        # old version - before page object:

        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver.maximize_window()
        # # wait = WebDriverWait(driver, 10)
        # driver.get("http://seleniumdemo.com/")
        #
        # # My Account - definiujemy poszukiwanie elementów, ale uzywając ogólnej metody, której argumenty
        # # to technika lokalizowania elementów oraz parametr
        # driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
        #
        # # Metoda 1 - logowanie - podajemy login, haslo i klikamy na Login:
        # # driver.find_element(By.ID, "username").send_keys("testujemy@python.org")
        # # driver.find_element(By.ID, "password").send_keys("python123!@#")
        # # driver.find_element(By.NAME, "login").click()
        #
        # # Metoda 2 - logowanie - podajemy login, haslo, przesuwamy się nad przycisk przez JS i klikamy na Login:
        # # driver.find_element(By.ID, "username").send_keys("testujemy@python.org")
        # # driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID, "password"))
        # # driver.find_element(By.ID, "password").send_keys("python123!@#")
        # # driver.find_element(By.NAME, "login").click()
        #
        # # Metoda 3 - logowanie - podajemy login, haslo i naciskamy Enter:
        # driver.find_element(By.ID, "username").send_keys("testujemy@python.org")
        # driver.find_element(By.ID, "password").send_keys("python123!@#")
        # driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
        #
        # # aby zbadać czy faktycznie zalogowano się, musimy to sprawdzić za pomocą asercji
        # # można np. sprawdzić czy po zalogowaniu link Logout jest widoczny (pojawia się w panelu usera po zalogowaniu)
        # assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    # metoda sprawdzająca niepowodzenie podczas logowania:
    def test_log_in_failed(self):

        # upgrade - przed odpaleniem testu definiujemy page object:
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("testujemy@python11.org", "python123!@#")

        assert "ERROR: Incorrect username or password" in my_account_page.get_error_msg()

        # old version - before page object:

        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver.maximize_window()
        # # wait = WebDriverWait(driver, 10)
        # driver.get("http://seleniumdemo.com/")
        #
        # # My Account - definiujemy poszukiwanie elementów, ale uzywając ogólnej metody, której argumenty
        # # to technika lokalizowania elementów oraz  parametr
        # driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
        #
        # # Metoda 1 - logowanie - podajemy login, haslo i klikamy na Login:
        # # driver.find_element(By.ID, "username").send_keys("testujemy@python.org")
        # # driver.find_element(By.ID, "password").send_keys("python123!@#")
        # # driver.find_element(By.NAME, "login").click()
        #
        # # Metoda 2 - logowanie - podajemy login, haslo, przesuwamy się nad przycisk przez JS i klikamy na Login:
        # # driver.find_element(By.ID, "username").send_keys("testujemy@python.org")
        # # driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID, "password"))
        # # driver.find_element(By.ID, "password").send_keys("python123!@#")
        # # driver.find_element(By.NAME, "login").click()
        #
        # # Metoda 3 - logowanie - podajemy login, haslo i naciskamy Enter:
        # driver.find_element(By.ID, "username").send_keys("testujemy@python.org")
        # driver.find_element(By.ID, "password").send_keys("python123!@#abcd")
        # driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
        #
        # # aby zbadać czy faktycznie nastąpił błąd logowania, musimy to sprawdzić za pomocą asercji
        # # czyli sprawdzamy czy po wpisaniu danych wyswietla się komunikat o errorze logowania:
        # assert "ERROR: Incorrect username or password." in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
