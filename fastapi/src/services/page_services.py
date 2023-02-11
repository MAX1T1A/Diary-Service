from fastapi import HTTPException, status
from models.schemas import PageGet, PageCreate
from services.base_services import BaseService
from models.models import Page


class PageServices(BaseService):
    _model = Page

    def get_page(self, diary_id: int) -> PageGet:
        return self.get_many(diary_id=diary_id)

    def create_page(self, request: PageCreate, diary_id: int) -> Page:
        return self.create(name=request.name, body=request.body, diary_id=diary_id)

    def update_page(self, request: PageCreate, **kwargs) -> int:
        page = self._session.query(self._model).filter_by(**kwargs).first()
        if not page:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This page doesn't exist")
        self.update(page, request, 2)
        return status.HTTP_200_OK

    def delete_page(self, **kwargs) -> int:
        page = self._session.query(self._model).filter_by(**kwargs).first()
        if not page:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This page doesn't exist")
        self.delete(page)
        return status.HTTP_200_OK
