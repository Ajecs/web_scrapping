from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        for element in soup.find_all('div', {'title': 'buyer-info'}):
            div = element.div
            span = element.span
            # En caso de no encontrarse el elemento se devuelve none
            print(div.text, span.text) #
