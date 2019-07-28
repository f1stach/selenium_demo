"""
Współdzielenie metody setup() -> metoda 2.
Metoda setup zawarta jest w specjalnym pliku conftest.
Nie tworzymy tutaj klasy.
"""

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from page_object_pattern.utils.driver_factory import DriverFactory


# tworzymy setupową metodę, w niej tworzymy przeglądarkę i zamykamy ją
# dodatkowo jako argument przyjmuje parametr request, do którego w ciele przypisujemy
# zmienną driver - po to aby funkcje testowe nie pluły się o brak drivera.

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # nie chcemy na sztywno wywoływać Chrome, tylko dac wybór więc korzystamy z DriverFacotry:
    # driver = DriverFactory.get_driver("chrome")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    # dodajemy opcję wykonywania prtscr gdy test zostanie zakonczony niepowodzeniem
    # najpierw sprawdzamy ile mamy testów, które zakonczyły się niepowodzeniem:

    before_failed = request.session.testsfailed

    yield
    driver.quit()
