import requests
import os

API_KEY = os.environ.get('KEY')
DOMAIN_NAME = os.environ.get('DOMAIN_NAME')


def send_simple_message(mail_to, domain_name, api_key):
    response = requests.post(
        f"https://api.mailgun.net/v3/{domain_name}/messages",
        auth=("api", api_key),
        data={"from": f"Excited User mailgun@{domain_name}",
              "to": [mail_to],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
    print(response.status_code)


if __name__ == '__main__':
    send_simple_message('lolo.edinburgh@gmail.com', DOMAIN_NAME, API_KEY)
