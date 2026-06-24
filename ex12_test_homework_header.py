import requests


class TestHomeworkHeader:
    def test_homework_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")

        print(response.headers)

        assert "x-secret-homework-header" in response.headers, \
            "Заголовок 'x-secret-homework-header' отсутствует в ответе"
        assert response.headers["x-secret-homework-header"] == "Some secret value", \
            f"Неожиданное значение заголовка: {response.headers['x-secret-homework-header']}"
