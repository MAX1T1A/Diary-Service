from typing import Dict
from fastapi import HTTPException, status
from models.models import User
from models.schemas import Login
from core.hashing import Hash
from api.v1.utils.create_token import create_token
from services.base_services import BaseService


class UserServices(BaseService):
    _model = User

    async def create_user(self, **kwargs) -> User:
        for c in self._session.query(self._model):
            if c.email == kwargs.get("email"):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="This user is already registered")
        return self.create(name=kwargs.get("name"), email=kwargs.get("email"), password=Hash().bcrypt(kwargs.get("password")))

    async def login_user(self, request: Login) -> Dict[str, str]:
        user = self._session.query(User).filter(User.email == request.email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This user is not registered")

        if not Hash().verify(user.password, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Password or login was entered incorrectly")

        access_token = create_token(data={"user_id": user.id})
        return {"access_token": access_token, "token_type": "bearer"}
