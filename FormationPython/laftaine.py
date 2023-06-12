from random import randint
lance_result = []
def laftaine_listes(n):
    for i in range(0, n+1):
        resutl = randint(1, 6)
        print(resutl)
        if resutl == 6:
            print("Le liévre a gagné")
        else:
            lance_result.append(resutl)

        if len(lance_result) == n:
            print("La tortue a gagné ")
    print("le dé a tiré "+str(lance_result))
laftaine_listes(6)
