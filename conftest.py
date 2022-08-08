import pytest  # Импортируем библиотеку Pytest
from selenium import webdriver # Импорт драйвера из Селениум
from webdriver_manager.chrome import ChromeDriverManager #Импортируем вебрайвер менеджер из библиотеки (чтобы вручную его не сетапать евритайм)


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
