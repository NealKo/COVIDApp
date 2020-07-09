
class CountryData:

    class Coordinates:
        def __init__(self, latitude, longitude):
            self.latitude = latitude
            self.longitude = longitude

    class Today:
        def __init__(self, deaths, cases):
            self.deaths = deaths
            self.cases = cases

    class LatestData:
        def __init__(self, deaths, confirmed, recovered, critical, calculated):
            self.deaths = deaths
            self.confirmed = confirmed
            self.recovered = recovered
            self.critical = critical
            self.calculated = calculated

        class Calculated:
            def __init__(self, deaths, confirmed, recovered, critical):
                self.deaths = deaths
                self.confirmed = confirmed
                self.recovered = recovered
                self.critical = critical


