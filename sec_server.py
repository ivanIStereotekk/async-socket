import socket
import selectors

selector = selectors.DefaultSelector()


def server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('localhost',5003))
    server.listen()
    selector.register(fileobj=server,events=selectors.EVENT_READ,data=accept_conn)
    
def accept_conn(server):
    client,addr = server.accept()
    print('Connection is made to :', addr)
    selector.register(fileobj=client,events=selectors.EVENT_READ,data=send_msg)


def send_msg(client):        
    incoming = client.recv(4096)
    print("RECIEVED MESSAGE :", incoming.decode())
    if incoming:
        mess_body = "SENT MESSAGE :" + str(input('Type something :')) + '\n'
        client.send(mess_body.encode())
        
    else:
        selector.unregister(client)
        client.close()
        
    
def event_loop():
    while True:
        events = selector.select()
        for key,_ in events:
            callback = key.data
            callback(key.fileobj)
            
    
    
if __name__ == '__main__':
    server()
    event_loop()