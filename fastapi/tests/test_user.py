from test_core.conftest import BaseTestSettings


class TestUser(BaseTestSettings):
    json = {
      "name": "string",
      "email": "string@example.com",
      "password": "stringst",
      "password2": "stringst"
    }

    def test_user_register(self, test_client):
        response = test_client.post("api/v1/register", json=self.json)
        assert response.status_code == 200
