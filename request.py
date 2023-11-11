import requests
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
from pathlib import Path
from datetime import datetime as dt

# Disable insecure platform warnings
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

# Get the script directory
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# File name for the day
today = dt.now()
folder_today = str(today.day)

# File name for the month
current_month = dt.now()
folder_name = str(current_month.month)

# Create full paths for the folders
folder_name = current_dir / "Folder_name" / "folder_name_year" / folder_name
folder_today = folder_name / folder_today

# Check if the month folder does not exist before creating
if not folder_name.exists():
    folder_name.mkdir(parents=True)
    print(f'Month folder created at: {folder_name}')
else:
    print(f'The month folder {folder_name} already exists.')

# Check if the day folder does not exist before creating
if not folder_today.exists():
    folder_today.mkdir()
    print(f'Day folder created at: {folder_today}')
else:
    print(f'The day folder {folder_today} already exists.')

# Username & Password
username = 'YOUR_LOGIN'
password = 'PASSWORD!@#' #JUST FOR DOCUMENTATION

url_csv = 'URL_TO_DOWNLOAD_YOUR_CSVfile'

login_data = {
    'username': username,
    'password': password,
}

# Request session
with requests.Session() as session:
    # Disable SSL certificate verification
    session.verify = False

    # Perform login using basic authentication in the header
    # session.post(url_csv, auth=(username, password))

    # Download the CSV file after login
    response = session.get(url_csv, auth=(username, 'pasword!@#'))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(f'Connection 100%')
        # Specify the path where you want to save the file
        destination_path = str(folder_today / 'FILE.csv')

        # Save the file content
        with open(destination_path, 'wb') as file:
            file.write(response.content)

        print(f"Download completed. File saved at: {destination_path}")
    else:
        print(f"Download error. Status code: {response.status_code}")
