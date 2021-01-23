import requests
url = 'http://0.0.0.0:8000/image/raw/'
files = {'media': open('/Users/johnbensen/Downloads/IMG_0022.png', 'rb')}
requests.post(url, files=files)