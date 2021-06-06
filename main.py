import requests

URL = 'http://econpy.pythonanywhere.com/ex/001.html'


if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text # devuelve un string

        # print(content)

        # generar archivo local
        with open('econpy.html', 'w+') as file:
            file.write(content)
