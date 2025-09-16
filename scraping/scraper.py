import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.nasa.gov/a-to-z-of-nasa-missions/'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

#titulos = soup.select("ul.arrow-list a")
links = soup.select('p > a')

for link in links:
    print(link)

# conectando ao banco
conexao = sqlite3.connect("orbita.db")
cursor = conexao.cursor()

# inserindo cada titulo no banco
for titulo in links:
    nome_missao = titulo.text.strip()
    cursor.execute('''
        INSERT INTO lancamentos_espaciais (nome_missao, veiculo_lancador, nome_agencia, carga, destino, data, horario_utc3, local_lancamento, resultado, descricao)
        VALUES (?)
        ''', (nome_missao, None, None, None, None, None, None, None, None, None))
conexao.commit()
conexao.close()

