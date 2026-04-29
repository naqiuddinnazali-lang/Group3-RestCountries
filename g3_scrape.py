import requests
import urllib3

# Suppress only the insecure request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_asian_countries():
    """
    Fetches country data for Asia from restcountries.com,
    bypassing SSL verification (not recommended for production).
    Returns a list of dictionaries with country details.
    """
    url = "https://restcountries.com/v3.1/region/asia"
    response = requests.get(url, verify=False)
    response.raise_for_status()
    countries = response.json()
    result = []
    for country in countries:
        info = {
            "name": country.get('name', {}).get('common', 'N/A'),
            "capital": country.get('capital', ['N/A'])[0],
            "population": country.get('population', 'N/A'),
            "region": country.get('region', 'N/A'),
            "subregion": country.get('subregion', 'N/A')
        }
        result.append(info)
    return result

# Example usage
asian_countries = get_asian_countries()
for c in asian_countries:
    print(c)