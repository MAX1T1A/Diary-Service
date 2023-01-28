from passlib.context import CryptContext


class Hash:
    pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def bcrypt(self, password: str):
        return self.pwd_cxt.hash(password)

    def verify(self, hashed_password, plain_password):
        return self.pwd_cxt.verify(plain_password, hashed_password)
