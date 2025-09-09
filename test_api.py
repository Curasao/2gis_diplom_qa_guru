import pytest

import requests

class TestAuth:

    def test_auth(self, base_url:str):
        response = requests.post(
            url="https://regions-test.2gis.com/v1/auth/tokens",
            allow_redirects=False, timeout=10,
            verify=False
        )
        assert response.status_code == 200
        assert response.cookies.get("token") is not None

    def test_token_expires(self, session: requests.Session, base_url: str):
        """токен истекает через 2000мс"""
        # получаем токен
        response = session.post("https://regions-test.2gis.com/v1/auth/tokens")
        assert response.status_code == 200
        token = response.cookies.get("token")
        assert token

        # ждём 3 секунды (чуть больше 2000мс)
        time.sleep(3)

        # пробуем использовать истекший токен
        headers = {"Cookie": f"token={token}"}
        data = {"title": "test", "lat": 55.0, "lon": 82.0}

        response = session.post(
            url = "https://regions-test.2gis.com/v1/auth/tokens"/v1/favorites",
            data=data,
            headers=headers
        )


