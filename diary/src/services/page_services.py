from models.models import Page
from services.base_services import BaseService


class PageServices(BaseService):
    _model = Page


page_service: PageServices = PageServices()


def get_page_service() -> PageServices:
    return page_service
