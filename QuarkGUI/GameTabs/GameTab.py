from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

from QuarkAPI.Controllers.Stores import Game

from ..Buttons.FavouriteButton import FavouriteButton

Builder.load_file("./QuarkGUI/GameTabs/GameTab.kv")


class GameTab(BoxLayout):
    def __init__(self, game: Game, **kwargs):
        super().__init__(**kwargs)
        self.ids["name_tab"].text = game.name


