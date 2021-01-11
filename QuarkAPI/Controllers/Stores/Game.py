from dataclasses import dataclass
from datetime import datetime
from typing import List

from .Store import StoreTypes


@dataclass
class Game:
    name: str
    dev: str
    price: float
    original_price: float
    discount_percentage: float
    fetch_date: datetime
    store: List[StoreTypes]
    image_url: str
    release_date: datetime = None
    is_stored: bool = False
    currency: str = "EUR"
