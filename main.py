from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        # * OPCION 1
        # for element in soup.find_all(attrs={'class': 'item-price'}):

        # * OPCION 2
        for element in soup.find_all(class_='item-price'):
            # ! de no existir clase no aparece nada. Debe el mismo orden que la etiqueta
            print(element.text)
