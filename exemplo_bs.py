from bs4 import BeautifulSoup
import requests

url = ""
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('title')
for title in titles:
    print(title.text)

