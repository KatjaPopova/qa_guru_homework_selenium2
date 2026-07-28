import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By


# Позитивные тесты:
# 1. Все поля формы заполнены кириллицей:
def test_all_fields_filled_with_cyrillic_letters(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example" in result_box.text
    assert "Москва" in result_box.text
    assert "Санкт-Петербург" in result_box.text


# 2. Все поля формы заполнены латиницей:
def test_all_fields_filled_with_latin_letters(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Olga Ivanova")
    text_box_page.find_element(By.ID, "userEmail").send_keys("olgaivanova@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Moscow")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Saint-Petersburg")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Olga Ivanova" in result_box.text
    assert "olgaivanova@example.com" in result_box.text
    assert "Moscow" in result_box.text
    assert "Saint-Petersburg" in result_box.text


# 3. В поле Full Name указано полное ФИО (с отчеством):
def test_name_surname_patronymic_in_name_field(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петров Петр Петрович")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петров Петр Петрович" in result_box.text
    assert "petrov@example" in result_box.text
    assert "Москва" in result_box.text
    assert "Санкт-Петербург" in result_box.text


# 4. В поле Full Name указано короткое значение:
def test_short_name(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Ян")
    text_box_page.find_element(By.ID, "userEmail").send_keys("yan@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Сочи")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Ян" in result_box.text
    assert "yan@example.com" in result_box.text
    assert "Москва" in result_box.text
    assert "Сочи" in result_box.text


# 5. В поле Full Name указано длинное значение:
def test_long_name(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Константинопольская Апполинария Максимилиановна")
    text_box_page.find_element(By.ID, "userEmail").send_keys("yan@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Сочи")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Константинопольская Апполинария Максимилиановна" in result_box.text
    assert "yan@example.com" in result_box.text
    assert "Москва" in result_box.text
    assert "Сочи" in result_box.text


# 6. В поле Full Name присутствует дефис:
def test_hyphen_in_name_field(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Иван Мамин-Сибиряк")
    text_box_page.find_element(By.ID, "userEmail").send_keys("yan@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Сочи")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Иван Мамин-Сибиряк" in result_box.text
    assert "yan@example.com" in result_box.text
    assert "Москва" in result_box.text
    assert "Сочи" in result_box.text


# 7. В поле Email буквы разных регистров:
def test_email_in_mixed_case(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("PetrovPetr@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Казань")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Москва")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "PetrovPetr@example.com" in result_box.text
    assert "Казань" in result_box.text
    assert "Москва" in result_box.text


# 8. В поле Email присутствуют цифры:
def test_numbers_in_email(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov1985@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Тюмень")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Омск")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov1985@example.com" in result_box.text
    assert "Тюмень"
    assert "Омск"


# 9. Значения полей current_address и permanent_address совпадают:
def test_current_address_equals_permanent_address(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrovpetya@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Москва")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrovpetya@example.com" in result_box.text
    assert "Москва" in result_box.text
    assert "Москва" in result_box.text


# 10. В поле current_address указан адрес с городом, улицей, номерами дома и квартиры:
def test_current_address_with_city_street_house_flat(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва, ул. Тверская, дом 5, кв. 23")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Краснодар")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Москва, ул. Тверская, дом 5, кв. 23" in result_box.text
    assert "Краснодар" in result_box.text


# 11. В поле current_address указан адрес с городом, улицей, номерами дома, строения и квартиры:
def test_current_address_with_city_street_house_building_flat(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва, ул. Тверская, дом 5, корп. 1, кв. 23")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Краснодар")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Москва, ул. Тверская, дом 5, корп. 1, кв. 23" in result_box.text
    assert "Краснодар" in result_box.text


# 12. В поле current_address указан адрес с городом и улицей:
def test_current_address_only_city_and_street(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва, ул. Тверская")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Краснодар")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Москва, ул. Тверская" in result_box.text
    assert "Краснодар" in result_box.text


# 13. В поле current_address указан длинный адрес:
def test_long_current_address(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")

    long_current_address: str = ("192177, г. Санкт-Петербург, Внутригородское "
                                 "муниципальное образование Санкт-Петербурга "
                                 "муниципальный округ Рыбацкое, Шлиссельбургский проспект, "
                                 "дом 24, корпус 2, строение 1, подвальный этаж, "
                                 "помещение 3-Н, комната 14, офис 5")

    text_box_page.find_element(By.ID, "currentAddress").send_keys(long_current_address)
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Краснодар")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert long_current_address in result_box.text
    assert "Краснодар" in result_box.text


# 14. В поле current_address указан короткий адрес:
def test_short_current_address(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Уфа")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Краснодар")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Уфа" in result_box.text
    assert "Краснодар" in result_box.text


# 15. В поле current_address присутствуют спецсимволы:
def test_current_address_contains_symbols(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("г. Санкт-Петербург, Невский пр., д. 15/2, кв. №34")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Пермь")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "г. Санкт-Петербург, Невский пр., д. 15/2, кв. №34" in result_box.text
    assert "Пермь" in result_box.text


# 16. В поле permanent_address указан адрес с городом, улицей, номерами дома и квартиры:
def test_permanent_address_with_city_street_house_flat(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Казань")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Москва, ул. Тверская, дом 5, кв. 23")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Казань" in result_box.text
    assert "Москва, ул. Тверская, дом 5, кв. 23" in result_box.text


# 17. В поле permanent_address указан адрес с городом, улицей, номерами дома, строения и квартиры:
def test_permanent_address_with_city_street_house_building_flat(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Казань")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Москва, ул. Тверская, дом 5, корп. 1, кв. 23")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Казань" in result_box.text
    assert "Москва, ул. Тверская, дом 5, корп. 1, кв. 23" in result_box.text


# 18. В поле permanent_address указан адрес с городом и улицей:
def test_permanent_address_only_city_and_street(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Казань")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Москва, ул. Тверская")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Казань" in result_box.text
    assert "Москва, ул. Тверская" in result_box.text


# 19. В поле permanent_address указан длинный адрес:
def test_long_permanent_address(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Казань")

    long_permanent_address: str = ("192177, г. Санкт-Петербург, Внутригородское "
                                   "муниципальное образование Санкт-Петербурга "
                                   "муниципальный округ Рыбацкое, Шлиссельбургский проспект, "
                                   "дом 24, корпус 2, строение 1, подвальный этаж, "
                                   "помещение 3-Н, комната 14, офис 5")

    text_box_page.find_element(By.ID, "permanentAddress").send_keys(long_permanent_address)

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Казань" in result_box.text
    assert long_permanent_address in result_box.text


# 20. В поле permanent_address указан короткий адрес:
def test_short_permanent_address(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Мурманск")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Уфа")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Мурманск" in result_box.text
    assert "Уфа" in result_box.text


# 21. В поле permanent_address присутствуют спецсимволы:
def test_permanent_address_contains_symbols(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Пермь")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("г. Санкт-Петербург, Невский пр., д. 15/2, кв. №34")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Петр Петров" in result_box.text
    assert "petrov@example.com" in result_box.text
    assert "Пермь" in result_box.text
    assert "г. Санкт-Петербург, Невский пр., д. 15/2, кв. №34" in result_box.text


# 22. Форма отправляется, если все поля формы пустые (позитивная проверка, так как все поля формы необязательные):
# Падает из-за опечатки на странице ("permananet" вместо "permanent")
def test_text_form_sent_if_all_fields_empty(text_box_page):
    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    result_box = text_box_page.find_element(By.ID, "output")

    assert result_box.is_displayed()
    assert "Name:\n" in result_box.text
    assert "Email:\n" in result_box.text
    assert "Current Address :\n" in result_box.text
    assert "Permanent Address :\n" in result_box.text


# Негативные тесты:
# 1. Email без символа @:
def test_email_with_no_mail_symbol(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrovexample.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Мурманск")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Уфа")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    error_text = text_box_page.find_element(By.ID, "userEmail").get_attribute("validationMessage")

    assert error_text != ""


# 2. В поле Email используется кириллица:
def test_long_email(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("петров@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    error_text = text_box_page.find_element(By.ID, "userEmail").get_attribute("validationMessage")

    assert error_text != ""


# 3. В поле Email два символа @@:
def test_email_with_two_mail_symbols(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    error_text = text_box_page.find_element(By.ID, "userEmail").get_attribute("validationMessage")

    assert error_text != ""


# 4. В поле Email спецсимволы:
def test_special_symbols_in_email_field(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov[]@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    error_text = text_box_page.find_element(By.ID, "userEmail").get_attribute("validationMessage")

    assert error_text != ""


# 5. В поле Email пробел:
def test_space_in_email_field(text_box_page):
    text_box_page.find_element(By.ID, "userName").send_keys("Петр Петров")
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov @example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    error_text = text_box_page.find_element(By.ID, "userEmail").get_attribute("validationMessage")

    assert error_text != ""


# 6. HTML-иньекция (тест падает, так как html выполняется):
def test_html_injection(text_box_page):
    payload = "<div id='hack'>Hello</div>"

    text_box_page.find_element(By.ID, "userName").send_keys(payload)
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    html_elements = text_box_page.find_elements(By.ID, "hack")

    assert len(html_elements) == 0


# 7. XSS-иньекция:
def test_xss_injection(text_box_page):
    payload = "<script>alert(1)</script>"

    text_box_page.find_element(By.ID, "userName").send_keys(payload)
    text_box_page.find_element(By.ID, "userEmail").send_keys("petrov@example.com")
    text_box_page.find_element(By.ID, "currentAddress").send_keys("Москва")
    text_box_page.find_element(By.ID, "permanentAddress").send_keys("Санкт-Петербург")

    text_box_page.find_element(By.ID, "submit").click()

    time.sleep(3)

    try:
        alert = text_box_page.switch_to.alert
        assert False, f"XSS работает! Alert: {alert.text}"
    except NoAlertPresentException:
        pass
