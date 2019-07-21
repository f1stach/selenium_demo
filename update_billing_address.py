# plik, w którym testujemy zmianę danych adresowych usera
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# tworzymy nowe konto i wchodzimy do zakładki z danymi adresowymi:
def test_update_billing_address():

    # generujemy adres email aby utworzyć nowe konto usera:
    email = str(random.randint(0, 10000)) + "testujemy@python.org"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("python123!@#")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)

    # klikamy na pole Adresses:
    driver.find_element(By.LINK_TEXT, "Addresses").click()

    # klikamy na przycisk Edit i edytujemy pola tekstowe:
    driver.find_element(By.LINK_TEXT, "Edit").click()
    driver.find_element(By.ID, "billing_first_name").send_keys("John")
    driver.find_element(By.ID, "billing_last_name").send_keys("Doe")

    # kraj wybieramy z listy rozwijanej więc korzystamy z klasy Select do wykonania testu:
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Poland")

    driver.find_element(By.ID, "billing_address_1").send_keys("Kwiatowa 1")
    driver.find_element(By.ID, "billing_postcode").send_keys("00-001")
    driver.find_element(By.ID, "billing_city").send_keys("Warsaw")
    driver.find_element(By.ID, "billing_phone").send_keys("111111111")

    # powyzsze komendy wykonane bez problemu, ale też bez weryfikacji

    # zapisujemy formularz:
    driver.find_element(By.XPATH, "//button[@value='Save address']").click()

    # sprawdzamy czy po zapisaniu adresu odpowiednia wiadomość została wyswietlona:
    assert "Address changed successfully" in driver.find_element(By.XPATH, "//div[@class='woocommerce-message']").text
