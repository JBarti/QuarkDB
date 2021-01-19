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

from QuarkAPI.Quark import Quark
from QuarkAPI.Controllers import FilterNew, FilterStored, StoreTypes



Builder.load_file("./QuarkGUI/quarkGUIkivy.kv")


class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api = Quark()
        self.stored = False

        games = self.api.get_games(self.get_test_filter())
        self.ids["games"].display_games(games)

        self.ids["btn_search"].on_press = self.apply_filter
        self.ids["filters"]._finish_init()

    def get_test_filter(self):
        return FilterNew(
            name="Star Wars",
            stores=[StoreTypes.steam],
        )

    def apply_filter(self):
        game_name = self.ids["filter_name"].text
        filters = self.ids["filters"].get_filters()

        FlterNew()

        print(filters)



class QuarkFE(App):
    def build(self):
        return MainLayout()
