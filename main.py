from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        a = soup.new_tag('a', href='www.google.com', target='_blank')
        a.string = 'Google'
        div = soup.new_tag('div', id='item01', title='item-data')
        div['new-attrs'] = 'new-attrs'
        div.append('\n')
        div.append(a)
        div.append('\n')

        # soup.body.append(div)
        soup.body.insert(1, div) # coloca en la posicion 1 de la lista contents

        print(soup.prettify) 
        # lo añade al final del body