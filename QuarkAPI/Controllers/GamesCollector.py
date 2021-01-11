from typing import List
from copy import deepcopy

from .Stores import Store, StoreTypes, Steam, G2A, GOG, Game
from .Filter import Filter, FilterNew, FilterStored


class GamesCollector:
    store_types_classes = {
        StoreTypes.steam: Steam(),
        StoreTypes.g2a: G2A(),
    }

    def __init__(self):
        self.last_fetched = []
        self.last_filter = Filter(stores=[])

    def collect_games(self, filter_params: Filter):
        if not self.should_fetch(filter_params):
            self.last_filter = deepcopy(filter_params)
            return self.apply_filters(filter_params, self.last_fetched)

        games = []
        for store_type in filter_params.stores:
            games += self.store_types_classes[store_type].get_games(filter_params.name)

        return self.apply_filters(filter_params, games)

    def should_fetch(self, filter_params: Filter):
        return not (filter_params.name == self.last_filter.name and self.last_fetched) 

    def search_stores(self, pattern: str, stores: List[Store]):
        pass

    def apply_filters(self, filter_params: Filter, games: List[Game]):
        return games
