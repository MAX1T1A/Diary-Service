from fastapi import APIRouter, HTTPException, status, Depends
from jose import JWTError, jwt

from core.config import settings
from db.postgres import Session, get_db
from models.models import User
from services.create_jwt import create_access_token

router = APIRouter(tags=['JWT'])


# the endpoint to get the token
@router.get("/get_token")
async def get_token(db: Session = Depends(get_db)):
    user = db.query(User)
    # user_id = user.user_id


    print(f'user from query = {user} end Query')

    data = {
        "info": "secret information",
        "from": "GFG",
        # "user_id":
    }
    token = create_access_token(data=data)
    return {"token": token}


# the endpoint to verify the token
@router.post("/verify_token")
async def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.token.access_token, algorithms=[settings.token.token_type])
        print(payload)
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
