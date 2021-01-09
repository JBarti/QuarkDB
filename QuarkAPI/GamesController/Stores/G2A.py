import requests
from urllib.parse import urlencode

from .Store import Store


class G2A(Store):
    URL_BASE = "https://www.g2a.com/new/api/v3/products/filter"

    CUSTOM_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Host": "www.g2a.com",
        "Origin": "https://www.g2a.com",
        "Referer": "https://www.g2a.com/",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "if-none-match": "W/\"9d3-vtNfK63G7ERz4Ayz1z6ErA\"",
    }


    def __init__(self):
        super().__init__(G2A.URL_BASE, G2A.CUSTOM_HEADERS)


    def get_games(self, search_pattern: str):
        url_params = {
            "currency": "EUR",
            "query": search_pattern,
            "store": "english",
            "wholesale": "false"
        }
        print("GOT HERE")
        data = self.fetch_raw_data(url_params)
        print(data)


