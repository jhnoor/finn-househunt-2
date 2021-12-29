import requests
import json

def get_apartments():
    # Make a request to Finn API
    url = 'https://www.finn.no/api/search-qf?searchkey=SEARCH_ID_REALESTATE_HOMES&area_from=56&facilities=1&lat=59.931445590877985&lifecycle=1&lifecycle=3&lon=10.808450499022456&no_of_bedrooms_from=2&price_collective_to=5500000&radius=3000&sort=PUBLISHED_DESC&stored-id=53316898&q='
    response = requests.get(url)

    # Place response into object
    return json.loads(response.text)['docs']