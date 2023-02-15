from typing import Dict
from models.models import Diary
from services.base_services import BaseService


class DiaryServices(BaseService):
    _model = Diary

    @property
    def model(self) -> _model:
        return self._model


diary_service: DiaryServices = DiaryServices()


async def get_diary_service() -> DiaryServices:
    return diary_service



