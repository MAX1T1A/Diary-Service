from typing import List

from api.v1.utils.auth_bearer import JWTBearer
from fastapi import APIRouter, Depends, HTTPException, status
from models.models import User
from models.schemas import PageGet, PageUniversal
from services.diary_services import DiaryServices
from services.page_services import PageServices
from services.providers import stub_diary_service, stub_page_service

router = APIRouter()


@router.get("/diary/{diary_id}/page")
def get_list_pages(
    diary_id: int,
    page_service: PageServices = Depends(stub_page_service),
    author: User = Depends(JWTBearer()),
    diary_service: DiaryServices = Depends(stub_diary_service),
) -> List[PageGet]:
    diary = diary_service.find_one(id=diary_id, user_id=author)
    if not diary:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist."
        )
    return [
        PageGet(**page.to_dict()) for page in page_service.find_many(diary_id=diary_id)
    ]


@router.post("/diary/{diary_id}/page")
def add_page(
    diary_id: int,
    request: PageUniversal,
    page_service: PageServices = Depends(stub_page_service),
    author: User = Depends(JWTBearer()),
    diary_service: DiaryServices = Depends(stub_diary_service),
) -> int:
    diary = diary_service.find_one(id=diary_id, user_id=author)
    if not diary:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist."
        )
    page_service.create(name=request.name, body=request.body, diary_id=diary_id)
    return status.HTTP_201_CREATED


@router.put("/diary/{diary_id}/page/{page_id}")
def update_page(
    diary_id: int,
    page_id: int,
    request: PageUniversal,
    page_service: PageServices = Depends(stub_page_service),
    author: User = Depends(JWTBearer()),
    diary_service: DiaryServices = Depends(stub_diary_service),
) -> int:
    diary = diary_service.find_one(id=diary_id, user_id=author)
    if not diary:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist."
        )
    page = page_service.find_one(id=page_id, diary_id=diary_id)
    if not page:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This page doesn't exist."
        )
    page_service.update(request, page)
    return status.HTTP_204_NO_CONTENT


@router.delete("/diary/{diary_id}/page/{page_id}")
def delete_page(
    diary_id: int,
    page_id: int,
    page_service: PageServices = Depends(stub_page_service),
    author: User = Depends(JWTBearer()),
    diary_service: DiaryServices = Depends(stub_diary_service),
) -> int:
    diary = diary_service.find_one(id=diary_id, user_id=author)
    if not diary:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist."
        )
    page = page_service.find_one(id=page_id, diary_id=diary_id)
    if not page:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This page doesn't exist."
        )
    page_service.delete(page)
    return status.HTTP_204_NO_CONTENT
