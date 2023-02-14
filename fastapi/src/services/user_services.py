from typing import Dict
from fastapi import HTTPException, status
from models.models import User
from models.schemas import Login
from core.hashing import Hash
from api.v1.utils.create_token import create_token
from services.base_services import BaseService


class UserServices(BaseService):
    _model = User

    @property
    def model(self) -> _model:
        return self._model


user_service: UserServices = UserServices()
hasher: Hash = Hash()


def get_user_service() -> UserServices:
    return user_service


def get_hasher() -> Hash:
    return hasher
