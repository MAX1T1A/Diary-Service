from sqlalchemy import Column, Integer, String, ForeignKey, Text, MetaData
from sqlalchemy.orm import relationship
from db.postgres import Base

metadata = MetaData()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)


class Diary(Base):
    __tablename__ = "diaries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    name = Column(String)

    user = relationship("User", back_populates="diary")


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)
    diary_id = Column(Integer, ForeignKey(Diary.id))
    name = Column(String)
    body = Column(Text)

    diary = relationship("Diary", back_populates="page")
