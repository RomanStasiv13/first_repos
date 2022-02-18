# Task 1
# Robots.txt
# Download and save to file robots.txt from wikipedia, twitter websites etc.

import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')

with open('robots.txt', 'w', encoding='utf-8') as file:
    file.write(soup.getText())
    file.close()
