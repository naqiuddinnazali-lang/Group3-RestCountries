def classify_countries(countries, more_than_100m, less_than_100m):
    for country in countries:
        if country["Population"] >= 100_000_000:
            more_than_100m.append(country)
        else:
            less_than_100m.append(country)

def display_results(more_than_100m, less_than_100m):
    print("Countries with population ≥ 100,000,000:")
    for c in more_than_100m:
        print(f"- {c['Country']}")
        print(f"  Capital: {c['Capital']}")
        print(f"  Region: {c['Region']}")
        print(f"  Subregion: {c['Subregion']}\n")

    print("Countries with population < 100,000,000:")
    for c in less_than_100m:
        print(f"- {c['Country']}")
        print(f"  Capital: {c['Capital']}")
        print(f"  Region: {c['Region']}")
        print(f"  Subregion: {c['Subregion']}\n")

if __name__ == "__main__":
    classify_countries("Jakarta")
