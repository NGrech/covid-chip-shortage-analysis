import os 
import urllib.request 
import urllib.error

BASE_URL = "https://www.oica.net/wp-content/uploads/Passenger-Cars-"
YEARS = [2018, 2019, 2020, 2021]

def setup_data_dir():
    if not os.path.isdir(os.path.join(os.pardir, 'data','raw', 'automotive')):
        os.makedirs(os.path.join(os.pardir, 'data', 'raw', 'automotive'))

def retrieve_files():
    for year in YEARS:
        print(f'Getting Data for {year}.')
        url = BASE_URL + str(year) + '.xlsx'
        save_path = os.path.join(os.pardir, 'data', 'raw', 'automotive', f'oica_stats_{year}.xlsx')
        try:
            urllib.request.urlretrieve(url, save_path)
        except  urllib.error.HTTPError:
            print(f'No data for {year}')


if __name__ == "__main__":
    print('Running Automotive Scraper')
    setup_data_dir()
    retrieve_files()
