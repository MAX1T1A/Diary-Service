from services.user_services import UserServices, user_service


def provider_diary():
    raise NotImplementedError


def get_user_service() -> UserServices:
    return UserServices()




