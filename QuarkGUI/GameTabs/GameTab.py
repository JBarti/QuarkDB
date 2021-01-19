from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.image import AsyncImage

from QuarkAPI.Controllers.Stores import Game
from QuarkAPI.Quark import api

from ..Buttons.FavouriteButton import FavouriteButton

Builder.load_file("./QuarkGUI/GameTabs/GameTab.kv")


class GameTab(BoxLayout):
    def __init__(self, game: Game, **kwargs):
        super().__init__(**kwargs)
        self.game = game

        self.ids["img_tab"].source = game.image_url
        self.ids["name_tab"].text = game.name
        self.ids["store_tab"].text = game.store
        self.ids["price_tab"].text = str(game.price)
        self.ids["discount_tab"].text = "{0:.2f}%".format(game.discount_percentage)
        self.ids["original_price_tab"].text = str(game.original_price)
        
        self.ids["btn_favourite"].disabled = game.is_stored or api.is_game_stored(game)
        self.ids["btn_favourite"].on_press = self.favourite_game


    def favourite_game(self):
        api.store_game(self.game)
        self.ids["btn_favourite"].disabled = True

