def affiche_prenom():
    prenom = input("Quel est votre prenom : ")
    return prenom
    
def affiche_age(prenom):
    age = input("Quel age as-tu? ")    
    str_age = str(age)
    return age

def affiche_infos(prenom, age, taille=0):   #taille est une parametre optionnel
    print("Vous vous appelez "+prenom+" et vous avez "+age+" ans")
    int_age = int(age)
    if int_age >= 18:
        print("Vous etez majeur")
    else:
        print("vous etez mineur")
    if not taille == 0:
        print("Taille ; "+taille) 

"""prenom1 = affiche_prenom()
prenom2 = affiche_prenom()

age1 = affiche_age(prenom1)
age2 = affiche_age(prenom2)

affiche_infos(prenom1, age1)
affiche_infos(prenom2, age2)"""

for i in range(0,3):
    prenom = "pers"+str(i+1)
    prenom = affiche_prenom()
    age = affiche_age(prenom)
    affiche_infos(prenom, age)




    