import requests

URL = 'http://econpy.pythonanywhere.com/ex/001.html'


if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text 
        # <div title="buyer-name">Carson Busses</div>
        regexa = '<div title="buyer-name">'
        regexb = '</div>'

        for line in content.split('\n'):
            if regexa in line:
                # print(line)
                start = line.find(regexa) + len(regexa)
                end = line.find(regexb)
                title = line[start:end]

                print(title)

        
