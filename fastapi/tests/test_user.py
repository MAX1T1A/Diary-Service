import pytest

json = {
    "name": "string",
    "email": "qweqwe@example.com",
    "password": "stringst",
    "password2": "stringst"
}


def test_user_register(test_client):
    response = test_client.post("api/v1/register", json=json)
    assert response.status_code == 200
