from services.user_services import UserServices


def stub_user_service():
    raise NotImplementedError


def get_user_service(session) -> UserServices:
    return UserServices(session)




