import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By


# Позитивные тесты:
# 1. Неудачная попытка залогиниться (не удалось найти успешный способ это сделать):
def test_unsuccessful_login(login_page):
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='login-input']").send_keys("Ekaterina")
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='password-input']").send_keys("123456")
    login_page.find_element(By.XPATH, "//button[text()='Login']").click()

    time.sleep(3)

    error = login_page.find_element(By.CSS_SELECTOR, "[data-testid='error-message']").text

    assert error == "Wrong login or password"


# 2. Проверка ввода текста в поля формы:
def test_input_fields(login_page):
    login = login_page.find_element(By.CSS_SELECTOR, "[data-testid='login-input']")
    password = login_page.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")

    login.send_keys("Ekaterina")
    password.send_keys("123456")

    time.sleep(3)

    assert login.get_attribute("value") == "Ekaterina"
    assert password.get_attribute("value") == "123456"


# 3. Проверка кнопки Login:
def test_button_login_enabled(login_page):
    button = login_page.find_element(By.XPATH, "//button[text()='Login']")

    time.sleep(3)

    assert button.is_enabled()


# Негативные тесты:
# 1. Корректный Login, некорректный Password
def test_invalid_password_valid_login(login_page):
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='login-input']").send_keys("Ekaterina")
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='password-input']").send_keys("invalid")
    login_page.find_element(By.XPATH, "//button[text()='Login']").click()

    time.sleep(3)

    error = login_page.find_element(By.CSS_SELECTOR, "[data-testid='error-message']").text

    assert error == "Wrong login or password"


# 2. Отправка формы с пустыми полями Login и Password:
def test_all_empty_fields(login_page):
    login_page.find_element(By.XPATH, "//button[text()='Login']").click()

    time.sleep(3)

    error = login_page.find_element(By.CSS_SELECTOR, "[data-testid='error-message']").text

    assert error == "Login and password are required (minimum 3 and 6 characters)"


# 3. Отправка формы с пустым полем Login:
def test_empty_field_login(login_page):
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='password-input']").send_keys("123456")
    login_page.find_element(By.XPATH, "//button[text()='Login']").click()

    time.sleep(3)

    error = login_page.find_element(By.CSS_SELECTOR, "[data-testid='error-message']").text

    assert error == "Login is required (minimum 3 characters)"


# 4. Отправка формы с пустым полем Password:
def test_empty_field_password(login_page):
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='login-input']").send_keys("Ekaterina")
    login_page.find_element(By.XPATH, "//button[text()='Login']").click()

    time.sleep(3)

    error = login_page.find_element(By.CSS_SELECTOR, "[data-testid='error-message']").text

    assert error == "Password is required (minimum 6 characters)"


# 5. Слишком короткий Login:
def test_too_short_login(login_page):
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='login-input']").send_keys("Hi")
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='password-input']").send_keys("123456")
    login_page.find_element(By.XPATH, "//button[text()='Login']").click()

    time.sleep(3)

    error = login_page.find_element(By.CSS_SELECTOR, "[data-testid='error-message']").text

    assert error == "Login must be at least 3 characters"


# 6. Слишком короткий Password:
def test_too_short_password(login_page):
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='login-input']").send_keys("Ekaterina")
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='password-input']").send_keys("123")
    login_page.find_element(By.XPATH, "//button[text()='Login']").click()

    time.sleep(3)

    error = login_page.find_element(By.CSS_SELECTOR, "[data-testid='error-message']").text

    assert error == "Password must be at least 6 characters"


# 7. SQL-инъекция:
def test_sql_injection_in_login_field(login_page):
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='login-input']").send_keys("' OR 1=1 --")
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='password-input']").send_keys("123456")
    login_page.find_element(By.XPATH, "//button[text()='Login']").click()

    time.sleep(3)

    error = login_page.find_element(By.CSS_SELECTOR, "[data-testid='error-message']")

    assert error.is_displayed()


# 8. XSS-инъекция:
def test_xss_injection_in_login_field(login_page):
    payload = "<script>alert('XSS')</script>"
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='login-input']").send_keys(payload)
    login_page.find_element(By.CSS_SELECTOR, "[data-testid='password-input']").send_keys("123456")
    login_page.find_element(By.XPATH, "//button[text()='Login']").click()

    time.sleep(3)

    try:
        login_page.switch_to.alert
        assert False, "XSS сработал!"
    except NoAlertPresentException:
        pass
