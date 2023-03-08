# import pytest
# from dictionary import headers, CORRECT_DIARY_DATA
#
#
# class TestDiaryRoutes:
#     def test_get_list_diaries(self, client):
#         response = client.get("api/v1/diary", headers=headers)
#
#         assert response.status_code == 200
#         assert response.json() == []
#
#     def test_add_diary(self, client):
#         response = client.post("api/v1/diary", json={"name": "berupor"}, headers=headers)
#
#         assert response.json() == 201
