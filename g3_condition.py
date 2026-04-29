
countries = [
    {
        "Country": "Iran",
        "Capital": "Tehran",
        "Region": "Asia",
        "Subregion": "Southern Asia",
        "Population": 85961000,
    },
    {
        "Country": "Indonesia",
        "Capital": "Jakarta",
        "Region": "Asia",
        "Subregion": "South-Eastern Asia",
        "Population": 284438782,
    }
]

more_than_100m = []
less_than_100m = []

for country in countries:
    if country["Population"] >= 100_000_000:
        more_than_100m.append(country)
    else:
        less_than_100m.append(country)

print("Countries with population ≥ 100,000,000:")
for c in more_than_100m:
    print(f"- {c['Country']}")

print("\nCountries with population < 100,000,000:")
for c in less_than_100m:
    print(f"- {c['Country']}")
