import socket

s = socket.socket()

port = 12345

s.bind(('', port))

s.listen(5)

while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    c.send('Thank you for connecting'.encode())
    c.close()
    break
