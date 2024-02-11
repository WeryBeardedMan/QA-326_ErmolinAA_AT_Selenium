from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://webtucre.ru/testovaya-stranicza-4/")
    driver.implicitly_wait(5)
    yield driver


def test_name_input_field(driver):
    try:
        name_input_field_text = driver.find_element(By.XPATH, "//*[@id='post-867']/div/div/div/section[3]/div/div[2]/div/section/div[2]/div/div/div/div/form/div/div[1]/label").get_attribute("innerHTML")
        print(f'name_input_field_text: {name_input_field_text}')
        assert name_input_field_text == 'Ваше имя'
        print('Название поля для ввода имени не содержит ошибок')
    except NoSuchElementException:
        print("Элементы не найдены")  # оставил просто для наглядности


def test_name_input_field_placeholder(driver):
    try:
        name_input_field = driver.find_element(By.ID, 'form-field-name')
        name_input_field_placeholder = name_input_field.get_attribute('placeholder')
        print(f'name_input_field_placeholder: {name_input_field_placeholder}')
        assert name_input_field_placeholder == 'Ваше имя'
        print('placeholder поля для ввода имени не содержит ошибок')
    except NoSuchElementException:
        print("Элементы не найдены")  # оставил просто для наглядности


def test_email_input_field(driver):
    try:
        email_input_field_text = driver.find_element(By.XPATH, "//*[@id='post-867']/div/div/div/section[3]/div/div[2]/div/section/div[2]/div/div/div/div/form/div/div[2]/label").get_attribute("innerHTML")
        print(f'name_input_field_text: {email_input_field_text}')
        assert email_input_field_text == 'Ваше Email'
        print('Название поля для ввода Email не содержит ошибок')
    except NoSuchElementException:
        print("Элементы не найдены")  # оставил просто для наглядности


def test_email_input_field_placeholder(driver):
    try:
        email_input_field = driver.find_element(By.ID, 'form-field-email')
        email_input_field_placeholder = email_input_field.get_attribute('placeholder')
        print(f'name_input_field_placeholder: {email_input_field_placeholder}')
        assert email_input_field_placeholder == 'petrov@yandex.ru'
        print('placeholder поля для ввода Email не содержит ошибок')
    except NoSuchElementException:
        print("Элементы не найдены")  # оставил просто для наглядности


def test_message_input_field(driver):
    try:
        message_input_field_text = driver.find_element(By.XPATH, "//*[@id='post-867']/div/div/div/section[3]/div/div[2]/div/section/div[2]/div/div/div/div/form/div/div[3]/label").get_attribute("innerHTML")
        print(f'name_input_field_text: {message_input_field_text}')
        assert message_input_field_text == 'Ваше сообщение'
        print('Название поля для ввода сообщения не содержит ошибок')
    except NoSuchElementException:
        print("Элементы не найдены")  # оставил просто для наглядности


def test_message_input_field_placeholder(driver):
    try:
        message_input_field = driver.find_element(By.ID, 'form-field-message')
        message_input_field_placeholder = message_input_field.get_attribute('placeholder')
        print(f'name_input_field_placeholder: {message_input_field_placeholder}')
        assert message_input_field_placeholder == 'Заказ прошу доставить по адресу:'
        print('placeholder поля для ввода сообщения не содержит ошибок')
    except NoSuchElementException:
        print("Элементы не найдены")  # оставил просто для наглядности
