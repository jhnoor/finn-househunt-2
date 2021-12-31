import gspread
import os

def authenticate_google_sheet():
    # Authenticate with Google
    credentials_file = os.environ['CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE']
    gc = gspread.service_account(filename='{}'.format(credentials_file))
    sh = gc.open("House Hunt 2: Return to Oslo")
    return sh.get_worksheet(2)


# Get google credentials from environment variable

