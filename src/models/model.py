from abc import ABCMeta, abstractmethod
from typing import List, TypeVar, Type, Dict, Union

from common.database import Database

T = TypeVar('T')


class Model(metaclass=ABCMeta):
    collection: str
    _id: str

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    def save_to_mongo(self):
        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id": self._id})

    # _id are unique so we can return the first item found
    @classmethod
    def get_by_id(cls: Type[T], _id: str) -> T:
        return cls.find_one_by("_id", _id)

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        element_from_db = Database.find(cls.collection, {})  # it returns a cursor
        return [cls(**elem) for elem in element_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: Union[str, Dict]):
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute, value) -> List[T]:
        return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]
