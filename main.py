# Retrieves all the apartments for sale that fits the filter
# and then inserts the attributes into the google sheet
# ensuring that the id is unique
from finn import get_apartment, get_apartments
from google_sheet import authenticate_google_sheet
from util import get_value
from datetime import datetime

sheet = authenticate_google_sheet()
apartments = get_apartments()
rows = sheet.get_all_records()

def filter_apartments(apt):
    # checks if key is in dictionary
    if ('price_suggestion' not in apt):
        return False
    
    is_not_present = (apt['ad_id'] not in [row['link'] for row in rows])

    return is_not_present


for (i, apt) in enumerate(filter(filter_apartments, apartments)):
    # Parses date from strings like "2022-01-06T15:30:00.000+00:00"
    viewing_times = [datetime.strftime(datetime.strptime(
        x, "%Y-%m-%dT%H:%M:%S.%f%z"), "%Y-%m-%d %H.%M.%S")for x in get_value(apt, 'viewing_times')]
    apt_detailed = get_apartment(apt['ad_id'])
    new_row = [
        '=HYPERLINK("{}"; "{}")'.format(apt['ad_link'], apt['ad_id']),  # link
        get_value(apt, 'local_area_name'),  # område
        apt['owner_type_description'],
        '=O{0}-F{0}+calculator!c14-K{0}'.format(len(rows)+i+2),
        apt['area_range']['size_from'],
        apt['price_suggestion']['amount'],
        '=F{0}/E{0}'.format(len(rows) + i+2),
        get_value(apt_detailed, 'Fellesgjeld'),
        apt['price_shared_cost']['amount'],
        apt['number_of_bedrooms'],
        get_value(apt_detailed, 'Omkostninger'),
        get_value(apt_detailed, 'Byggeår'),
        get_value(apt_detailed, 'Energimerking'),
        None,
        '=calculator!B17-H{0}'.format(len(rows) + i+2),
        viewing_times[0] if len(viewing_times) > 0 else None,
        viewing_times[1] if len(viewing_times) > 1 else None,
        datetime.now().strftime("%Y-%m-%d %H.%M.%S"),
        '=(1/G{0}/0,000001)+(D{0}/100000000)*0,2-(H{0}/100000)'.format(len(rows) + i+2),
    ]
    # Insert the attributes into the google sheet
    print("Adding row: {}".format(new_row))
    sheet.insert_row(
        new_row, 
        value_input_option='USER_ENTERED',
        index=len(rows) + i+2
    )
