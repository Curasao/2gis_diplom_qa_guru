
import requests

import time

import allure

from conftest import auth_headers


class TestAuth:


    def test_auth(self, base_url:str):
        response = requests.post(
            url="https://regions-test.2gis.com/v1/auth/tokens",
            allow_redirects=False, timeout=10,
            verify=False
        )
        print(f"Создание токена: {response.status_code}")
        assert response.status_code == 200
        assert response.cookies.get("token") is not None


    def test_token_expires(self,session: requests.Session, base_url: str):
        """токен истекает через 2000мс"""
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
            f"{base_url}/v1/auth/tokens",
            data=data,
            headers=headers
        )
        print(f"Истечение токена: {response.status_code}")
        assert response.status_code == 401



class Test_create_Place:
    def test_create_place(self,session: requests.Session, base_url: str):
        response = session.post(f"{base_url}/v1/favorites")
        print(f"Создание места: {response.status_code}")
        assert response.status_code == 200

    def test_create_place_valid_data(self,session: requests.Session, base_url: str,valid_favorite_data, valid_coordinates,auth_headers):
        valid_data = {'title': 'Театр', 'lat': 55.028254, 'lon': 82.918501}
        response = requests.post(f"{base_url}/v1/favorites", data=valid_coordinates, headers=auth_headers)
        print(f"Создание с валидными данными: {response.status_code}")
        if response.status_code == 200:
            print(f"ID созданного места: {response.json()['id']}")





