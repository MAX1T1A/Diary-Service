from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.postgres import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    diary_id = Column(Integer, ForeignKey("diary.id"))

    diary = relationship("Diary", back_populates="user")


class Diary(Base):
    __tablename__ = "diaries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    page_id = Column(Integer, ForeignKey("page.id"))

    user = relationship("User", back_populates="diary")
    page = relationship("Page", back_populates="diary")


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    body = Column(Text)
    diary_id = Column(Integer, ForeignKey("diary.id"))

    diary = relationship("Diary", back_populates="page")
