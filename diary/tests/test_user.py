import pytest


@pytest.mark.parametrize("test_input, expected", [
    ({"name": "Vasya", "email": "asyaqwe@example.com", "password": "12345678", "password2": "12345678"}, 201),
    ({"name": "Senya12313", "email": "rqrqrqrqr@example.com", "password": "seven-eleven", "password2": "seven-eleven"}, 201),
    ({"name": "qwrqwrq", "email": "qwcgbbACC@example.com", "password": "stringst", "password2": "stringst"}, 201)
])
def test_user_register(test_input, expected, client):
    response = client.post("api/v1/register", json=test_input)
    assert response.json() == expected
