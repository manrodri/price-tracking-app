import re
import uuid
from typing import Dict

from models.model import Model


class Store(Model):
    collection = 'stores'

    def __init__(self, name: str, url_prefix: str, tag_name: str, query: Dict, _id: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = _id or uuid.uuid4().hex

    def __repr__(self):
        return f"<Store: {self._id}>"

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_by_name(cls, store_name: str) -> "Store":
        return cls.find_one_by("name", store_name)

    @classmethod
    def get_by_url_prefix(cls,url_prefix: str) -> "Store":
        url_regex = {"$regex": "^{}".format(url_prefix)}
        print(f"url_prefix: {url_prefix}")
        print(f"store collection: {cls.collection}")
        return cls.find_one_by("url_prefix", url_regex)

    @classmethod
    def find_by_url(cls, url: str) -> "Store":
        '''
        Return a store from a url like https://johnlewis.co.uk/tiems/somethg/.kfdkfdkfdkdfkd
        :param url: the url of the item
        :return: the store object
        '''

        pattern = re.compile(r'(https?://.*?/)')
        match = pattern.search(url)
        url_prefix = match.group(1)
        print(f"url_prefix found: {url_prefix}")
        return cls.get_by_url_prefix(url_prefix)




