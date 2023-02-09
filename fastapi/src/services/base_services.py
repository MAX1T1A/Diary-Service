from db.postgres import Session


class BaseService:
    _model = None

    def __init__(self):
        self._session = Session()

    def get_many(self, **kwargs):
        return self._session.query(self._model).filter_by(**kwargs).all()

    def create(self, **kwargs):
        instance = self._model(**kwargs)
        self._session.add(instance)
        self._session.commit()
        self._session.refresh(instance)
        return instance

    def update_name(self, instance, request):
        instance.name = request.name
        return self._session.commit()

    def update_body(self, instance, request):
        instance.body = request.body
        return self._session.commit()

    def delete(self, instance):
        self._session.delete(instance)
        return self._session.commit()
