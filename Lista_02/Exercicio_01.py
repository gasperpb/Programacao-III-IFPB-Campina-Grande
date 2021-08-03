#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

MAXBYTES = 65535

# 1 - criando uma exceção

class TimeExceeded(OSError):
    pass
    
####################

def find_server(sock):
	
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	
	delay = 0.5
	tentativas = 0
		
	while True:
		
		sock.sendto(b"DISCOVERY", ('127.255.255.255',50000))
		
		sock.settimeout(delay)
		
		try:
			data , address = sock.recvfrom(MAXBYTES)
		
		except socket.timeout:
			# 2 - contanto as tentativas
			tentativas += 1
			
			print("Servidor não encontrado!")
			
			# 3 - verificando as tentativas
			if tentativas == 30:
				# 4 - lançando a exceção
				raise TimeExceeded
		
		else:
			print("Servidor encontrado em {}".format(address))
			break
	
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 0)
	
	sock.settimeout(None)
	
	return address

def main():
	
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	
	# 5 - executando em um bloco seguro
	try:
		address = find_server(sock)
	
	# 6 - capturando exceção
	except TimeExceeded:
		print("SERVIDOR NÃO ENCONTRADO!!")
		print("Abortando...")
		sock.close()
		
		# 7 - encerrando
		return
	
	sock.connect(address)
	
	while True:
		
		text = input("Texto: ")
		
		if text == 'bye':
			sock.send(b'BYE')
			data = sock.recv(MAXBYTES)
			break
		
		sock.send(b'UPPER' + text.encode())
		
		data = sock.recv(MAXBYTES)
		
		print("Servidor responde: {}".format(data.decode()))
		
	
	sock.close()
	return 0

if __name__ == '__main__':
	main()