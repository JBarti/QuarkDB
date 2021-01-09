from typing import Union

from Filter import Filter


class Quark():
    last_fetched = []
    def get_games(self, filter_params: Filter):
        pass


if __name__ == "__main__":
    from GamesController.Stores import G2A
    G2A().get_games("penis")
