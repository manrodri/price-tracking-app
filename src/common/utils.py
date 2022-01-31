import re
from passlib.hash import pbkdf2_sha512


class Utils:
    @staticmethod
    def email_is_valid(email: str) -> bool:
        email_address_matcher = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password: str) -> str:
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password: str, hashed_password) -> bool:
        return pbkdf2_sha512.verify(password, hashed_password)