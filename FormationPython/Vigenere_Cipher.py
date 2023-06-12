from random import randint



# Choix d'un key aléatoirement
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def key(num):
    k = ''
    for i in range(0, num):
        char = randint(0, 25)
        k += alphabet[char]
    return k

# Chiffrement
def encryption(m, c):
    encrypt_mess = ''
    m_inttab = []
    c_inttab = []
    Ei = 0
    for i in m:
        a = alphabet.index(i)
        m_inttab.append(a)
    for j in c:
        b = alphabet.index(j)
        c_inttab.append(b)
    #for l in range(0, len(m_inttab)):
    l= 0
    p = 0
    tab_Ei = []
    while l != len(m_inttab):
        d = c_inttab[p]
        p += 1
        if p == len(c_inttab):
            p = 0
        e = m_inttab[l]
        l += 1
        Ei = (e + d) % 26
        tab_Ei.append(Ei)
    
    for i in tab_Ei:
        encrypt_mess += alphabet[i]
    
    return encrypt_mess

# Dechiffrement
def decryption(m, c):
    decrypt_mess = ''
    m_inttab = []
    c_inttab = []
    Di = 0
    for i in m:
        a = alphabet.index(i)
        m_inttab.append(a)
    for j in c:
        b = alphabet.index(j)
        c_inttab.append(b)
    #for l in range(0, len(m_inttab)):
    l= 0
    p = 0
    tab_Di = []
    while l != len(m_inttab):
        d = c_inttab[p]
        p += 1
        if p == len(c_inttab):
            p = 0
        e = m_inttab[l]
        l += 1
        Di = (e - d + 26) % 26
        tab_Di.append(Di)
    for i in tab_Di:
        decrypt_mess += alphabet[i]
    
    return decrypt_mess

if __name__ == "__main__":
    message = input("Entrer le message en clair : ")
    n = randint(3, 5)
    cle = key(n)    
    mess = encryption(message, cle)
    print(mess)
    print()
    print()
    mess_decrypt = decryption(mess, cle)
    print(mess_decrypt)