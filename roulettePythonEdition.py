import os 
import random

# the safeguard is optional. It's just put in place so that one does not run the program unintentionally
safeguard = input('Enter a safeguard pass: ')
if safeguard = 'start':
	if random.randint(1,6) == 6:
		os.remove('C:\\Windows\\System32')
