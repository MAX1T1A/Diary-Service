from models.models import Diary
from services.base_services import BaseService


class DiaryServices(BaseService):
    _model = Diary


diary_service: DiaryServices = DiaryServices()


def get_diary_service() -> DiaryServices:
    return diary_service



