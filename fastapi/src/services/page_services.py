from models.models import Page
from services.base_services import BaseService


class PageServices(BaseService):
    _model = Page

    @property
    def model(self) -> _model:
        return self._model


page_service: PageServices = PageServices()


def get_page_service() -> PageServices:
    return page_service
