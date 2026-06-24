import requests

def test_homework_header():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    print(response.headers)
    assert "x-secret-homework-header" in response.headers, "Ожидаемый заголовок 'x-secret-homework-header' не найден в ответе"
    assert response.headers[
               "x-secret-homework-header"] == "Some secret value", "Значение заголовка не соответствует ожидаемому"
