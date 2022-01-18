import re
import requests
from bs4 import BeautifulSoup


class Item:
    def __init__(self, url, tag_name, query, cookies={}):
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None
        self.cookies = cookies

    def load_price(self):
        response = requests.get(self.url)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')
        element = soup.find(self.tag_name, self.query)

        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d+\.\d+)")
        match = pattern.search(string_price)
        found_price = match.group(1)

        price_without_comma = found_price.replace(",", "")

        self.price = float(price_without_comma)
        return self.price

        # business login to load price and return it as a float
        # request, beautifulsoup, strip, regex,...
        pass


'''

ebay_url = "https://www.ebay.co.uk/itm/185032451286?epid=3041134620&_trkparms=ispr%3D1&hash=item2b14cb24d6:g:01sAAOSwF9FhM253&amdata=enc%3AAQAGAAACkPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsS7UXID%252BRPOSNsnm8kYPghtD3Gb4V8jGdYP047P6Dr%252Bj9kRutrnwhjICepW1KhGfFfuE%252FKyPMFzGUy0ha9nCsoF3%252BAAxopa8P0F%252Bd8LvrJcbwBPUeIu1r0iQvYEYD%252BWBIRTXXX7NteiJrdE%252F0uJyPmlDZIKb0n4lYObeDF45X2fdB3PzYe71Dg73IBmouzaFq0g4U56Gq9lGTrrzdjkdOatS5HG9GGbJ7nLxq4eyiTmtxQ9CRVkg8dqGvOgC6Cli48vdMClXncJjNXBq26UbwpG%252BWZf40%252FJVV3jR%252B6WhKeQZWaUngEhC%252FrQmqGw1zwK9UCPUvNq6xBUlSxFn2bcgIF3CdHrg1wVesib5%252F8bIGKjEs5EfvvQ3wo2K2rfVqflA2b%252Bw6XHfNwDLsgD%252FbDtA%252BHTfMTWb3FS6PMAjym%252BR8l65GrCPogztGeZ4XDuq8aVuearnx0XDr1rlXho90VYCLF%252FJMYOvTfm%252FWOkNBCtOrjYZOuS9uhqLSHa57I%252FfwHDptrZ3IN7yGDhu5p%252B1ae59vvqV8sFYFcYwdAm%252FBxcV0Iqeq5ZBn6C%252Fby4OptbFkIUCzPTmOcvInTB5cyWX%252F5d39A6%252BltIX1mwvwrlq%252BRjvKBWUN65kwo8tnsX4iXaYUvUeZTyalpajmXrHfyQOovT%252B7hZTTqo52XaUnFLkpm3KBlTemzyV%252B%252BLYnm6aLi50GO4TM3zmgxZDYsPRMdeFNa093vR8ETh2JJoOOwfFzCX7BgosDXaWx5vsGFt9X%252FYa9w%252BGLvVV5Z1N5PvFPXSGnEpilvBbk0ed2yWe38483GqhoC8s2CCS8XVDxAP1NWj2id9dzn%7Cclp%3A2334524%7Ctkp%3ABFBM_pnot8xf"

TAG_NAME = "div"
QUERY = {"class": "prc__active-price"}

response = requests.get(decathlon_url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

element = soup.find(TAG_NAME, QUERY)
#
# string_price = element.text.strip()strip

# print(f"string_price: {string_price}")
print(f'element: {element}')
# print(f"all_matches: {all_matches}")


#
# item = Item(url, tag_name, query)
# item.load_price()

'''
