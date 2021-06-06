from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        div = soup.find('div', {'title': 'buyer-info'})

        # div.contents = []
        # a contents tambien se lo puede escribir.

        div.div.string = '' # elimina el texto busses carson

        # * Se puede extraer un elemento 

        span = div.span.extract()

        print(div)
        print(span)