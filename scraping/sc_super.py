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
        segundo = titulos[1]   # pegando só o segundo
        print(segundo)

# conectando ao banco
conexao = sqlite3.connect("missoes.db")
cursor = conexao.cursor()

# garantindo que a tabela exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS lancamentos_espaciais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_missao TEXT
)
""")

# extraindo e inserindo no banco
for i in titulos:
    nome_missao = i.get_text(strip=True)
    if nome_missao:
        print(nome_missao)
        cursor.execute("INSERT INTO lancamentos_espaciais (nome_missao) VALUES (?)",
                       (nome_missao,))

conexao.commit()
conexao.close()