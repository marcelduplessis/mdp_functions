import wget
import requests
from bs4 import BeautifulSoup
import datetime

# Get the current year
year = datetime.datetime.now().year

# Define the base URL for sea ice data
data_url = 'http://data.meereisportal.de/data/iup/hdf/s/{}/'.format(year)

# Define the file extension for the data
file_extension = 'hdf'

# Function to list filenames within a server directory with a specific extension
def list_files_with_extension(url, extension=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(extension)]

# List all data files on the server with the specified extension
data_files = list_files_with_extension(data_url, file_extension)

# Define the start and end dates for the data range
date_start = '20230301'
date_end = '20230601'

# Find the indices for the start and end dates in the data file list
ind_start = next((i for i, item in enumerate(data_files) if date_start in item), None)
ind_end = next((i for i, item in enumerate(data_files) if date_end in item), None)

# Create a new list of files within the specified date range
selected_data_files = data_files[ind_start:ind_end]

# Specify the directory where you want to save the downloaded files
download_directory = '/Users/xduplm/Desktop/'

# Download the selected data files
for url in selected_data_files:
    filename = wget.download(url, out=download_directory)

# Download the latitude and longitude information for the sea ice data
lat_lon_url = 'https://seaice.uni-bremen.de/data/grid_coordinates/s6250/LongitudeLatitudeGrid-s6250-Antarctic.hdf'
lat_lon_filename = wget.download(lat_lon_url, out=download_directory)
