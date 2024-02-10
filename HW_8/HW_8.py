from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture
def find_button():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_find_button_if_user_selected(find_button):
    user_select_dropdown_menu = Select(find_button.find_element(By.ID, "userSelect"))
    user_select_dropdown_menu.select_by_visible_text("Albus Dumbledore")
    selected_customer = user_select_dropdown_menu.first_selected_option.text
    assert selected_customer == "Albus Dumbledore"
    button = find_button.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/button")
    if button.is_displayed():
        name_screenshot = 'Кнопка Login отображается' + '.png'
        find_button.save_screenshot(name_screenshot)
        print(f'\nКнопка "Login" отображается')
    else:
        name_screenshot = 'Кнопка Login не отображается' + '.png'
        find_button.save_screenshot(name_screenshot)
        print(f'\nКнопка "Login" не отображается')


def test_find_button_if_user_not_selected(find_button):
    user_select_dropdown_menu = Select(find_button.find_element(By.ID, "userSelect"))
    user_select_dropdown_menu.select_by_visible_text("---Your Name---")
    selected_customer = user_select_dropdown_menu.first_selected_option.text
    assert selected_customer == "---Your Name---"
    button = find_button.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/button")
    if button.is_displayed():
        name_screenshot = 'Кнопка Login отображается' + '.png'
        find_button.save_screenshot(name_screenshot)
        print(f'\nКнопка "Login" отображается')
    else:
        name_screenshot = 'Кнопка Login не отображается' + '.png'
        find_button.save_screenshot(name_screenshot)
        print(f'\nКнопка "Login" не отображается')
