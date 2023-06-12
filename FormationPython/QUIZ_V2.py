question1 = ("Quel est le capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quel est la capitale de l'italie ?", ("Rome", "Venise", "Milan", "Pise"), "Rome")
question3 = ("Quel est la capitale de l'inde ?", ("Kalkota", "Gao", "New Delhi", "Mumbai"), "New Delhi")
question4 = ("Quel est la capitale du Sénégal ?", ("Kédouguou", "Saint-Lious", "Thies", "Matam", "Dakar"), "Dakar")
score = 0
Q = (question1, question2, question3, question4)
def qcm(question_posee):
    nb = 1
    global score
    print(question_posee[0])
    print("Vos choix de réponse sont :")
    choix = question_posee[1]
    for i in choix:
        print(nb, "-", i)
        nb +=1
    reponse = input("Entré votre choix : ")
    if reponse.lower() == question_posee[2].lower():
        print("")
        print("Bonne Réponse")
        print("")
        score += 1
    else:
        print("")
        print("Mauvaise Réponse")
        print("")

for i in Q:
    qcm(i)
print("")
print("Score : ", score,"/4")