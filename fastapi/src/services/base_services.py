from typing import List

from sqlalchemy import select, update

from db.postgres import Session


class BaseService:
    _model = None

    def __init__(self):
        self._session = Session()

    def get_many(self, **kwargs) -> List[_model]:
        return self._session.query(self._model).filter_by(**kwargs).all()

    def create(self, **kwargs) -> _model:
        instance = self._model(**kwargs)
        self._session.add(instance)
        self._session.commit()
        self._session.refresh(instance)
        return instance

    def update(self, request, instance) -> None:
        for key, value in request.__dict__.items():
            setattr(instance, key, value)
        return self._session.commit()

    def delete(self, instance: _model) -> None:
        self._session.delete(instance)
        return self._session.commit()

    @property
    def session(self) -> Session:
        return self._session
