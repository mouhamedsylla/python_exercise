#FONCTION RECURSIVE
#C'est une fonction qui s'appelle elle meme

"""def a(n, limit):
    if n > limit:
        return
    print("n :", n )
    a(n*n, limit)

a(2, 100000)"""

def demander_choix_utilisateur(min, max):
    reponse = input(f"Quel est votre choix compris entre {min} et {max} : ")

    try:
        str_reponse = int(reponse)
        if max < str_reponse or str_reponse < 1:
            print(f"ERREUR! Votre nombre n'est pas compris entre {min} et {max}")
            print()
            return demander_choix_utilisateur(min, max)
        else:
            return str_reponse
    except:
        print("ERREUR! Vous devez entrer un nombre")
        print()
        return demander_choix_utilisateur(min, max)


choix = demander_choix_utilisateur(1, 4)
print("Votre choix est : "+str(choix))