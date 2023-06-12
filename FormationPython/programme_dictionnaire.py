"""    personne = {'Nom': 'Mouhamed', 'Age': 23, 'taille': 1.85}

    print(personne['Nom'])
    print(personne['Age'],"ans")
    print(personne['taille'])

    personne['travail'] = 'étudiant'


    personne['domaine'] = 'informatique'
    personne['langage_appris'] = ["Langage C", "Java", "PHP", "Javascript", "C#", "HTML", "CSS", "Python"]

    print(personne) """


# Recherche sur liste VS Recherche sur dictionnaire

    # Sur listes

"""personnes = [
        ("Mouhamed", 23, 1.85), 
        ("Awa", 23, 1.65), 
        ("Ibrahim", 2, 0.8)
    ]

def Recherche_Personne(nom, liste):
    for i in liste:
        if i[0] == nom:
            print(i)
    return None

Recherche_Personne("Mouhamed", personnes)"""
  
    # Sur dictonnaire

personnes_2 = {
        "Mouhamed": (23, 1.85), 
        "Awa": (23, 1.65), 
        "Ibrahim": (2, 0.8)
    }

#infos_personne = personnes_2["Mouhamed"]
#print(infos_personne)

#Gérer le cas d'erreur quand la personne rechercher n'existe pas

infos_personne = personnes_2.get("Modou")
if infos_personne == None: # OU if not infos_personne
    print("La personne recherché n'existe pas !")
else:
    print(infos_personne)
