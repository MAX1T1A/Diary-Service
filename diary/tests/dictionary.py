from core.config import settings

headers = {"Authorization": f"Bearer {settings.jwt_token.token}"}


# User values __________________________________________________________________________________________
CORRECT_REGISTER_DATA = [
    (
        {"name": "Vasya", "email": "vasya@gmail.com", "password": "12345678",
         "password2": "12345678"},
        201
    ),
    (
        {"name": "Maksud", "email": "maksud_loh_05@gmail.com", "password": "stringst",
         "password2": "stringst"},
        201
    ),
    (
        {"name": "Dasha", "email": "nedam_tebe_loh@gmail.com", "password": "qwer1234",
         "password2": "qwer1234"},
        201
    ),
]

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

# -----------------------
CORRECT_LOGIN_DATA = [
    (
        {"email": "vasya@gmail.com", "password": "12345678"},
        200,
    ),
    (
        {"email": "maksud_loh_05@gmail.com", "password": "stringst"},
        200,
    ),
    (
        {"email": "nedam_tebe_loh@gmail.com", "password": "qwer1234"},
        200,
    ),
]
# -----------------------
WRONG_REGISTER_DATA = [
    (
        {"name": "Keesha", "email": "Keesha@", "password": "12345678",
         "password2": "12345678"},
        422,
    ),
    (
        {"name": "Maks", "email": "maks@gmail.com", "password": "123456122",
         "password2": "123456"},
        400,
    ),
    (
        {"name": "Gena", "email": "nedam_tebe_loh@gmail.com", "password": "123456789",
         "password2": "123456789"},
        401,
    )
]
# -----------------------
WRONG_LOGIN_DATA = [
    (
        {"email": "qqqqsds@gmail.com", "password": "qwwwqqwww"},
        404
    ),
    (
        {"email": "nedam_tebe_loh@gmail.com", "password": "22222222222222"},
        400
    ),
    (
        {"email": " ", "password": "22222222222222"},
        422
    ),
]


