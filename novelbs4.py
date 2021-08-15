from bs4 import BeautifulSoup
import requests
import pyperclip
import unicodedata

url = 'http://boxnovel.org/overgeared-chapter-'

capInicio = 641
capFim = 650
todosCap = []

for i in range(capInicio, capFim + 1):
    response = requests.get(f'{url}{i}').text
    soup = BeautifulSoup(response, 'lxml')
    conteudo = soup.find('div', id='chr-content')
    todosCap.append(conteudo)
    print(i)


pyperclip.copy(str(todosCap))

print('Done')