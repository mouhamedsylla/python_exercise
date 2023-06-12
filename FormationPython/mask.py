import ipaddr
# CIDR (Classless Inter-Domain Routing). Elle donne le numero du réseau suivi par une barre oblique(/) et le nombre de bit
# à 1 dans la notation binaire du masque de sous de réseau.
ip = input("Veillez votre addresse ip reseaux en notation CIDR: ")
mask = ipaddr.IPv4Network(ip)
maskSous_reseau = mask.netmask

print("Votre masque de sous réseau est : "+str(maskSous_reseau))