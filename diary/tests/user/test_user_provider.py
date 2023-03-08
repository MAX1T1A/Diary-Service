import pytest
from dictionary import CORRECT_REGISTER_DATA, CORRECT_LOGIN_DATA, WRONG_REGISTER_DATA, WRONG_LOGIN_DATA


class TestUserRoutes:
    @pytest.mark.parametrize("test_input, expected", CORRECT_REGISTER_DATA)
    def test_user_register(self, test_input, expected, client):
        response = client.post("api/v1/register", json=test_input)

        assert response.status_code == 200
        assert response.json() == expected

    @pytest.mark.parametrize("test_input, expected", CORRECT_LOGIN_DATA)
    def test_user_login(self, test_input,  expected, client):
        response = client.post("api/v1/login", json=test_input)

        print(response.json())
        assert response.status_code == expected
        assert type(response.json()) == dict
        assert type(response.json()["access_token"]) == str
        assert len(response.json()["access_token"]) == 121
        assert response.json()["token_type"] == "bearer"

    @pytest.mark.parametrize("test_input, expected", WRONG_REGISTER_DATA)
    def test_wrong_user_register(self, test_input, expected, client):
        response = client.post("api/v1/register", json=test_input)

        assert response.status_code == expected

    @pytest.mark.parametrize("test_input, expected", WRONG_LOGIN_DATA)
    def test_wrong_user_login(self, test_input, expected, client):
        response = client.post("api/v1/login", json=test_input)

        assert response.status_code == expected
