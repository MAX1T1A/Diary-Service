from sqlalchemy import Column, Integer, String, ForeignKey

from db.postgres import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), nullable=False)
    name = Column(String(120), nullable=False)
    password = Column(String(50), nullable=False)


class Diary(Base):
    __tablename__ = 'diary'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class UserDiary(Base):
    __tablename__ = 'user_diary'

    user_id = Column(Integer, ForeignKey(User.id), index=True)
    diary_id = Column(Integer, ForeignKey(Diary.id), index=True)


class Page(Base):
    __tablename__ = 'user_diary'

    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    body = Column(String)


class DiaryPage(Base):
    __tablename__ = 'diary_page'

    diary_id = Column(Integer, ForeignKey(Diary.id), index=True)
    page_id = Column(Integer, ForeignKey(Page.id), index=True)
