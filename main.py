from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        div = soup.find('div', {'title': 'buyer-info'})

        for child in div.children:
            # * el atributo children devuelve un iterador
            print(child)

        # print(div.contents) 
        #  * El atributo content devuelve una lista que contiene todos los nodos hijos

        # div_item = div.contents[1]
        # span_item = div.contents[3]

        # print(div_item.text, span_item.text)