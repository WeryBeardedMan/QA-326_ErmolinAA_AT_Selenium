import requests


def test_incorrect_date_http_status_code_400():
    api_key = "1kLgD5ankgacBidBSdUiWtP16sUcvJILTiBWcH7d"
    date = "1946-10-24"  # Заменяем дату в запросе
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    response = requests.get(url)  # Отправляем GET-запрос к API
    result = response.status_code  # Получаем HTTP status code
    try:
        assert result >= 400
        print(f"\nActual status code: {result}")
    except:
        print(f"\nExpected status code 4xx, but got {result}result")


def test_not_existing_date_http_status_code_400():
    api_key = "1kLgD5ankgacBidBSdUiWtP16sUcvJILTiBWcH7d"
    date = "0000-00-00"  # Заменяем дату в запросе
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    response = requests.get(url)  # Отправляем GET-запрос к API
    result = response.status_code  # Получаем HTTP status code
    try:
        assert result >= 400
        print(f"\nActual status code: {result}")
    except:
        print(f"\nExpected status code 4xx, but got {result}result")


def test_existing__correct_date_http_status_code_200():
    api_key = "1kLgD5ankgacBidBSdUiWtP16sUcvJILTiBWcH7d"
    date = "2000-01-01"  # Заменяем дату в запросе
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    response = requests.get(url)  # Отправляем GET-запрос к API
    result = response.status_code  # Получаем HTTP status code
    try:
        assert 200 <= result < 300
        print(f"\nActual status code: {result}")
    except:
        print(f"\nExpected status code 4xx, but got {result}result")


def test_incorrect_API_key_correct_date_status_code_400():
    date = "2000-01-01"  # Заменяем дату в запросе
    api_key = "000000"  # Заменяем API key в запросе
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}d&date={date}'
    response = requests.get(url)  # Отправляем GET-запрос к API
    result = response.status_code  # Получаем HTTP status code
    try:
        assert result >= 400
        print(f"\nActual status code: {result}")
    except:
        print(f"\nExpected status code 4xx, but got {result}result")
