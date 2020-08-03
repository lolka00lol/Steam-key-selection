from time import sleep
import os

key = input('Key: ')
os.system('cls')

x = 0
while 10 > x:
	key_with_number = key.replace('*', str(x))
	print(key_with_number)
	x += 1

sleep(120)