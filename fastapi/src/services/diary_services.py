from fastapi import HTTPException, status
from models.models import Diary
from models.schemas import DiaryBase, DiaryGet
from services.base_services import BaseService


class DiaryServices(BaseService):
    _model = Diary

    def get_diary(self, author: int) -> DiaryGet:
        return self.get_many(user_id=author)

    def create_diary(self, request: DiaryBase, author: int) -> Diary:
        return self.create(name=request.name, user_id=author)

    def update_diary(self, request: DiaryBase, **kwargs) -> int:
        diary = self._session.query(self._model).filter_by(**kwargs).first()
        if not diary:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist")
        self.update_name(diary, request)
        return status.HTTP_200_OK

    def delete_diary(self, **kwargs) -> int:
        diary = self._session.query(self._model).filter_by(**kwargs).first()
        if not diary:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist")
        self.delete(diary)
        return status.HTTP_200_OK
