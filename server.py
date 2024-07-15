import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('localhost',5003))
server.listen()


message = 'Hello from nowhere !'

while True:
    client,addr = server.accept()
    print('Connection is made to :', addr)
    while True:
        print('POINT - Before recieveing: ', type(client))
        request = client.recv(4096)
        if not request:
            break
        else:
            response = message.encode()
            client.send(response)