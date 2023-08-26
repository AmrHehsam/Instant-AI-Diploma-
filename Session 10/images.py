import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


data = getdata("https://github.com/")
soup = BeautifulSoup(data, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])
