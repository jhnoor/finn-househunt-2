# Finn House-Hunt 2: Oslo Streets - A GTA-inspired Real Estate Scraper

This project is an automatic scraper for fetching real estate listings from finn.no (using their open search API) and injecting the data into a [Google Sheet document](https://docs.google.com/spreadsheets/d/1KhuunGT21T4y40u4-KEqiLtBR8lOuY_YqdeYkAVlK0c/edit#gid=2074132605).

## Features

- Automatically fetches apartment listings from finn.no
- Injects the data into a Google Sheet for easy analysis and filtering
- Customizable search parameters for targeted results

## Getting Started

### Prerequisites

- Python 3.x
- A Google account with access to Google Sheets

### Installation

1. Clone the repository:

```
git clone https://github.com/your_username/finn_house_hunt.git
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. Set up your Google Sheets API credentials (follow the instructions [here](https://developers.google.com/sheets/api/quickstart/python)).

4. Update the `google_sheet.py` file with your Google Sheets API credentials and the ID of the Google Sheet you want to use.

### Usage

1. Run the main script:

```
python main.py
```

2. The script will fetch apartment listings from finn.no and inject the data into the specified Google Sheet.

## Files

- `scraper.py`: Contains the main scraping logic
- `requirements.txt`: Lists the required Python packages
- `util.py`: Utility functions used throughout the project
- `README.MD`: This file, containing information about the project
- `.gitignore`: Specifies files and folders to be ignored by Git
- `google_sheet.py`: Handles Google Sheets API interactions
- `main.py`: The main script that runs the scraper and updates the Google Sheet
- `finn.py`: Contains functions for interacting with the finn.no API
- `.vscode/settings.json`: Visual Studio Code settings for the project

## Contributing

We welcome contributions to improve this project. Please feel free to submit issues and pull requests.

## License

This project is open-source and available under the MIT License.