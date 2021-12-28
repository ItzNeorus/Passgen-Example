import json
import random
import string
import sys

config = {}

with open('config.json', 'r') as r: # Load data in config.
	config = json.load(r)

i = 0 # Index for arguments.

for p in sys.argv: # Arguments initilization. Example: python Passgen.py (First Length) (Second Length) (Ascii Symbol Chance)
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

if config['lengthFirst'] > config['lengthSecond']: # Error initilization.
	print('Error (Invalid value) in config.json(lengthFirst).')
	exit()
else:
	pass

pwg = ''

for i in range(random.randint(config['lengthFirst'], config['lengthSecond'])): # Genering password.
	chance = random.random() # Ascii symbol chance.
	if chance < config['asciiSymbolChance']: # Insert ascii symbol.
		symbols = string.ascii_lowercase
		symbol = random.choice(symbols) # Random ascii symbol.
		pwg = pwg + symbol # Gluing.
	else:
		symbol = random.randint(0, 9) # Random number.
		symbol = str(symbol)
		pwg = pwg + symbol # Gluing.

print(pwg) # Print genering password.

# End. Bye bye :)
