# Abstract interface for Repo the main Repo class will inherit from this
# Add any methods you want implemented here
# All methods are static


class RepoInterface:

    # Returns list of News Models
    # Default is 10
    @staticmethod
    def get_news(count=10):
        pass

    # Returns list of Country Models
    # Can specify countries by passing a list of Strings of country codes (US etc.) to the countries parameter
    # Columns =
        # name
        # code
        # population
        # updated_at
        # coordinates.latitude
        # coordinates.longitude
        # today.deaths
        # today.confirmed
        # latest_data.deaths
        # latest_data.confirmed
        # latest_data.recovered
        # latest_data.critical
        # latest_data.calculated.death_rate
        # latest_data.calculated.recovery_rate
        # latest_data.calculated.recovered_vs_death_ratio
        # latest_data.calculated.cases_per_million_population
    # ! Above list is not exclusive and actual num_columns could be larger
    @staticmethod
    def get_country_data(countries=None):
        pass
