from selenium import webdriver  # подключаем webdriver
from selenium.webdriver.common.by import By  # подключаем поиск элементов
from selenium.webdriver.common.keys import Keys  # подключаем клавиши
import time

driver = webdriver.Chrome()
driver.maximize_window()  # разворачиваем окно браузера
driver.get("https://www.python.org")  # переходим по ссылке
elem = driver.find_element(By.NAME, 'q')  # ищем элемент (поиск)
elem.click()  # кликаем на найденный ранее элемент
elem.send_keys("while")  # вводим поисковый запрос в поле поиска, который нашли ранее
elem.send_keys(Keys.ENTER)  # нажатие клавиши Enter
driver.save_screenshot("HW_5_screenshot_1.png")  # делаем скриншот страницы
time.sleep(5)
elem = driver.find_element(By.NAME, 'q')  # ищем элемент (поиск)
elem.clear()
elem.send_keys("else")  # вводим поисковый запрос в поле поиска, который нашли ранее
elem.send_keys(Keys.ENTER)  # нажатие клавиши Enter
driver.save_screenshot("HW_5_screenshot_2.png")  # делаем второй скриншот страницы
time.sleep(5)
url = driver.current_url  # запрашиваем URL
print(url)
driver.back()  # перейти назад (нажатие кнопки назад в браузере)
time.sleep(1)
driver.forward()  # перейти вперед (нажатие кнопки вперед в браузере)
time.sleep(1)
driver.quit()  # метод quit закрывает браузер
