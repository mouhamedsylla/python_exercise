# Chiffrement de césar/
Message = "ak"#"yirb"#"uahhks"


#key = 3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def chiffrement(m):
    Mes_crypte = ""
    Ek = 0
    m = m.lower()
    m_list = list(m)
    for i in m_list:
        if i == ' ':
            a = m_list.index(i)
            m_list.pop(a)
    m_new = ""
    for i in m_list:
        m_new += i 
    for i in m_new:
        ind = alphabet.index(i)
        Ek = (ind + key) % 26
        Mes_crypte += alphabet[Ek]
    print("Le message crypté est : "+Mes_crypte)

def dechiffrement(c):
    Dk = 0
    Mes_decrypt = ""
    for i in c:
        ind = alphabet.index(i)
        Dk = (ind - key) % 26
        Mes_decrypt += alphabet[Dk]
    print("Le message décrypté est : "+Mes_decrypt)

# Trouver la clé

for i in range(0, 26):
    key = i
    dechiffrement(Message)
    print("Le clé est : "+str(i))
    print("*********---------************")
    print()

dechiffrement(Message)