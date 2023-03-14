from core.config import settings

headers = {"Authorization": f"Bearer {settings.jwt_token.token}"}


# Diary values __________________________________________________________________________________________
CORRECT_DIARY_DATA = [
    (
        {"name": "berupor"},
        201
    ),
    (
        {"name": "valdimir"},
        201
    ),
    (
        {"name": "husan"},
        201
    ),
]

TESTING_DIARY = [
    {'name': 'berupor', 'id': 1},
    {'name': 'valdimir', 'id': 2},
    {'name': 'husan', 'id': 3}
]

TESTING_PAGE = [
    {"name": "max1t1a_style", "body": "hello world!"},
    [{'body': 'hello world!', 'id': 1, 'name': 'max1t1a_style'}]
]

