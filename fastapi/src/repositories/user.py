from typing import List, Optional

from core.security import hash_password
from db.postgres import user_table
from models.user import User, UserIn
from repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = user_table.select().limit(limit).offset(skip)
        # noinspection PyTypeChecker
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, pk: int) -> Optional[User]:
        query = user_table.select().where(user_table.c.id == pk)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, u: UserIn) -> User:
        user = User(
            name=u.name,
            email=u.email,
            password=hash_password(u.password),
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = user_table.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update(self, pk: int, u: UserIn) -> User:
        user = User(
            id=pk,
            name=u.name,
            email=u.email,
            password=hash_password(u.password),
        )
        values = {**user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = user_table.update().where(user_table.c.id == pk).values(**values)
        await self.database.execute(query)
        return user

    async def get_by_email(self, email: str) -> Optional[User]:
        query = user_table.select().where(user_table.c.email == email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)
