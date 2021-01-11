from typing import Union

from Controllers import GamesCollector, Filter, FilterNew
from Controllers.Stores import StoreTypes, Game


class Quark:
    gc = GamesCollector()

    def get_games(self, filter_params: Filter):
        return self.gc.collect_games(filter_params)

    def test(self):
        while 1:
            game_name = input("Enter game name: ")
            if game_name == "exit()":
                exit()
            else:
                games = self.get_games(self.construct_test_filter(game_name))
                for game in games:
                    self.print_game(game)

    def construct_test_filter(self, game_name: str):
        return FilterNew(name=game_name, stores=[StoreTypes.g2a, StoreTypes.steam])

    def print_game(self, game: Game):
        print(
            f"""
              name: {game.name} dev: {game.dev}
              price: {game.price} starting: {game.original_price} discount: {game.discount_percentage * 100}
              store: {game.store}
              """
        )


if __name__ == "__main__":
    api = Quark()
    api.test()
