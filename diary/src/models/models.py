from database.postgres import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(120), nullable=False, unique=True)
    name = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)
    diary_info = relationship("Diary", lazy="joined", back_populates="user_info")


class Diary(Base):
    __tablename__ = "diary"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), index=True)
    page_info = relationship(
        "Page", lazy="joined", back_populates="diary_info_for_page"
    )
    user_info = relationship("User", lazy="joined", back_populates="diary_info")

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Page(Base):
    __tablename__ = "page"

    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    body = Column(Text)
    diary_id = Column(Integer, ForeignKey(Diary.id), index=True)
    diary_info_for_page = relationship(
        "Diary", lazy="joined", back_populates="page_info"
    )

    def to_dict(self):
        return {"id": self.id, "name": self.name, "body": self.body}
