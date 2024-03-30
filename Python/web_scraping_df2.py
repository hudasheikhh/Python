#Unable to scrape data from Amazon, so using wikipedia
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')
    #scraped_text = soup.prettify()
    table = soup.find('table', class_='wikitable') #here, soup.find() will get data for just A character, soup.find_all() will give a list of all the characters.

    if table:
        data_rows = []
        for row in table.find_all('tr')[1:]:
            cells = row.find_all('td')
            data_row = [cell.get_text(strip=True) for cell in cells]
            data_rows.append(data_row)
    
        header = table.find('tr')
        cells = header.find_all('th')
        header_row = [cell.get_text(strip=True) for cell in cells]
        df = pd.DataFrame(data_rows, columns=header_row)
