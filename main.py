import requests
import re

URL = 'http://econpy.pythonanywhere.com/ex/001.html'


with open('econpy.html', 'r') as file:
    # es recomendable evitar muchas peticiones al servidor. 
    # Por ende es buena idea leer un archivo local de los datos de la web
    
    content = file.read()
    
    regex = '<div title="buyer-name">(.+?)</div>'

    for title in re.findall(regex, content):
        print(title)
        
