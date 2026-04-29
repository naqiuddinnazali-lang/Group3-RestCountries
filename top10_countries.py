from g3_scrape import get_asian_countries

def get_top_10_countries():
    countries = get_asian_countries()
    # Sort by population in descending order
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    # Get top 10
    top_10 = sorted_countries[:10]
    return top_10

def display_top_10(top_10):
    print("Top 10 countries by population:")
    for i, country in enumerate(top_10, start=1):
        print(f"{i}. {country['name']}")
        print(f"   Capital: {country['capital']}")
        print(f"   Population: {country['population']:,}")
        print(f"   Region: {country['region']}")
        print(f"   Subregion: {country['subregion']}\n")

if __name__ == "__main__":
    top_10 = get_top_10_countries()
    display_top_10(top_10)