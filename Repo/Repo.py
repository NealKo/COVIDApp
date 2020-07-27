from flask_setup.DataFetcher.DataFetcher import DataFetcher
from Repo.RepoInterface import RepoInterface


# !!!TODO For now always pulls from API directly need to cache in a MySQL database on Google Cloud
class Repo(RepoInterface):

    # Returns a pandas data frame with the news data
    # Default is 10
    @staticmethod
    def get_news(count=10):
        DataFetcher.get_news(count)

    # Returns a pandas data frame with the country data
    # Can specify countries by passing a list of Strings of country codes (US etc.) to the countries parameter
    # None will return all countries
    @staticmethod
    def get_country_data(countries=None):
        return DataFetcher.get_countries(countries)

    @staticmethod
    def get_formatted_data(countries=None):
        df = Repo.get_country_data(countries)
        df = df[
            ["name", "latest_data.confirmed", "latest_data.deaths", "latest_data.critical", "latest_data.recovered"]]
        df = df.rename(columns=({"name": "Country",
                                 "latest_data.confirmed": "Confirmed Cases",
                                 "latest_data.deaths": "Deaths",
                                 "latest_data.critical": "Critical Cases",
                                 "latest_data.recovered": "Recovered"}))
        df = df[df["Confirmed Cases"] > 0]
        return df
