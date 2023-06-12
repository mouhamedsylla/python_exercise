from random import randint
NB_VIE = 4

print(f"Vous avez {NB_VIE} vies")

nbMagik = randint(1, 10)



vie = 1
while vie <= NB_VIE:
    b = False 
    while b == False:
        entree = input("Quel est le nombre magique (entre 1 et 10) ? \n")
        try:
            int_entree = int(entree)
            b = True
        except: 
                if b == False:
                    print("ERREUR! Vous devez entrer un nombre entier\n")
        else:
            if int_entree <1 or int_entree > 10:
                    print("ERREUR!! Votre nombre n'est compris entre 1 et 10\n")
                    b = False

    if int(nbMagik) < int(entree):
        print("Le nombre magique est plus petite\n")
        
    elif int(nbMagik) > int(entree):
        print("Le nombre magique est plus grand\n")
    else:
        print("Bravo! Vous avez gagnez\n")
        break 
    reste = NB_VIE - vie
    if not reste == 0:
        print("il reste "+str(reste)+" vie")
    vie += 1
    condition1 = int(nbMagik) == int(entree)
    condition2 = reste == 0 
    
    if not condition1 and condition2:
        print("Vous avez perdu")