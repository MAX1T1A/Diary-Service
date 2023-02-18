from core.hashing import Hash
from models.models import User
from services.base_services import BaseService


class UserServices(BaseService):
    _model = User

    @property
    def model(self) -> _model:
        return self._model


user_service: UserServices = UserServices()
hasher: Hash = Hash()


async def get_user_service() -> UserServices:
    return user_service


async def get_hasher() -> Hash:
    return hasher
