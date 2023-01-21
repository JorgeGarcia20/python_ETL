from bs4 import BeautifulSoup
import requests

URL = 'https://www.larepublica.co/indicadores-economicos/movimiento-accionario'

result = requests.get(URL)
content = result.text

soup = BeautifulSoup(content, 'lxml')

container = soup.find('div', class_='tableActions')

name_action = container.find_all('a', class_='nameAction')
volume_action = container.find_all('span', class_='price')


actions = []
for action in name_action:
	actions.append(action.get_text())

prices = []
for price in volume_action:
	prices.append(price.get_text())

prices = prices[::2]

prices_cleaned = []
for p in prices:
	n_p = p.strip('$').strip(' ').replace('.', '').replace(',', '.')
	prices_cleaned.append(float(n_p))
