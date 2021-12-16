import requests
from bs4 import BeautifulSoup
import urllib.request 
import os

REPO = "https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports"
GH_RAW = "https://raw.githubusercontent.com/"


def setup_data_dir():
    if not os.path.isdir(os.path.join(os.pardir, 'data', 'raw', 'covid19', 'daily_reports')):
        os.makedirs(os.path.join(os.pardir, 'data', 'raw', 'covid19', 'daily_reports'))

def get_csv_files():
    print('Collecting daily covid reports...')
    r = requests.get(REPO)
    soup = BeautifulSoup(r.text, 'html.parser')
    csv_files = [h['href'] for h in soup.find_all('a', {'class': 'js-navigation-open Link--primary'})if h['href'].endswith('.csv')]
    total_csv_files = len(csv_files)

    for i, csv_file in enumerate(csv_files):
        
        file_name =  csv_file.split('/')[-1]
        raw_url = GH_RAW + csv_file.replace('/blob', '')
        
        print(f'Getting daily report: {file_name} ({i+1}/{total_csv_files})')
        save_path = os.path.join(os.pardir, 'data', 'raw', 'covid19', 'daily_reports', file_name)
        urllib.request.urlretrieve(raw_url, save_path)

if __name__ == "__main__":
    print('Running Covid Scraper')
    setup_data_dir()
    get_csv_files()

