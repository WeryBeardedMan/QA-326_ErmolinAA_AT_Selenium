from pages.locators import *


class LoginPage:
    # Атрибуты
    def __init__(self, driver):
        self.button_first_sign_in = driver.find_element(*button_first_sign_in)
        self.sign_in_email_inp = driver.find_element(*sign_in_email_inp)
        self.sign_in_pwd_inp = driver.find_element(*sign_in_pwd_inp)
        self.button_final_sign_in = driver.find_element(*button_final_sign_in)

    # Методы
    def login(self, sign_in_email_inp='', sign_in_pwd_inp=''):
        self.button_first_sign_in.click()
        self.sign_in_email_inp.send_keys(sign_in_email_inp)
        self.sign_in_pwd_inp.send_keys(sign_in_pwd_inp)
        self.button_final_sign_in.click()
