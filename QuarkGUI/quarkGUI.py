from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set("graphics", "width", 900)
Config.set("graphics", "height", 600)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from .Buttons.searchbutton import SearchButton
from .Buttons.MainPageButton import MainPageButton
from .Buttons.FavouritePageButton import FavouritePageButton
from .Buttons.FavouriteButton import FavouriteButton
from .Layouts.Layouts import UpperBar, BottomBar, GamesLayout, FilterLayout
from .Inputs.Inputs import SearchInput, FromPriceInput,ToPriceInput
from .GameTabs.GameTab import GameTab

from QuarkAPI.Quark import api
from QuarkAPI.Controllers import Filter, FilterNew, FilterStored, StoreTypes


Builder.load_file("./QuarkGUI/quarkGUIkivy.kv")



class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids["btn_search"].on_press = self.apply_filter
        self.ids["filters"]._finish_init()

    def get_page_filter_cls(self) -> Filter:
        main_page = self.ids["btn_main_pg"].state == "down"
        fav_page = self.ids["btn_fav_pg"].state == "down"

        if main_page:
            return FilterNew
        if fav_page:
            return FilterStored

    def apply_filter(self):
        game_name = self.ids["filter_name"].text
        filters = self.ids["filters"].get_filters()
        filter_cls = self.get_page_filter_cls()

        game_filter = filter_cls(
            name=game_name,
            stores=filters.get("stores"),
            price_from=filters.get("price_from"),
            price_to=filters.get("price_to"),
            discount=filters.get("discount"),
        )

        games = api.get_games(game_filter)
        self.ids["games"].display_games(games)


class QuarkFE(App):
    def build(self):
        return MainLayout()
