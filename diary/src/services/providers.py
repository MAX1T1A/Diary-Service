from services.diary_services import DiaryServices
from services.page_services import PageServices
from services.user_services import UserServices
from sqlalchemy.orm import sessionmaker


# User Stub and Service ________________________________________________

def stub_user_service():
    raise NotImplementedError


def get_user_service(session: sessionmaker) -> UserServices:
    return UserServices(session=session)


# Diary Stub and Service ________________________________________________


def stub_diary_service():
    raise NotImplementedError


def get_diary_service(session: sessionmaker) -> DiaryServices:
    return DiaryServices(session=session)


# Page Stub and Service ________________________________________________

def stub_page_service():
    raise NotImplementedError


def get_page_service(session: sessionmaker) -> PageServices:
    return PageServices(session=session)
