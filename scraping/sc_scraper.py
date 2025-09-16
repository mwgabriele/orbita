import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.supercluster.com/launches'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

for span in soup.find_all('span'):
    titulos = [t.strip().strip('"') for t in span.stripped_strings]
    if len(titulos) > 1:
        segundo = titulos[1]   # pega só o segundo
        print(segundo)
