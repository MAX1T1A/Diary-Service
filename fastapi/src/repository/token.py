from datetime import datetime, timedelta
from jose import jwt, JWTError
from core.config import settings
from models.schemas import TokenData


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.jwt_token.active_time)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_token.secret_key, settings.jwt_token.algorithm)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.jwt_token.secret_key, algorithms=[settings.jwt_token.algorithm])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        TokenData(id=user_id)
    except JWTError:
        raise credentials_exception
