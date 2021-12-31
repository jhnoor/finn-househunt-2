import gspread
import os
from dotenv import load_dotenv

load_dotenv()


def authenticate_google_sheet():
    # Authenticate with Google
    credentials_file = os.environ['CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE']
    gc = gspread.service_account(filename='{}'.format(credentials_file))
    sh = gc.open("House Hunt 2: Return to Oslo")
    return sh.get_worksheet(0)


# Get google credentials from environment variable

