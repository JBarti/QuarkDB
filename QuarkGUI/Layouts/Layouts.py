from typing import List

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect

from QuarkAPI.Controllers.Stores import Game, StoreTypes

from ..GameTabs.GameTab import GameTab

Builder.load_file("./QuarkGUI/Layouts/Layouts.kv")


class UpperBar(BoxLayout):
    pass


class BottomBar(GridLayout):
    pass


class GamesLayout(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def display_games(self, games: List[Game]):
        game_container = self.ids["game_container"]
        game_container.clear_widgets()

        for game in games:
            game_container.add_widget(GameTab(game))


class FilterLayout(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.store_filters = {}

    def _finish_init(self):
        self.store_filters = {
            StoreTypes.steam: self.ids["steam_check"],
            StoreTypes.g2a: self.ids["g2a_check"],
        }

    def get_prices(self):
        try:
            price_from = float(self.ids["price_from"].text)
        except ValueError:
            price_from = None

        try:
            price_to = float(self.ids["price_to"].text)
        except ValueError:
            price_to = None

        return price_from, price_to

    def get_filters(self):
        stores = [
            store
            for store, chck in self.store_filters.items()
            if chck.state == "down"
        ]

        price_from, price_to = self.get_prices()
        discount = self.ids["discount_check"].state == "down"

        return {
            "stores": stores,
            "price_from": price_from,
            "price_to": price_to,
            "discount": discount,
        }


