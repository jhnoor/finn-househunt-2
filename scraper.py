# Scrapes web page data from finn.no and retrieves apartment data

import requests
from bs4 import BeautifulSoup
import re


def get_page_data(id):
    url = 'https://www.finn.no/realestate/homes/ad.html?finnkode={}'.format(id)
    response = requests.get(url)

    # Place response into object
    return response.text

# Parses html using BeautifulSoup
def parse_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup

def get_cost_breakdown(soup):
    costs_keys_html = soup.select("div.panel>dl>dt")
    costs_html = soup.select("div.panel>dl>dd")
    # Use regex to remove non-numeric characters
    costs = [[re.sub('[^0-9]', '', x.text) for x in html] for html in costs_html]
    costs_keys = [x.text for x in costs_keys_html]
    
    # create a dictionary of the costs
    return dict(zip(costs_keys, [x[0] for x in costs]))

def get_apt_details(soup):
    detail_keys_html = soup.select("section.panel>dl>dt")
    detail_html = soup.select("section.panel>dl>dd")
    detail_dict = dict(zip([x.text for x in detail_keys_html], [x.text for x in detail_html]))
    if ("Energimerking" in detail_dict):
        detail_dict["Energimerking"] = detail_dict["Energimerking"].split("\n")[2].strip()
    return detail_dict