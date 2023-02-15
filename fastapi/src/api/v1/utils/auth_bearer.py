import time
from typing import List
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
import jwt
from core.config import settings


async def decode_and_verify_jwt(token: str, secret_key: str, algorithms: List[str]) -> dict:
    try:
        decoded_token = await jwt.decode(token, secret_key, algorithms=algorithms)
        if decoded_token["exp"] >= time.time():
            return decoded_token
        else:
            raise HTTPException(status_code=403, detail="Expired token.")
    except jwt.exceptions.DecodeError:
        raise HTTPException(status_code=403, detail="Invalid authorization code.")
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Invalid token or expired token.")


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Authentication token invalid  scheme.")
            user_id = decode_and_verify_jwt(
                credentials.credentials,
                settings.jwt_token.secret_key,
                [settings.jwt_token.algorithm],
            ).__getattribute__("user_id")

            return user_id
