from requests import Response, post
import os
from typing import List


class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message


class Mailgun:
    API_KEY = os.environ.get('KEY', None)
    DOMAIN_NAME = os.environ.get('DOMAIN_NAME', None)

    FROM_TITLE = 'Pricing service'
    FROM_EMAIL = f'do-not-reply@{DOMAIN_NAME}'
    MAILGUN_URL = f"https://api.mailgun.net/v3/{DOMAIN_NAME}/messages"

    @classmethod
    def send_email(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        if cls.API_KEY is None:
            raise MailgunException("Failed to load Mailgun API KEY")
        if cls.DOMAIN_NAME is None:
            raise MailgunException("Failed to load Mailgun DOMAIN_NAME")

        response = post(
            cls.MAILGUN_URL,
            auth=("api", cls.API_KEY),
            data={"from": f"{cls.FROM_TITLE} {cls.FROM_EMAIL}",
                  "to": [email],
                  "subject": subject,
                  "text": text,
                  "html": html,
                  })
        if response.status_code != 200:
            print(response.json())
            raise MailgunException("An error occurred while sending emails")

        return response


if __name__ == '__main__':
    Mailgun.send_email(['lolo.edinburgh@gmail.com'],
                       "Hello",
                       "This is a test",
                       '<h4>This is a test</h4>'
                       )
