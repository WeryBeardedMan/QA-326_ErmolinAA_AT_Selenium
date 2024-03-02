from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Настройка опций для headless режима
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
base_url = 'https://www.planetsad.ru/'
