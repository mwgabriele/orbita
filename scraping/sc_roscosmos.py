import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.spacelaunchschedule.com/category/russian-federal-space-agency-roscosmos/'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(response.text, 'html.parser')

