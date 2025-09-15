import requests
from bs4 import BeautifulSoup

# fazendo a requisição para a página de notícias
url = 'https://spaceflightnow.com/launch-schedule/'
response = requests.get(url)
html = response.text

# criando o objeto beautifulsoup
soup = BeautifulSoup(html, 'html.parser')
# buscando todos os elementos que contém os títulos das notícias
titulos = soup.find_all('span', class_="mission")

# extraindo e imprimindo os títulos
for titulo in titulos:
    print(titulo.text.strip())