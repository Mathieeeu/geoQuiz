import socket


ClientMultiSocket = socket.socket()

pseudo=input("Pseudo : ")
ip=input("IP de connexion : ")
if ip == "":
    ip="localhost"

print(pseudo,ip)

host = ip
port = 2004

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)

message = (str(pseudo)+","+str(ip)+",connexion")
ClientMultiSocket.send(str.encode(message))
res = ClientMultiSocket.recv(1024)
try:
    score=int(res.decode('utf-8'))
except:
    score=0
print("score="+str(score))
while True:
    if  input("point ou pas point ")=="oui":
        score+=1
        message = (str(pseudo)+","+str(ip)+","+str(score))
        ClientMultiSocket.send(str.encode(message))
        res = ClientMultiSocket.recv(1024)
        print(res.decode('utf-8'))


ClientMultiSocket.close()
