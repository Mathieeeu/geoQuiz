import socket

hostname = socket.gethostname()
ip_client = socket.gethostbyname(hostname)
print('Ton Adresse IP : {}'.format(ip_client))

ClientMultiSocket = socket.socket()

pseudo=input("\nPseudo : ")
ip=input("IP de l'hôte : ")
if ip == "":
    ip="localhost"
    ip_client="localhost"
elif ip == "dev":
    ip="localhost"
    ip_client=input("IP du client : ")


print(pseudo,ip)

host = ip
port = 2003

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)

message = (str(pseudo)+","+str(ip_client)+",connexion")
ClientMultiSocket.send(str.encode(message))
res = ClientMultiSocket.recv(1024)
if res.decode('utf-8').startswith('pseudo_update,'):
    pseudo=res.decode('utf-8').replace('pseudo_update,','')
    print("votre pseudo est maintenant {}".format(pseudo))
try:
    score=int(res.decode('utf-8'))
except:
    score=0
print("score="+str(score))
while True:
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
    if  input("point ou pas point ")=="oui":
        score+=1
        message = (str(pseudo)+","+str(ip_client)+","+str(score))
        ClientMultiSocket.send(str.encode(message))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))


ClientMultiSocket.close()
