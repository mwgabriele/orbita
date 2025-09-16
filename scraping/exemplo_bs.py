import requests
from bs4 import BeautifulSoup

# fazendo a requisição para a página de notícias
url = 'https://www.nasa.gov/a-to-z-of-nasa-missions/'
response = requests.get(url)
html = response.text

# criando o objeto beautifulsoup
soup = BeautifulSoup(html, 'html.parser')

titulos = soup.select("ul.arrow-list a")

# extraindo e imprimindo titulos
for titulo in titulos:
    print(titulo.text)