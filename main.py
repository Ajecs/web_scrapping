from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        div = soup.find('div', {'title': 'buyer-info'})

        # * Para acceder a los valores de cada elemento se debe aplicar como si fuera un diccionario
        print(div['title'])

        # * como en un diccionario se puede acceder al valor del key mediante el metodo get
        # que permite un valor por defecto en caso de no encontrar el key

        print(div.get('titles', 'valor por default'))

        div['id'] = 'item01'
        div['title'] = 'nuevo-titulo' # sobreescribe el valor del atributo title
        div.div.string = 'valor modificado'
        div.span.string = '$1000.50'
 
        print(div)
        print(soup.prettify)