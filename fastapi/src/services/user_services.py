from core.hashing import Hash
from models.models import User
from services.base_services import BaseService


class UserServices(BaseService):
    _model = User


user_service: UserServices = UserServices()


def get_user_service() -> UserServices:
    return user_service

