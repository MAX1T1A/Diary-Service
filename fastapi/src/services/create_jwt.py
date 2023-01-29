from jose import jwt
from datetime import datetime, timedelta

from core.config import settings


def create_access_token(data: dict):
    to_encode = data.copy()
    print(f'to_encode = {to_encode}')

    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.token.access_token, algorithm=settings.token.token_type)
    print(f'encode_jwt = {encoded_jwt}')
    return encoded_jwt
