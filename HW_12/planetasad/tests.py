import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import *
from pages.testing_data_login import *
from pages.login_page import LoginPage


@pytest.fixture()
def browser():
    driver.get(base_url)
    driver.implicitly_wait(3)
    yield driver


@pytest.mark.parametrize('sign_in_email_inp, sign_in_pwd_inp', data_login(test_cases))
def test_message_page(browser, sign_in_email_inp, sign_in_pwd_inp):
    login_page = LoginPage(browser)
    login_page.login(sign_in_email_inp, sign_in_pwd_inp)
    try:
        customer_sign_out_btn = (By.XPATH, '/html/body/div[1]/div[2]/div/ul/li[3]/a')
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(customer_sign_out_btn))
        not_found = False
    except:
        not_found = True
    assert not_found
