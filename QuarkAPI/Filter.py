from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import List

from GamesController.Stores import GOG, G2A, Steam, Store


class StoreTypes(Enum):
    steam = Steam
    g2a = G2A
    gog = GOG


class Filter:
    name: str = None
    dev: str = None
    price_from: float = None
    price_to: float = None
    discount: bool = None
    store: List[Store] = []


@dataclass
class FilterNew(Filter):
    from_stored = False


@dataclass
class FilterStored(Filter):
    date_from: datetime = datetime.now() - timedelta(weeks=5)
    date_to: datetime = datetime.now()
    from_stored = True

