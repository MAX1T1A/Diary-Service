import pytest
from test_data.diary_data import CORRECT_DIARY_DATA, TESTING_PAGE, headers


class TestDiaryPageRoutes:
    @pytest.mark.parametrize("test_input, expected", CORRECT_DIARY_DATA[0])
    def test_add_diary(self, test_input, expected, client):
        response = client.post("api/v1/diary", json=test_input, headers=headers)

        assert response.status_code == 200
        assert response.json() == expected

    def test_get_list_diaries(self, client):
        response = client.get("api/v1/diary", headers=headers)

        assert response.status_code == 200
        assert response.json() == CORRECT_DIARY_DATA[1]

    def test_update_diary(self, client):
        response = client.put(
            "api/v1/diary/1", json={"name": "max1t1a"}, headers=headers
        )

        assert response.status_code == 200
        assert response.json() == 204

    def test_delete_diary(self, client):
        response = client.delete("api/v1/diary/1", headers=headers)

        assert response.status_code == 200
        assert response.json() == 204

    def test_is_not_diary(self, client):
        response_put = client.put(
            "api/v1/diary/10", json={"name": "max1t1a"}, headers=headers
        )
        response_delete = client.delete("api/v1/diary/10", headers=headers)

        assert response_put.status_code == 404
        assert response_put.json() == {"detail": "This diary doesn't exist."}

        assert response_delete.status_code == 404
        assert response_delete.json() == {"detail": "This diary doesn't exist."}

    def test_add_page(self, client):
        response = client.post(
            "api/v1/diary/2/page", json=TESTING_PAGE[0], headers=headers
        )

        assert response.status_code == 200
        assert response.json() == 201

    def test_get_list_pages(self, client):
        response = client.get("api/v1/diary/2/page", headers=headers)

        assert response.status_code == 200
        assert response.json() == TESTING_PAGE[1]

    def test_update(self, client):
        response = client.put(
            "api/v1/diary/2/page/1",
            json={"name": "berupor_style", "body": "good test max1t1a"},
            headers=headers,
        )

        assert response.status_code == 200
        assert response.json() == 204

    def test_delete(self, client):
        response = client.delete("api/v1/diary/2/page/1", headers=headers)

        assert response.status_code == 200
        assert response.json() == 204

    def test_is_not_page(self, client):
        response_put = client.put(
            "api/v1/diary/10/page/1",
            json={"name": "max1t1a", "body": "qwerty_small"},
            headers=headers,
        )
        response_delete = client.delete("api/v1/diary/10/page/1", headers=headers)

        assert response_put.status_code == 404
        assert response_put.json() == {"detail": "This diary doesn't exist."}

        assert response_delete.status_code == 404
        assert response_delete.json() == {"detail": "This diary doesn't exist."}
