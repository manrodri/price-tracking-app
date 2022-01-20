import re
import requests
from bs4 import BeautifulSoup
from typing import Dict
import uuid
from common.database import Database


class Item:
    def __init__(self, url: str, tag_name: str, query: Dict, _id: str = None, cookies: Dict = {}):
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None
        self.cookies = cookies
        self.collection = 'items'
        self._id = _id or uuid.uuid4().hex

    def __repr__(self):
        return f"<Item {self.url}>"

    def load_price(self) -> float:
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

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query,
            "price": self.price

        }

    def save_to_mongo(self):
        Database.insert(self.collection, self.json())
