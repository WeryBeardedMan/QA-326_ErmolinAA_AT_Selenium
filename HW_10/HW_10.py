import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    current_url = "https://webtucre.ru/testovaya-stranicza-4/"
    driver.get(current_url)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver


def data_message(data):
    for i, l in enumerate(data):
        data[i] = (l['username'], l['email'], l['message'], l['expected_url'])
    return data


test_cases = [
    {
        "username": " ",
        "email": "petrov@yandex.ru",
        "message": " ",
        "expected_url": "https://webtucre.ru/testovaya-stranicza-4/"
    },
    {
        "username": "Name",
        "email": "petrov@yandex.ru",
        "message": "1",
        "expected_url": "https://webtucre.ru/spasibo-2/"
    },
]


@pytest.mark.parametrize('username, email, message, expected_url', data_message(test_cases))
def test_message_page(driver, username, email, message, expected_url):
    username_inp = driver.find_element(By.ID, 'form-field-name')
    username_inp.send_keys(username)
    email_inp = driver.find_element(By.ID, 'form-field-email')
    email_inp.send_keys(email)
    message_inp = driver.find_element(By.ID, 'form-field-message')
    message_inp.send_keys(message)
    button_submit = driver.find_element(By.CSS_SELECTOR, 'button.elementor-button')
    button_submit.click()
    wait = WebDriverWait(driver, 10)
    wait.until(ec.url_to_be(expected_url))
    current_url = driver.current_url
    assert current_url == expected_url
    print(f'\ncurrent_url = {current_url}')
