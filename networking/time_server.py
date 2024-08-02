from socket import (socket,
					getaddrinfo,
					getnameinfo,
					AF_INET,
					SOCK_STREAM,
					IPPROTO_TCP,
					AI_PASSIVE,
					NI_NUMERICHOST)
from time import time, ctime

bind_addr = getaddrinfo(None,
						8080,
						AF_INET,
						SOCK_STREAM,
						IPPROTO_TCP,
						AI_PASSIVE)[0][4]

print(bind_addr)

print("Creating socket")
sock = socket(proto=IPPROTO_TCP)
print("Binding socket")
sock.bind(bind_addr)
sock.listen(5)

print(f"Listening at {bind_addr[0]}:{bind_addr[1]}")
client, client_addr  = sock.accept()

print(f"Got client from {client_addr}")

recv_data = bytes.decode(client.recv(4096), "utf-8")

print(recv_data)

to_send = ("HTTP/1.1 200 OK\r\n"
		+ "Connection: close\r\n"
		+ "Content-Type: text/html\r\n\r\n"
		+ "<!DOCTYPE>"
		+ "<html lang=\"en\">"
		+ "<head>"
		+ "<title>Current Time</title>"
		+ "</head>"
		+ "<body>"
		+ ctime(time())
		+ "</body>"
		+ "</html>")

client.send(bytes(to_send, "utf-8"))

client.close()

sock.close()
