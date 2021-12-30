# Retrieves all the apartments for sale that fits the filter
# and then inserts the attributes into the google sheet
# ensuring that the id is unique
from finn import get_apartment, get_apartments
from google_sheet import authenticate_google_sheet
from util import get_value
from datetime import datetime

sh = authenticate_google_sheet()
apartments = get_apartments()
rows = sh.get_worksheet(0).get_all_records()

for (i, apt) in enumerate(filter(lambda apt: (apt['ad_id'] not in [row['link'] for row in rows]), apartments)):
    # Parses date from strings like "2022-01-06T15:30:00.000+00:00"
    viewing_times = [datetime.strftime(datetime.strptime(
        x, "%Y-%m-%dT%H:%M:%S.%f%z"), "%Y-%m-%d %H.%M.%S")for x in get_value(apt, 'viewing_times')]
    apt_detailed = get_apartment(apt['ad_id'])
    new_row = [
        '=HYPERLINK("{}"; "{}")'.format(apt['ad_link'], apt['ad_id']),
        get_value(apt, 'local_area_name'),
        viewing_times[0] if len(viewing_times) > 0 else None,
        viewing_times[1] if len(viewing_times) > 1 else None,
        apt['owner_type_description'],
        apt['area_range']['size_from'],
        apt['price_suggestion']['amount'],
        '=G{}/F{}'.format(len(rows) + i+2, len(rows) + i+2),
        get_value(apt_detailed, 'Fellesgjeld'),
        apt['price_shared_cost']['amount'],
        apt['number_of_bedrooms'],
        get_value(apt_detailed, 'Omkostninger'),
        get_value(apt_detailed, 'Byggeår'),
        get_value(apt_detailed, 'Energimerking')
    ]
    # Insert the attributes into the google sheet
    print("Adding row: {}".format(new_row))
    sh.get_worksheet(0).append_row(
        new_row, value_input_option='USER_ENTERED')


def filter_apartments(apt):
    return (apt['ad_id'] not in [row['id'] for row in rows])
