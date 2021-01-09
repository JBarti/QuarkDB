import requests
from urllib.parse import urlencode


class Store:
    def __init__(self, url_base: str, custom_headers: dict):
        self.url_base = url_base
        self.custom_headers = custom_headers


    def build_url(self, url_params: dict):
        str_params = urlencode(url_params)
        return f"{self.url_base}?{str_params}"

    def fetch_raw_data(self, url_params: dict):
        url = self.build_url(url_params)

        print(url)
        resp = requests.get(
            url=url,
            headers=self.custom_headers,
        )

        return resp.json()
