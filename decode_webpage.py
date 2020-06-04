import requests

from bs4 import BeautifulSoup

url = "https://www.etu.ru/en"

resp = requests.get(url)
print(resp)

soup = BeautifulSoup(resp.text,'html.parser')

for headings in soup.find_all(class_= 'nav navbar-nav target-groups'):
    print(headings)