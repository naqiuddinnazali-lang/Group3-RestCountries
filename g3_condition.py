

class CountryPopulationFilter:
    def __init__(self, countries):
        self.countries = countries
        self.more_than_100m = []
        self.less_than_100m = []

    def classify_countries(self):
        for country in self.countries:
            if country["Population"] >= 100_000_000:
                self.more_than_100m.append(country)
            else:
                self.less_than_100m.append(country)

    def display_results(self):
        print("Countries with population ≥ 100,000,000:")
        for c in self.more_than_100m:
            print(f"- {c['Country']}")
            print(f"  Capital: {c['Capital']}")
            print(f"  Region: {c['Region']}")
            print(f"  Subregion: {c['Subregion']}\n")

        print("Countries with population < 100,000,000:")
        for c in self.less_than_100m:
            print(f"- {c['Country']}")
            print(f"  Capital: {c['Capital']}")
            print(f"  Region: {c['Region']}")
            print(f"  Subregion: {c['Subregion']}\n")

