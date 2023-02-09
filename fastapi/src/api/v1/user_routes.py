from fastapi import APIRouter
from models.schemas import UserInSchemas, Login, UserSchemas
from services.user_services import UserServices

router = APIRouter()


@router.post("/register")
async def create(request: UserInSchemas):
    return await UserServices().create_user(name=request.name, email=request.email, password=request.password)


@router.post("/login")
async def login(request: Login):
    return await UserServices().login_user(request)
