import socket
print("Création d'un socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connexion faite")
print("Connexion à l'hote distant")
s.connect(("www.eni.fr", 80))
print("Connexion faite")
