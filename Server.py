import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created ")

s.bind(('localhost',9999))
print('Socked Binded')
s.listen(3)
print('Server is Listening for Clients')


while True:
    c,address = s.accept()
    message = c.recv(1024).decode()
    print('Connected with ',address,message)
    c.close()

