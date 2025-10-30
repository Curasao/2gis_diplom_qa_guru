
import requests

import time

import allure

from api.conftest import auth_headers


class TestAuth:
    def test_auth(self, base_url:str):
        with allure.step("Тестируем создание токена"):
            response = requests.post(
                url=f"{base_url}/v1/auth/tokens",
                allow_redirects=False, timeout=10,
                verify=False
            )
            print(f"Создание токена: {response.status_code}")
            assert response.status_code == 200
            assert response.cookies.get("token") is not None

    def test_token_expires(self, session: requests.Session, base_url: str):
        with allure.step("Истечение токена"):
            # получаем токен
            response = session.post(f"{base_url}/v1/auth/tokens")
            assert response.status_code == 200
            token = response.cookies.get("token")
            assert token

            # ждём 3 секунды (чуть больше 2000мс)
            time.sleep(3)

            # пробуем использовать истекший токен
            headers = {"Cookie": f"token={token}"}
            data = {"title": "test", "lat": 55.0, "lon": 82.0}

            response = session.post(
                f"{base_url}/v1/favorites",
                data=data,
                headers=headers
            )
            print(f"Истечение токена: {response.status_code}")
            assert response.status_code == 401

class Test_create_Place:
    def test_create_place_invalid_data(self, session: requests.Session, base_url: str, invalid_payloads, auth_headers):
        with allure.step("Создание избранного места с невалидными данными"):
            response = session.post(
                f"{base_url}/v1/favorites",
                data=invalid_payloads[0],
                headers=auth_headers
            )
            print(f"Создание места с невалидными данными: {response.status_code}")
            assert response.status_code == 400

    def test_create_place_valid_data(self, session: requests.Session, base_url: str, valid_favorite_data, auth_headers):
        with allure.step("Создание избранного места с валидными данными"):
            response = session.post(
                f"{base_url}/v1/favorites",
                data=valid_favorite_data,
                headers=auth_headers
            )
            print(f"Создание с валидными данными: {response.status_code}")
            if response.status_code == 200:
                print(f"ID созданного места: {response.json()['id']}")

    def test_create_place_valid_name(self, session: requests.Session, base_url: str, valid_favorite_data, auth_headers):
        with allure.step("Создание избранного места с валидным именем"):
            response = session.post(
                f"{base_url}/v1/favorites",
                data=valid_favorite_data,
                headers=auth_headers
            )
            print(f"Создание с валидным именем: {response.status_code}")
            assert response.status_code == 200

    def test_create_place_valid_color(self, session: requests.Session, base_url: str, valid_favorite_data, auth_headers,valid_color):
        with allure.step("Создание избранного места с валидным цветом"):
            response = session.post(
                f"{base_url}/v1/favorites",
                data=valid_favorite_data,
                headers=auth_headers
            )
            print(f"Создание с валидным цветом: {response.status_code}")
            assert response.status_code == 200

    def test_create_place_invalid_color(self, session: requests.Session, base_url: str, invalid_payloads, auth_headers,valid_color):
        with allure.step("Создание избранного места с невалидным цветом"):
            response = session.post(
                f"{base_url}/v1/favorites",
                data=invalid_payloads[0],
                headers=auth_headers
            )
            print(f"Создание с невалидным цветом: {response.status_code}")
            assert response.status_code == 400


    def test_create_place_null_color(self, session: requests.Session, base_url: str, invalid_color, auth_headers,valid_color):
        with allure.step("Создание избранного места с невалидным цветом null"):
            response = session.post(
                f"{base_url}/v1/favorites",
                data=invalid_color,
                headers=auth_headers
            )
            print(f"Создание с невалидным цветом null: {response.status_code}")
            assert response.status_code == 400
