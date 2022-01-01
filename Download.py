import requests
import os
from bs4 import BeautifulSoup


def get_url_paths(url, ext='', params={}):
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return parent

url = 'https://mtgjson.com/api/v5/'
ext = 'json'
result = get_url_paths(url, ext)
re = requests.get(result[0])

if not os.path.exists("./json"):
    os.makedirs("json")

for i in range(len(result)):
    b=result[i].split("/")
    open("json/"+b[5], "wb").write(re.content)
