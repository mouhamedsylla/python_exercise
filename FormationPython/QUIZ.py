score = 0
def qcm(pays, ville1, ville2, ville3, ville4, bonRep):
    global score
    print("Question : Quel est la capitale de "+pays)
    print("(a) "+ville1)
    print("(b) "+ville2)
    print("(c) "+ville3)
    print("(d) "+ville4)
    print()

    print("Pour votre réponse entrer la lettre a, b, c ou d")
    reponse = input("Reponse : ")

    if reponse == bonRep:
        print("Bonne Réponse")
        score += 1
    
    else:
        print("Mauvaise Réponse")


def quiz():
    qcm("Sénégal", "Kédouguou", "Saint-Lious", "Thies", "Dakar", 'd')
    print()
    qcm("France", "Paris", "Bordeaux", "Marseille", "Nante", 'a')
    print()
    qcm("Inde", "Kalkota", "Gao", "New Delhi", "Mumbai", 'c')
    print()
    qcm("Etat Unis", "New York", "Washington", "Texas", "Miami", 'b')



quiz()
print("Score : "+str(score)+"/4")
