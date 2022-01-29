import uuid
from typing import Dict
from dataclasses import dataclass, field
from models.item import Item
from models.model import Model


@dataclass(eq=False)
class Alert(Model):

    collection: str = field(init=False, default='alerts')
    name: str
    item_id: str
    price_limit: float
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)

    def __repr__(self):
        return f"<Alert: {self._id}>"

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name": self.name,
            "price_limit": self.price_limit,
            "item_id": self.item_id
        }

    def load_item_price(self) -> float:  # not working
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        # email functionality to be implemented for now jsut prints out a message
        if self.item.price < self.price_limit:
            print(f"Item {self.item} price is below {self.price_limit}!! \n")
            print(f"Latest price: {self.item.price}\n")


