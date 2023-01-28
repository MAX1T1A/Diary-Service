from sqlalchemy.orm import Session
from models.models import User
from models.schemas import UserIn
from core.hashing import Hash


def create(request: UserIn, db: Session):
    new_user = User(
        name=request.name,
        email=request.email,
        password=Hash().bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
