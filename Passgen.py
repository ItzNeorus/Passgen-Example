import json
import random
import string
import sys

config = {}

with open('config.json', 'r') as r:
	config = json.load(r)

i = 0

for p in sys.argv:
	if p == 'Passgen.py':
		pass
	else:
		i = i + 1
		try:
			p = int(p)
		except:
			p = float(p)
		if i == 1:
			config['lengthFirst'] = p
		elif i == 2:
			config['lengthSecond'] = p
		elif i == 3:
			config['asciiSymbolChance'] = p

if config['lengthFirst'] > config['lengthSecond']:
	print('Error (Invalid value) in config.json(lengthFirst).')
	exit()
else:
	pass

pwg = ''

for i in range(random.randint(config['lengthFirst'], config['lengthSecond'])):
	chance = random.random()
	if chance < config['asciiSymbolChance']:
		symbols = string.ascii_lowercase
		symbol = random.choice(symbols)
		pwg = pwg + symbol
	else:
		symbol = random.randint(0, 9)
		symbol = str(symbol)
		pwg = pwg + symbol

print(pwg)
