import requests
import json

url = 'http://127.0.0.1:8000/test1/test2/'
files = {'media': open('/Users/johnbensen/Downloads/IMG_0022.png', 'rb')}


Matrix = {"matrix": "[1,2,3],[4,5,6],[7,8,9]"}
response = requests.post(url, Matrix)
print(Matrix)
print(response.text)