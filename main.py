from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')
        
        title = soup.find('title')
        
        print(title)
        print(title.name)

        print(title.text)
        print(title.get_text()) # igual que text
