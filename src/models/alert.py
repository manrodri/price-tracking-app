import uuid
from typing import Dict
from models.item import Item
from common.database import Database
from models.model import Model


class Alert(Model):

    collection = 'alerts'

    def __init__(self, item_id: str, price_threshold: float, _id: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_threshold = price_threshold
        self._id = uuid.uuid4().hex

    def __repr__(self):
        return f"<Alert: {self._id}>"

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "price_threshold": self.price_threshold,
            "item_id": self.item_id
        }

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        # email functionality to be implemented for now jsut prints out a message
        if self.item.price < self.price_threshold:
            print(f"Item {self.item} price is below {self.price_threshold}!! \n")
            print(f"Latest price: {self.item.price}\n")


