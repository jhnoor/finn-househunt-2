import gspread

def authenticate_google_sheet():
    # Authenticate with Google
    gc = gspread.service_account()
    sh = gc.open("House Hunt 2: Return to Oslo")
    return sh.get_worksheet(2)
