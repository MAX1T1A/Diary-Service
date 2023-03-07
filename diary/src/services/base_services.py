from typing import List

from database.postgres import Session


class BaseService:
    _model = None

    def __init__(self, session):
        self._session = session

    def find_many(self, **kwargs) -> List[_model]:
        return self._session.query(self._model).filter_by(**kwargs).all()

    def find_one(self, **kwargs) -> _model:
        return self._session.query(self._model).filter_by(**kwargs).first()

    def create(self, **kwargs) -> None:
        instance = self._model(**kwargs)
        self._session.add(instance)
        self._session.commit()
        return self._session.refresh(instance)

    def update(self, request, instance) -> None:
        for key, value in request.__dict__.items():
            setattr(instance, key, value)
        return self._session.commit()

    def delete(self, instance: _model) -> None:
        self._session.delete(instance)
        return self._session.commit()
