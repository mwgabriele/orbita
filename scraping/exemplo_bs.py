import requests
from bs4 import BeautifulSoup

# fazendo a requisição para a página de notícias
url = 'https://www.nasa.gov/a-to-z-of-nasa-missions/'
response = requests.get(url)
html = response.text

# criando o objeto beautifulsoup
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())