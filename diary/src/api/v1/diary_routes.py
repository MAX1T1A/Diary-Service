from typing import List

from api.v1.utils.auth_bearer import JWTBearer
from fastapi import APIRouter, Depends, HTTPException, status
from models.models import User
from models.schemas import DiaryGet, DiaryUniversal
from services.diary_services import DiaryServices
from services.providers import stub_diary_service

router = APIRouter()


@router.get("/diary")
def get_list_diaries(
    author: User = Depends(JWTBearer()),
    diary_service: DiaryServices = Depends(stub_diary_service),
) -> List[DiaryGet]:
    return [
        DiaryGet(**diary.to_dict()) for diary in diary_service.find_many(user_id=author)
    ]


@router.post("/diary")
def add_diary(
    request: DiaryUniversal,
    author: User = Depends(JWTBearer()),
    diary_service: DiaryServices = Depends(stub_diary_service),
) -> int:
    diary_service.create(name=request.name, user_id=author)
    return status.HTTP_201_CREATED


@router.put("/diary/{diary_id}")
def update_diary(
    diary_id: int,
    request: DiaryUniversal,
    author: User = Depends(JWTBearer()),
    diary_service: DiaryServices = Depends(stub_diary_service),
) -> int:
    diary = diary_service.find_one(id=diary_id, user_id=author)
    if not diary:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist."
        )
    diary_service.update(request, diary)
    return status.HTTP_204_NO_CONTENT


@router.delete("/diary/{diary_id}")
def delete_diary(
    diary_id: int,
    author: User = Depends(JWTBearer()),
    diary_service: DiaryServices = Depends(stub_diary_service),
) -> int:
    diary = diary_service.find_one(id=diary_id, user_id=author)
    if not diary:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist."
        )
    diary_service.delete(diary)
    return status.HTTP_204_NO_CONTENT
