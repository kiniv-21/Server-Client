import socket
c = socket.socket()
c.connect(('localhost',9999))
message = input("Enter Your Message")
c.send(bytes(message,'utf-8'))
c.close()