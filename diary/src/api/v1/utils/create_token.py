from datetime import datetime, timedelta

import jwt
from core.config import settings


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.jwt_token.active_time)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.jwt_token.secret_key, settings.jwt_token.algorithm
    )
    return encoded_jwt
