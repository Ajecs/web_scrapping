from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        span = soup.find('span', class_= 'item-price')

        print(span.parent)
        print(span.parent.parent.name) # seria la etiqueta 'abuelo' -> body
        print(span.parent.parent.parent.name) # seria la etiqueta 'bisabuelo' -> html
        print(span.parent.parent.parent.parent.name) # seria la etiqueta 'tatarabuelo' -> document
        print(span.parent.parent.parent.parent.parent) # no existe padre -> None 

        
        # * todos los padres de una etiqueta
        for parent in span.parents:
            print (parent.name) # div body html [document]

        for child in span.descendants:
            print(child.name) # None