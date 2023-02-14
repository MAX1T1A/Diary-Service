from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from api.v1.utils.auth_bearer import JWTBearer
from models.schemas import DiaryGet, DiaryUniversal
from models.models import User
from services.diary_services import DiaryServices, get_diary_service

router = APIRouter()


@router.get(path="/diary")
async def getting_list_diaries(author: User = Depends(JWTBearer()), diary_service: DiaryServices = Depends(get_diary_service)) -> List[DiaryGet]:
    return [DiaryGet(id=diary.id, name=diary.name) for diary in diary_service.get_many(user_id=author)]


@router.post(path="/diary")
async def adding_diary_database(request: DiaryUniversal, author: User = Depends(JWTBearer()), diary_service: DiaryServices = Depends(get_diary_service)) -> int:
    diary_service.create(name=request.name, user_id=author)
    return status.HTTP_201_CREATED


@router.put(path="/diary/{diary_id}")
async def update_diary_database(diary_id: int, request: DiaryUniversal, author: User = Depends(JWTBearer()), diary_service: DiaryServices = Depends(get_diary_service)) -> int:
    diary = diary_service.session.query(diary_service.model).filter_by(id=diary_id, user_id=author).first()
    if not diary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist.")
    diary_service.update(request, diary)
    return status.HTTP_204_NO_CONTENT


@router.delete(path="/diary/{diary_id}")
async def deleting_diary_database(diary_id: int, author: User = Depends(JWTBearer()), diary_service: DiaryServices = Depends(get_diary_service)) -> int:
    diary = diary_service.session.query(diary_service.model).filter_by(id=diary_id, user_id=author).first()
    if not diary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist.")
    diary_service.delete(diary)
    return status.HTTP_204_NO_CONTENT
