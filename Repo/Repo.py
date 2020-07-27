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
        df = df[["name", "population", "today.deaths", "today.confirmed"]]
        df =  df.rename(columns = ({"name" : "Country", "population": "Population"}))
        return df