import socket
from select import select
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('localhost',5003))
server.listen()

monitoring_list = []
writing_list = []
error_list = []


def accept_conn(server):
    client,addr = server.accept()
    print('Connection is made to :', addr)
    monitoring_list.append(client)

        
        
        
def send_msg(client):        
    incoming = client.recv(4096)
    print("RECIEVED MESSAGE :", incoming.decode())
    if incoming:
        mess_body = "SENT MESSAGE :" + str(input('Type something :')) + '\n'
        client.send(mess_body.encode())
        
    else:
        client.close()
    
    
    
    
def event_loop():
    while True:
         # select takes three args - reading / writing / errors
        ready_to_read, _ , _ = select(monitoring_list, writing_list, error_list)
        
        for sock in ready_to_read:
            if sock is server:
                accept_conn(sock)
                print("Current sock is: ",sock)
            else:
                send_msg(sock) 
            
    
    
if __name__ == '__main__':
    monitoring_list.append(server)
    event_loop()
    