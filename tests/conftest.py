import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.tables_page import TablesPage
from pages.text_box_page import TextBoxPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

