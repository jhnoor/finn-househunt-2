import requests
import json

from scraper import get_apt_details, get_cost_breakdown, get_page_data, parse_html
from util import flatten
from toolz import unique


def get_apartments():
    # Make a request to Finn API
    urls = [
        'https://www.finn.no/api/search-qf?searchkey=SEARCH_ID_REALESTATE_HOMES&area_from=56&facilities=1&lat=59.931445590877985&lifecycle=1&lon=10.808450499022456&no_of_bedrooms_from=2&price_collective_to=5500000&radius=3000&sort=PUBLISHED_DESC&stored-id=53316898',
        'https://www.finn.no/api/search-qf?searchkey=SEARCH_ID_REALESTATE_HOMES&area_from=56&facilities=1&lat=59.89706652757974&lifecycle=1&lon=10.773433609564563&no_of_bedrooms_from=2&price_collective_to=5500000&radius=1500&sort=PUBLISHED_DESC&stored-id=53395250',
        'https://www.finn.no/api/search-qf?searchkey=SEARCH_ID_REALESTATE_HOMES&area_from=55&lat=59.93234101544252&lifecycle=1&lon=10.780679560073699&no_of_bedrooms_from=2&price_collective_to=5700000&radius=5000&stored-id=53445669'
    ]

    apartments = flatten([search_apartments(url) for url in urls])
    return list(unique(apartments, key=lambda x: x['ad_id']))


def search_apartments(search_url):
    response = requests.get(search_url)
    return json.loads(response.text)['docs']


def get_apartment(id):
    page_data = get_page_data(id)
    soup = parse_html(page_data)
    costs = get_cost_breakdown(soup)
    details = get_apt_details(soup)
    return {**costs, **details}
