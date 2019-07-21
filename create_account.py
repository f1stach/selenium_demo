import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# najpierw test faila tworzenia konta czyli dodanie takiego, które juz istnieje:
def test_create_account_failed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys("testujemy@python.org")
    driver.find_element(By.ID, "reg_password").send_keys("python123!@#")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)

    # powyzszy kod zapewnił, że nie ma mozliwości zarejestrowania tego samego usera.
    # tworzymy asercje potwierdzającą, że tak jest
    msg = " An account is already registered with your email address. Please log in."
    assert msg in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text


# drugi test - możemy się zarejestrowac:
def test_create_account_passed():
    # generujemy adres email aby utworzyć nowe konto usera:
    email = str(random.randint(0, 10000)) + "testujemy@python.org"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("python123!@#")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)

    # aby zbadać czy faktycznie zalogowano się, musimy to sprawdzić za pomocą asercji
    # można np. sprawdzić czy po zalogowaniu link Logout jest widoczny (pojawia się w panelu usera po zalogowaniu)
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
