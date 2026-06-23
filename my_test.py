import requests

def test_homework_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

    # разведка: смотрим, что прислал сервер нам
    for cookie in response.cookies:
        print(cookie.name, "=", cookie.value)

    # фиксируем поведение
    assert "HomeWork" in response.cookies, \
        "В ответе нет ожидаемой cookie"
    assert response.cookies["HomeWork"] == "hw_value", \
        f"Значение cookie не совпадает: {response.cookies['HomeWork']}"