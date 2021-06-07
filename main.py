import requests
from bs4 import BeautifulSoup

DOMAIN = 'https://pokemondb.net/'
URL = '/pokedex/all'

if __name__ == '__main__':
    response = requests.get(DOMAIN + URL)
    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        table = soup.find('table', {'id': 'pokedex'})
        for row in table.tbody.find_all('tr'):
            columns = row.find_all('td', limit=3)  # limite de nodos a obtener
            
            name = columns[1].a.text
            type = [a.text for a in columns[2].find_all('a')] # * list comprehension
            # print(*type) # * transforma el resultado(list) en un string

            link = DOMAIN + columns[1].a['href']

            print (link)