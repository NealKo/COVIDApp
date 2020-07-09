import json
import requests
from pandas import json_normalize


class DataFetcher:

    @staticmethod
    def get_news(count=10):
        pass

    # Quick and dirty implementation
    # Only returns full list for now
    @staticmethod
    def get_countries(countries=None):
        # TODO switch to URL builder
        data = requests.get("https://corona-api.com/countries")

        json_dict = json.loads(data.content).get("data")
        data_frame = json_normalize(json_dict)

        return data_frame
