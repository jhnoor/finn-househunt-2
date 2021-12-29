# Retrieves all the apartments for sale that fits the filter
# and then inserts the attributes into the google sheet
# ensuring that the id is unique
from finn import get_apartments
from google_sheet import authenticate_google_sheet
from util import get_value

sh = authenticate_google_sheet()
apartments = get_apartments()
rows = sh.get_worksheet(0).get_all_records()

for apt in apartments:
    if apt['ad_id'] not in [row['id'] for row in rows]:

    # ad_id = print(doc['ad_id'])
    # heading = print(doc['heading'])
    # price_suggestion = print(doc['price_suggestion']['amount'])
    # price_total = print(doc['price_total']['amount'])
    # area_range = print(doc['area_range']['size_from'])
        new_row = [
            apt['ad_id'],
            apt['ad_link'],
            get_value('local_area_name'),
            None,
            None,
            None, 
            apt['area_range']['size_from'],
            apt['price_suggestion']['amount'],
            None,
            None,
            None,
            apt['price_shared_cost']['amount'],
        ]
        # Insert the attributes into the google sheet
        sh.get_worksheet(0).append_row(new_row)

