from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        div = soup.find('div', string='Carson Busses')

        # * next_sibling

        # * previous_sibling
        print(div.next_sibling)  # el nodo "\n"
        print(div.next_sibling.next_sibling)  # el nodo "span"
        print(div.previous_sibling)  # de nuevo a \n

        for element in div.previous_siblings:
            # devuelve un iterador (generator)
            print(element)
