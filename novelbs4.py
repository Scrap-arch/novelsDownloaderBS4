from bs4 import BeautifulSoup
import requests
import pyperclip
import unicodedata

url = 'http://boxnovel.org/overgeared-chapter-'

capInicio = 601
capFim = 620
todosCap = []

for i in range(capInicio, capFim + 1):
    response = requests.get(f'{url}{i}').text
    soup = BeautifulSoup(response, 'lxml')
    conteudo = soup.find('div', id='chr-content')
    #conteudo = conteudo.p
    #conteudo = str(conteudo)
    todosCap.append(conteudo)
    #hw_berlin.distance_centre_km = re.sub('[^0-9.]','', x) for x in hw_berlin.distance_centre_km
    print(i)


pyperclip.copy(str(todosCap))

# with open(f'Overgeared {capFim}.html','w') as f:
    
#     for i in todosCap:
#         i = unicodedata.normalize('NFKD', str(i)).encode('ascii','ignore')
#         f.write(str(i))
#     f.close()

print('Done')