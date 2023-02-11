from typing import List
from fastapi import APIRouter, Depends
from api.v1.utils.auth_bearer import JWTBearer
from models.schemas import PageBase, PageGet, PageCreate
from models.models import Page
from services.page_services import PageServices

router = APIRouter()


@router.post("/diary/{diary_id}/page", response_model=PageCreate)
async def create(diary_id: int, request: PageCreate):
    return PageServices().create_page(request, diary_id)


@router.get("/diary/{diary_id}/page", response_model=List[PageGet])
def get_page(diary_id: int):
    return PageServices().get_page(diary_id=diary_id)


@router.put("/diary/{diary_id}/page/{page_id}", response_model=int)
def update_page(request: PageCreate, diary_id: int, page_id: int):
    return PageServices().update_page(request, id=page_id, diary_id=diary_id)


@router.delete("/diary/{diary_id}/page/{page_id}", response_model=int)
def delete(diary_id: int, page_id: int):
    return PageServices().delete_page(id=page_id, diary_id=diary_id)
