import re


class Utils:
    @staticmethod
    def email_is_valid(email: str) -> bool:
        email_address_matcher = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return True if email_address_matcher.match(email) else False

