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

# conectando ao banco
conexao = sqlite3.connect("orbita.db")
cursor = conexao.cursor()

# inserindo cada titulo no banco
for titulo in titulos:
    nome_missao = titulo.text.strip()
    cursor.execute('''
        INSERT INTO lancamentos_espaciais (nome_missao, veiculo_lancador, nome_agencia, carga, destino, data, horario_utc3, local_lancamento, resultado, descricao)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (nome_missao, None, None, None, None, None, None, None, None, None))
conexao.commit()
conexao.close()