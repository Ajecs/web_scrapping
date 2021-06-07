import requests
from datetime import datetime
from bs4 import BeautifulSoup

DOMAIN = 'https://pokemondb.net/'
URL = 'https://news.google.com/topstories?hl=es-419&gl=US&ceid=US%3Aes-419'


if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        now = datetime.now().strftime('%d_%m_%Y')

    with open(f'news/news_{now}.txt', 'w+') as file:
        for element in soup.find_all('h3', class_='ipQwMb ekueJc RD0gLb', limit=20):
            title = element.a.text
            file.write(title + '\n')

    print('Archivo generado de forma exitosa')
