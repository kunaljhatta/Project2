import socket
import sys

port = int(sys.argv[1])
s = socket.socket()
s.bind(('', port))
s.listen()
while True:
    new_conn = s.accept()
    new_socket = new_conn[0]
    request = new_socket.recv(4096).decode()
    while True:
        if "\r\n\r\n" in request:
            break
    req = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!\r\n"
    new_socket.sendall(req.encode())
    print("Closing the socket")
    new_socket.close()
