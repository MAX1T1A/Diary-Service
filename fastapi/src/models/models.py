from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from db.postgres import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), nullable=False)
    name = Column(String(120), nullable=False)
    password = Column(String(50), nullable=False)
    # registration_date = Column(DateTime)
    diary_name = relationship('Diary', lazy='joined', back_populates='user_name')


class Diary(Base):
    __tablename__ = 'diary'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), index=True)
    page_name = relationship('Page', lazy='joined', back_populates='diary')
    user_name = relationship('User', lazy='joined', back_populates='diary_name')



class Page(Base):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    body = Column(Text)
    diary_id = Column(Integer, ForeignKey(Diary.id), index=True)
    diary = relationship('Diary', lazy='joined', back_populates='page_name')


