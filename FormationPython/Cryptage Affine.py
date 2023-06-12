# Cryptage Affine
m = "dcodesaitdecrypterlechiffreaffine"

# Fonction de cryptage y = (ax + b) mod 26

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Cryptage(mes):
    result = ""
    print("nous allons définir notre fontion de cryptage affine...")
    a = input("donner la valeur de a: ")
    a = int(a)
    b = input("donner la valeur de b: ")
    b = int(b)
    for i in mes:
        x = alphabet.index(i)
        print
        y = ((a*x)+b)%26
        result += alphabet[y]
    print("Le message décrypter est : "+result)

def deCrypter(mes):
    result = ""
    
Cryptage(m)



