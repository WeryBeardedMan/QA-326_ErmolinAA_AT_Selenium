from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import datetime

chrome_options = webdriver.ChromeOptions()  # чтобы увидеть, что происходит в браузере - закомментировать строки 8 и 9
chrome_options.add_argument("--headless")  # headless - аргумент позволяет проводить тест автономно - не открывая окна
driver = webdriver.Chrome(options=chrome_options)  # а также убрать аргумент options=chrome_options
driver.maximize_window()
driver.get("https://calcus.ru/kalkulyator-ipoteki")
try:
    width = 1920
    height = 2200
    driver.set_window_size(width, height)
    driver.implicitly_wait(5)
    property_values = driver.find_element(By.NAME, "cost")
    initial_payment = driver.find_element(By.NAME, "start_sum")
    loan_period = driver.find_element(By.NAME, "period")
    interest_rate = driver.find_element(By.NAME, "percent")
    submit_button = driver.find_element(By.XPATH, "//input[@value='Рассчитать']")
    test_case = {"property_values": "2300000",
                 "initial_payment": "1500000",
                 "loan_period": "6",
                 "interest_rate": "12.3"}
    property_values.click()
    property_values.send_keys(test_case['property_values'])
    initial_payment.click()
    initial_payment.send_keys(test_case['initial_payment'])
    loan_period.click()
    loan_period.send_keys(test_case['loan_period'])
    interest_rate.click()
    interest_rate.send_keys(test_case['interest_rate'])
    submit_button.click()
    page_body = driver.find_element(By.TAG_NAME, "body")
    current_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
    name_screenshot = 'full_page_screenshot' + current_date + '.png'
    wait = WebDriverWait(driver, timeout=10)
    wait.until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading-overlay']")))
    page_body.screenshot(name_screenshot)
    print('Все элементы найдены!')  # оставил просто для наглядности
except NoSuchElementException:
    print("нет ни одного элемента")  # оставил просто для наглядности
